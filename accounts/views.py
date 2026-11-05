from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render


def staff_member_required(view_func):
    return user_passes_test(lambda user: user.is_authenticated and user.is_staff, login_url="login")(view_func)


@login_required
@staff_member_required
def dashboard(request):
    return render(request, "accounts/dashboard.html")
