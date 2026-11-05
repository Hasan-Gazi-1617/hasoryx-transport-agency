from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        SUPER_ADMIN = "super_admin", "Super Admin"
        OPERATIONS = "operations", "Operations"
        DISPATCH = "dispatch", "Dispatch"
        WAREHOUSE = "warehouse", "Warehouse"
        FINANCE = "finance", "Finance"
        SUPPORT = "support", "Customer Support"
        STAFF = "staff", "General Staff"

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=24, choices=Role.choices, default=Role.STAFF)

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.role = self.Role.SUPER_ADMIN
        super().save(*args, **kwargs)

    def __str__(self):
        return self.get_full_name() or self.username
