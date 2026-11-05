from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from accounts import views as account_views
from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("staff/", account_views.dashboard, name="staff-dashboard"),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("fleet/", views.fleet, name="fleet"),
    path("track/", views.track, name="track"),
    path("contact/", views.contact, name="contact"),
]
