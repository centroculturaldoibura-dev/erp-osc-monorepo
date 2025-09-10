#!/usr/bin/env bash

# Rodar migrações
python manage.py migrate --noinput

# Criar usuário admin se não existir
python csi_erp/init_admin.py || true

# (Opcional) coletar estáticos
python manage.py collectstatic --noinput || true

# Subir o servidor
python manage.py runserver 0.0.0.0:8000

