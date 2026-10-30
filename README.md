# Hasoryx Transport Agency Limited

A Django-powered, database-free transport and logistics website with JSON-based public shipment tracking.

## Stack
- Python and Django
- Django signed-cookie sessions (no database required)
- JSON file for shipment tracking data
- WhiteNoise for static files
- Render deployment

## Local setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

Open http://127.0.0.1:8000/.

## Tracking data
Edit `data/shipments.json` and commit the change to GitHub. The public tracking page only exposes shipment status, route, service, and timeline. Do not put customer phone numbers, email addresses, or other private information in this file.

## Render
Use the included `render.yaml`, or set the build command to `./build.sh` and the start command to `gunicorn config.wsgi:application`. Set `DJANGO_SECRET_KEY` to a long random secret and `DJANGO_DEBUG=False`.

This project intentionally does not use PostgreSQL or Django ORM models. Render's ephemeral filesystem is not used for tracking records.