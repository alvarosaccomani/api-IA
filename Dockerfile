# Usa una imagen oficial de Python
FROM python:3.11-slim

# Evita buffers de Python que interfieren con logs en tiempo real
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . .

# Exponer puerto (Flask por defecto usa 5000, pero puedes usar 8000, etc.)
EXPOSE 5000

# Usar gunicorn para producción
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]