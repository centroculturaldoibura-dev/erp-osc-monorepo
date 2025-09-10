#!/usr/bin/env bash
set -e

# Rodar migrações
python manage.py migrate --noinput

# Criar usuário admin se não existir
python manage.py shell -c "
from django.contrib.auth import get_user_model;
User = get_user_model();
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'Admin123')
"

# (Opcional) coletar estáticos
python manage.py collectstatic --noinput || true

# Subir o servidor
python manage.py runserver 0.0.0.0:8000

