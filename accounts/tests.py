from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


User = get_user_model()


class StaffAccessTests(TestCase):
    def setUp(self):
        self.staff = User.objects.create_user(
            username="operations1", email="ops@example.com", password="Strong-test-pass-123",
            is_staff=True, role=User.Role.OPERATIONS,
        )
        self.customer = User.objects.create_user(
            username="customer1", email="customer@example.com", password="Strong-test-pass-123",
        )

    def test_dashboard_redirects_anonymous_user_to_login(self):
        response = self.client.get(reverse("staff-dashboard"))
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('staff-dashboard')}")

    def test_staff_can_access_dashboard(self):
        self.client.force_login(self.staff)
        response = self.client.get(reverse("staff-dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Staff dashboard")

    def test_non_staff_user_cannot_access_dashboard(self):
        self.client.force_login(self.customer)
        response = self.client.get(reverse("staff-dashboard"))
        self.assertEqual(response.status_code, 403)

    def test_superuser_is_assigned_super_admin_role(self):
        admin = User.objects.create_superuser("root", "root@example.com", "Strong-test-pass-123")
        self.assertEqual(admin.role, User.Role.SUPER_ADMIN)
