# Hasoryx International Logistics Architecture

## Product direction

Hasoryx is a Bangladesh-launched logistics platform designed to support domestic transportation first and international logistics expansion later. The platform will combine a premium corporate website, customer self-service portal, and internal logistics operations system.

The platform must not claim to operate global routes, customs brokerage, or carrier integrations until the relevant partners, licences, contracts, and technical integrations exist. Features will distinguish between internally managed shipment events and verified third-party carrier events.

## Business capabilities

### Public website
- Corporate home, company profile, service catalogue, industry solutions, network and contact pages.
- Public shipment tracking using a non-sequential tracking reference.
- Quote request and shipment booking enquiry.
- Careers and customer support entry points.

### Customer portal
- Account profile and verified contact details.
- Create and manage booking requests.
- View own shipments and event timelines.
- Download authorised documents and invoices.
- Request quotations, submit support tickets, and receive notifications.

### Internal operations
- Role-based staff dashboard.
- Customer and booking management.
- Shipment creation, assignment, milestones, exceptions, and proof of delivery.
- Fleet, driver, warehouse, and consignment handling.
- Quotes, invoices, payments, refunds/adjustments, and operational reports.
- Audit trail for sensitive changes.

## Technology decisions

| Concern | Initial choice |
|---|---|
| Backend | Django 5.2 |
| Database | PostgreSQL |
| Web UI | Django templates, Bootstrap, JavaScript |
| Authentication | Django authentication and database sessions |
| Authorization | Django permissions and groups, with domain-level checks |
| API | Django REST Framework, introduced when needed |
| Static assets | WhiteNoise |
| Uploaded documents | Private S3-compatible object storage in production |
| Deployment | Render |
| Timezone | Asia/Dhaka for the initial operating team; store timestamps timezone-aware |
| Initial currency | BDT; design monetary records to support ISO currency codes |
| Background processing | Celery and Redis in a later phase |
| Maps and carrier APIs | Provider adapters; no hard dependency on a single provider |

## Django app boundaries

- `core`: public pages, shared utilities, health checks.
- `accounts`: user lifecycle, authentication, roles, staff access.
- `customers`: customer organisations, contacts, addresses, preferences.
- `services`: service catalogue, service availability and service rules.
- `bookings`: quote requests and booking lifecycle.
- `shipments`: consignments, packages, route legs, assignments.
- `tracking`: immutable tracking events, public tracking projection.
- `operations`: operational queues, exceptions, handovers and proof of delivery.
- `fleet`: vehicles, drivers, maintenance and availability.
- `warehouse`: facilities, storage locations, inventory movements and scans.
- `billing`: quotes, invoices, payments, credit notes and account balances.
- `documents`: document metadata, access policy and storage integration.
- `notifications`: email/SMS notification preferences and delivery records.
- `support`: customer enquiries and support tickets.
- `reports`: operational and financial reporting.
- `integrations`: carrier, map, payment and partner adapters.

Apps should be introduced incrementally. Do not create empty apps before the relevant feature is scheduled.

## High-level request flow

1. Browser requests a public page, customer page, or staff page.
2. Django security middleware and session middleware process the request.
3. Authentication middleware attaches the authenticated user.
4. URL routing dispatches to the owning app.
5. View/form or API serializer validates input.
6. Domain service applies business rules and database transaction.
7. Permission checks ensure the user can access the requested customer or shipment.
8. Response is rendered or returned as JSON.
9. Important state changes create audit and tracking records.
10. Notifications are queued after successful transaction commit.

## Security requirements

- Production secret keys must come from environment variables; never commit secrets.
- Production DEBUG must be false.
- Use HTTPS, secure session cookies, secure CSRF cookies, CSRF protection, and clickjacking protection.
- Use Django password hashers; never store plaintext passwords or reversible password encryption.
- Use Django sessions for browser login. Do not introduce JWT unless a separately justified API/mobile use case appears.
- Enforce role permissions and object-level ownership checks on every private view and API.
- Customers may only see their own bookings, shipments, documents, invoices, and support tickets.
- Staff access must be least-privilege and auditable.
- Public tracking must return a strict whitelist of safe fields, never contact details, internal notes, declared sensitive values, or private documents.
- Tracking references must be hard to guess and rate-limited.
- Validate file type, size, ownership, and access before accepting or serving documents.
- Record audit events for privileged actions, status overrides, financial changes, and permission changes.
- Back up PostgreSQL and private document storage; test restoration.

## Data and integration principles

- PostgreSQL is the source of truth for business records.
- Store money as decimal amounts with an ISO currency code, never floating point.
- Store timestamps as timezone-aware values in UTC; render in the user's or operating location's timezone.
- Keep shipment event history append-only. Corrections should be recorded as new audited events rather than silently rewriting history.
- Separate a booking request from an accepted shipment.
- Separate shipment status from payment status and delivery status.
- External carrier events must retain provider, external event ID, source timestamp, and raw/normalised status for traceability.
- Integration adapters must tolerate timeouts, retries, duplicate callbacks, and provider outages.
- Do not represent a planned integration as a live integration.

## Migration strategy

The current project is a small Django site with JSON-based public tracking. Preserve its public pages while migrating in controlled steps:
1. Add project documentation and a protected feature branch.
2. Add environment-aware PostgreSQL configuration and Django authentication/session support.
3. Add the first database-backed accounts and customer foundations.
4. Migrate shipment tracking from JSON to relational records with a one-time import and verification.
5. Add bookings, operations, billing, and customer portal incrementally.
6. Add external integrations only after partner/API credentials and test environments are available.

## Current implementation boundary

This document describes the target architecture, not completed functionality. The current repository still contains the original public Django pages and JSON tracking implementation. Each completed phase must be reflected in code, tests, and deployment configuration before being described as live.
