from django.contrib.auth import get_user_model
from django.db.utils import OperationalError

User = get_user_model()

try:
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="Admin123"
        )
        print("Superusuário 'admin' criado com sucesso.")
    else:
        print("Superusuário 'admin' já existe.")
except OperationalError as e:
    print("Banco de dados não está pronto ainda:", e)
