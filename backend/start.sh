#!/usr/bin/env bash
set -e

# Rodar migrações
python manage.py migrate --noinput

# Garantir que o admin exista
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'Admin123')" || true

# Coletar estáticos (ok falhar silenciosamente se não houver nada novo)
python manage.py collectstatic --noinput || true

# Subir o servidor
python manage.py runserver 0.0.0.0:8000
