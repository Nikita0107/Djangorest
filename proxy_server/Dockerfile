# Используем официальный образ Python
FROM python:3.12

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install django-extensions==3.2.3

# Копируем весь проект в контейнер
COPY . /app/

# Открываем порт 8002
EXPOSE 8002

# Запускаем Uvicorn сервер
CMD ["uvicorn", "proxy_server.asgi:application", "--host", "0.0.0.0", "--port", "8002", "--reload"]
