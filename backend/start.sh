#!/usr/bin/env bash
set -e

# Rodar migrações
python manage.py migrate --noinput

# Criar usuário admin se não existir (usa seu script existente)
python init_admin.py || true

# (Opcional) coletar estáticos se você adicionar depois
python manage.py collectstatic --noinput || true

# Subir o servidor
python manage.py runserver 0.0.0.0:8000
