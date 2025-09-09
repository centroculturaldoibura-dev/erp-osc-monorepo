FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Copia e dá permissão de execução ao start.sh
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Comando padrão para rodar o servidor
CMD ["/start.sh"]
