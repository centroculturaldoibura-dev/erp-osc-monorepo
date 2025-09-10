#!/usr/bin/env bash

# Rodar migrações
python manage.py migrate --noinput

# Criar usuário admin se não existir
python csi_erp/init_admin.py || true

# (Opcional) coletar estáticos
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'Admin123')"


# Subir o servidor
python manage.py runserver 0.0.0.0:8000

