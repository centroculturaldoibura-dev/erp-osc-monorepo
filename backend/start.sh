#!/usr/bin/env bash
set -e

# Rodar migrações
python manage.py migrate --noinput

# Coletar estáticos (ok falhar silenciosamente se não houver nada novo)
python manage.py collectstatic --noinput || true

# Subir o servidor
python manage.py runserver 0.0.0.0:8000
