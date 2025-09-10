#!/usr/bin/env bash
set -e

# Ir para a pasta do backend (onde está o manage.py)
cd /app/backend

# Migrações
python manage.py migrate --noinput

# (Re)criar/atualizar o superusuário admin com a senha desejada
python manage.py shell - <<'PY'
from django.contrib.auth import get_user_model
User = get_user_model()
u, created = User.objects.update_or_create(
    username="admin",
    defaults={"is_staff": True, "is_superuser": True},
)
u.set_password("Admin123!")
u.save()
print("ADMIN_OK", "created" if created else "updated")
PY

# Coletar estáticos (não falhar se não houver)
python manage.py collectstatic --noinput || true

# Subir o servidor
python manage.py runserver 0.0.0.0:8000
