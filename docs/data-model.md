# Hasoryx Logistics Data Model

This is the proposed relational model. Implement models incrementally in their owning Django apps. Names are conceptual and may be refined during implementation.

## Identity and access

### User
Use Django's custom user model from the beginning, before the first production migration. Recommended: subclass AbstractUser and use email as the login identifier if the business confirms email-based login.

Key fields: email, phone, first_name, last_name, is_active, is_staff, date_joined.

### Role and permissions
Use Django Groups and Permissions for broad roles:
- Super Admin
- Operations Manager
- Booking Officer
- Shipment Operator
- Warehouse Staff
- Fleet Manager
- Finance Officer
- Customer Support
- Customer

Do not rely on role names alone. Enforce specific Django permissions and object-level ownership in views and domain services.

## Customers

### CustomerOrganisation
Fields: legal_name, display_name, customer_code, business_type, tax_identifier (optional), status, billing_email, created_at.

### CustomerContact
Fields: organisation, user (optional), name, email, phone, designation, is_primary.

### Address
Fields: owner/customer, label, contact_name, phone, address_line_1, address_line_2, city, district, postal_code, country_code, latitude, longitude, is_default.

## Services and commercial requests

### LogisticsService
Fields: code, name, mode (road, air, ocean, multimodal, warehousing), description, active, domestic_available, international_available.

### QuoteRequest
Fields: reference, customer, requested_service, origin_address, destination_address, cargo_description, package_count, gross_weight, chargeable_weight (optional), dimensions (structured), requested_pickup_date, requested_currency, status, notes, created_by, created_at.

### Quote
Fields: quote_number, request, version, valid_until, currency, subtotal, surcharges, tax, total, terms, status, created_by, approved_at.

## Booking and shipment

### Booking
Fields: booking_number, customer, quote (optional), service, shipper_address, consignee_address, requested_pickup_at, special_instructions, status, created_by, created_at.

### Shipment
Fields: tracking_number (unique, random/non-sequential), booking, customer, service, status, origin, destination, booked_at, estimated_delivery_at, delivered_at, created_at, updated_at.

### Package
Fields: shipment, package_reference, description, package_type, quantity, weight, length, width, height, declared_value (optional), declared_currency (optional).

### ShipmentLeg
Fields: shipment, sequence, transport_mode, origin, destination, planned_departure, actual_departure, planned_arrival, actual_arrival, carrier_partner (optional), external_reference (optional), status.

### TrackingEvent
Fields: shipment, event_code, status_label, description, location, occurred_at, recorded_at, source (internal/carrier), source_name, external_event_id (optional), visibility (public/internal), created_by (optional).

Tracking events should be append-only. Add a uniqueness strategy for external_event_id scoped to its provider to make carrier webhook processing idempotent.

## Operations

### ShipmentAssignment
Fields: shipment, assigned_team/user, assigned_at, released_at, assignment_type, notes.

### DeliveryAttempt
Fields: shipment, attempt_number, attempted_at, outcome, reason, notes, recorded_by.

### ProofOfDelivery
Fields: shipment, recipient_name, delivered_at, signature_file (private), photo_file (private), notes, recorded_by.

### OperationalException
Fields: shipment, category, severity, description, opened_at, resolved_at, resolution, assigned_to.

## Fleet and warehouse

### Vehicle
Fields: vehicle_number, registration_number, vehicle_type, capacity_weight, capacity_volume, status, current_odometer.

### Driver
Fields: user (optional), name, phone, licence_number, licence_expiry, status.

### Facility
Fields: code, name, facility_type (warehouse, hub, branch, port, airport), address, active.

### WarehouseLocation
Fields: facility, code, name, location_type, active.

### InventoryMovement
Fields: package, from_location, to_location, movement_type, quantity, scanned_at, scanned_by.

## Billing

### Invoice
Fields: invoice_number, customer, shipment (optional), booking (optional), currency, subtotal, tax, total, amount_paid, due_date, status, issued_at.

### Payment
Fields: invoice, amount, currency, method, provider_reference, status, paid_at, received_by, verified_by.

### CreditNote
Fields: credit_note_number, invoice, amount, currency, reason, status, created_by, approved_by.

Use DecimalField for all monetary values. Payment status and shipment status are separate concepts.

## Documents and communication

### ShipmentDocument
Fields: shipment, document_type, storage_key, original_filename, mime_type, size_bytes, uploaded_by, uploaded_at, visibility, checksum.

### Notification
Fields: recipient_user (optional), recipient_email/phone, channel, template_key, payload, status, sent_at, provider_reference, error_message.

### SupportTicket
Fields: ticket_number, customer, created_by, subject, category, priority, status, assigned_to, created_at, resolved_at.

### AuditLog
Fields: actor, action, entity_type, entity_id, before_data (redacted JSON), after_data (redacted JSON), ip_address (where appropriate), created_at.

## Important relationships and constraints

- A customer organisation can have many contacts, addresses, bookings, shipments, invoices, and tickets.
- A booking may become one or more shipments only where the operational model requires it; define this rule before implementing split/partial shipments.
- A shipment has many packages, legs, tracking events, assignments, delivery attempts, documents, and exceptions.
- A shipment may have at most one successful final delivery record unless an authorised correction workflow is used.
- A customer user must be linked to a customer organisation and may only access that organisation's records.
- Tracking number, booking number, quote number, invoice number, and ticket number must be unique.
- Use database constraints for uniqueness and valid ranges where practical.
- Use soft deactivation for business entities where historical references must remain valid.

## Implementation order

1. Custom User and role/permission setup.
2. Customer organisation, contact, and address.
3. Service catalogue and quote requests.
4. Booking and shipment.
5. Packages, legs, and tracking events.
6. Operations, delivery, and proof of delivery.
7. Billing and payments.
8. Fleet, warehouse, documents, notifications, support, and reports.
