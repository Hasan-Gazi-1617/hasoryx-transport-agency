# Hasoryx International Logistics Roadmap

## Product baseline

Business direction: global logistics platform.
Initial market: Bangladesh.
Design direction: premium corporate experience.
Scope: full platform, delivered in safe, testable phases.

## Phase 0 - Architecture and repository foundation
- [x] Inspect the existing Django repository and deployment configuration.
- [x] Confirm product direction and target architecture.
- [x] Create a dedicated feature branch.
- [x] Document architecture, domain data model, and delivery roadmap.
- [ ] Add environment-aware production settings.
- [ ] Add automated checks and a repeatable local setup guide.

## Phase 1 - Platform foundation
- Configure PostgreSQL for production and SQLite for local development only if DATABASE_URL is absent.
- Configure Django auth, sessions, middleware, secure cookies, and login/logout.
- Establish a custom user model before the first production database migration.
- Add role/group bootstrap command and protected staff dashboard shell.
- Add tests for authentication, permissions, CSRF, and customer/staff access boundaries.
- Configure Render PostgreSQL and persistent production settings without committing secrets.

## Phase 2 - Premium corporate website
- Refine responsive navigation, homepage, service pages, company profile, industries, network, contact, and quote enquiry.
- Establish design tokens, typography, reusable components, accessible forms, SEO metadata, and performance budgets.
- Keep claims about routes, fleet, offices, certifications, and partner networks factually accurate.

## Phase 3 - Customer and commercial workflow
- Customer organisations, contacts, addresses, and service catalogue.
- Quote request intake and internal quotation management.
- Booking request and approval lifecycle.
- Customer portal with organisation-scoped access.

## Phase 4 - Shipment and tracking
- Relational shipments, packages, route legs, and append-only tracking events.
- Migrate the existing JSON sample data and verify tracking parity.
- Public tracking with privacy-safe output and rate limiting.
- Internal shipment event management and exception handling.

## Phase 5 - Operations
- Pickup, dispatch, handover, delivery attempts, and proof of delivery.
- Fleet and driver assignment.
- Warehouse facilities, locations, and package scans.
- Operational queues and dashboards.

## Phase 6 - Finance and documents
- Quotes, invoices, payments, credit notes, tax configuration, and financial reports.
- Private document storage and access control.
- Email notifications and customer communication history.

## Phase 7 - Integrations and international readiness
- Carrier/provider adapter framework and verified carrier API integrations.
- Maps and route estimation.
- Payment provider integration after commercial onboarding.
- Multi-currency support and configurable exchange-rate records.
- Country, customs, trade-document, and partner workflows as legally and operationally appropriate.

## Phase 8 - Production readiness
- Automated tests, security review, backup/restore test, monitoring, logging, and incident procedures.
- Load and performance testing.
- Staff training and operational acceptance.
- Production launch checklist and staged rollout.

## Working rules
- Work in feature branches; do not commit unfinished changes directly to main.
- Keep each phase deployable where possible.
- Never store secrets, customer personal data, or real shipment documents in Git.
- Add tests for every business rule and permission boundary.
- Run checks before opening a pull request.
- Do not merge or deploy to production without an explicit release decision.
- Update this roadmap as each phase is implemented and verified.
