# Imagen base de Python
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Exponer el puerto 80 (Flask modificado para usar este puerto)
EXPOSE 80

# Comando para ejecutar la app
CMD ["python", "app.py"]
