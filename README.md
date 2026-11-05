# Hasoryx Transport Agency Limited

Django-based transport and logistics platform. The public marketing website and JSON-backed tracking page remain available while the operational platform is developed in phases.

## Technology
- Python 3.12 and Django 5.2
- Django built-in SQLite database for the current development phase
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

- The project currently uses Django's built-in SQLite backend and stores the development database at `db.sqlite3` in the project root.
- Database tables are created/updated with `python manage.py migrate`.
- Render startup also runs migrations before starting Gunicorn.
- Important: Render's default filesystem is ephemeral. SQLite data on a free Render service can be lost when the service restarts or redeploys. Use SQLite for development and early testing only. Before storing real customer, booking, payment, or shipment records in production, move to a persistent managed database such as PostgreSQL.
- Set `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=False`, `DJANGO_ALLOWED_HOSTS` and `DJANGO_CSRF_TRUSTED_ORIGINS` in the hosting environment.

## Public shipment tracking

The existing data/shipments.json file remains the temporary public tracking source for this foundation phase. Only approved public fields are rendered. Do not add customer phone numbers, email addresses, payment details or internal notes. Shipment records will move to the relational database in a later migration phase.

## Checks

    python manage.py check
    python manage.py makemigrations --check --dry-run
    python manage.py test

GitHub Actions runs these checks for pushes to main and feature/** branches and for pull requests targeting main.
