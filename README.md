# Hasoryx Transport Agency Limited

Django-based transport and logistics platform. The public marketing website and JSON-backed tracking page remain available while the operational platform is developed in phases.

## Technology
- Python 3.12 and Django 5.2
- PostgreSQL for production; SQLite for local development
- Django authentication, sessions, groups and permissions
- WhiteNoise for static files
- Render deployment

## Local development

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

Open http://127.0.0.1:8000/. Staff sign in at /accounts/login/; the protected staff dashboard is at /staff/; Django administration is at /admin/.

## Accounts and access

The project uses the custom accounts.User model. Create the first administrator with python manage.py createsuperuser. Superusers are automatically assigned the Super Admin role. Staff users must have is_staff=True to enter the staff dashboard. Roles currently defined are Super Admin, Operations, Dispatch, Warehouse, Finance, Customer Support and General Staff. Fine-grained module permissions will be introduced with each operational module.

Do not create the first database migration against the built-in Django User model. The custom user model is configured from the start.

## Database configuration

- Local development: omit DATABASE_URL; SQLite is used when DJANGO_DEBUG=True.
- Production: set DATABASE_URL to a managed PostgreSQL connection string. Production startup deliberately fails if it is missing, rather than silently using Render's ephemeral filesystem.
- Set DJANGO_SECRET_KEY, DJANGO_DEBUG=False, DJANGO_ALLOWED_HOSTS and DJANGO_CSRF_TRUSTED_ORIGINS in the hosting environment.

Before deploying this branch, provision PostgreSQL in Render and add its internal connection string as DATABASE_URL. Then run python manage.py migrate as a release/deploy step and create the first superuser using a secure one-time management process. Do not commit credentials or a production database URL.

## Public shipment tracking

The existing data/shipments.json file remains the temporary public tracking source for this foundation phase. Only approved public fields are rendered. Do not add customer phone numbers, email addresses, payment details or internal notes. Shipment records will move to the relational database in a later migration phase.

## Checks

    python manage.py check
    python manage.py makemigrations --check --dry-run
    python manage.py test

GitHub Actions runs these checks for pushes to main and feature/** branches and for pull requests targeting main.
