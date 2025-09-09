import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","csi_erp.settings")
django.setup()
from django.contrib.auth import get_user_model

User = get_user_model()
username = os.getenv("DJANGO_SUPERUSER_USERNAME","admin")
email = os.getenv("DJANGO_SUPERUSER_EMAIL","admin@example.com")
password = os.getenv("DJANGO_SUPERUSER_PASSWORD","admin123")

u, created = User.objects.get_or_create(username=username, defaults={
    "email": email, "is_superuser": True, "is_staff": True, "role": "ADMIN"
})
u.is_superuser = True
u.is_staff = True
u.email = email
u.role = "ADMIN"
u.set_password(password)
u.save()
print(f"Admin user ready: {username} / (password set)")
