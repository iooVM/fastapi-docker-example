FROM python:3.9

WORKDIR /app

# Установите Poetry
RUN pip install poetry

# Копируем pyproject.toml и poetry.lock (если есть)
COPY pyproject.toml poetry.lock* ./

# Устанавливаем зависимости
RUN poetry install --no-dev

# Копируем код приложения
COPY ./app ./app

# Запускаем приложение
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
