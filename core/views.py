import json
from pathlib import Path
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.http import require_GET

DATA_FILE = Path(settings.BASE_DIR) / 'data' / 'shipments.json'

def _shipments():
    try:
        with DATA_FILE.open(encoding='utf-8') as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except (OSError, json.JSONDecodeError):
        return []

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def services(request):
    return render(request, 'core/services.html')

def fleet(request):
    return render(request, 'core/fleet.html')

@require_GET
def track(request):
    tracking_id = request.GET.get('id', '').strip().upper()
    shipment = None
    searched = bool(tracking_id)
    if tracking_id:
        for item in _shipments():
            if str(item.get('tracking_id', '')).strip().upper() == tracking_id:
                # Whitelist public fields. Never expose customer contact or internal notes.
                shipment = {key: item.get(key) for key in ('tracking_id', 'service', 'origin', 'destination', 'status', 'last_updated', 'history')}
                break
    return render(request, 'core/track.html', {'tracking_id': tracking_id, 'shipment': shipment, 'searched': searched})

def contact(request):
    return render(request, 'core/contact.html')
