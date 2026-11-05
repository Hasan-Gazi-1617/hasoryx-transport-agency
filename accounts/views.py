from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render


@login_required
def dashboard(request):
    if not request.user.is_staff:
        raise PermissionDenied("Staff access is required.")
    return render(request, "accounts/dashboard.html")
