import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "csi_erp.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

USERNAME = "admin"
PASSWORD = "Admin123!"
EMAIL = "admin@example.com"

def ensure_admin():
    user, created = User.objects.get_or_create(
        username=USERNAME,
        defaults={
            "email": EMAIL,
            "is_staff": True,
            "is_superuser": True,
            "is_active": True,
        },
    )
    # sempre garante permissões e senha
    user.is_staff = True
    user.is_superuser = True
    user.is_active = True
    user.set_password(PASSWORD)
    user.save()
    print("Superuser criado/atualizado:", user.username)

if __name__ == "__main__":
    ensure_admin()

