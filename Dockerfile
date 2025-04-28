# Dockerfile
FROM python:3.12-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos de dependencias
COPY pyproject.toml poetry.lock /app/

# Instalar Poetry
RUN pip install poetry

# Instalar dependencias
RUN poetry config virtualenvs.create false \
    && poetry install --only main --no-root


# Copiar todo el proyecto
COPY . /app/

# Exponer el puerto (Django por defecto usa 8000)
EXPOSE 8000

# Comando por defecto para arrancar el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
