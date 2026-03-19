# DevOps Nginx Reverse Proxy

Учебный проект, демонстрирующий публикацию контейнеризированного веб-приложения через Nginx reverse proxy с использованием Docker Compose и PostgreSQL.

## Описание

Проект состоит из трех сервисов:

* nginx — принимает входящие HTTP-запросы
* app — Flask-приложение
* db — PostgreSQL база данных

Пользователь взаимодействует только с Nginx. Приложение и база данных доступны только внутри docker-сети.

## Архитектура

```
Client -> Nginx -> Flask App -> PostgreSQL
```

## Стек технологий

* Nginx
* Python (Flask)
* PostgreSQL
* Docker
* Docker Compose

## Структура проекта

```
.
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── db/
│   └── init.sql
├── nginx/
│   └── default.conf
├── docker-compose.yml
├── .env.example
└── README.md
```

## Переменные окружения

Создайте файл `.env` на основе шаблона:

```
cp .env.example .env
```

Пример содержимого:

```
DB_HOST=db
DB_PORT=5432
DB_NAME=appdb
DB_USER=appuser
DB_PASSWORD=apppassword

POSTGRES_DB=appdb
POSTGRES_USER=appuser
POSTGRES_PASSWORD=apppassword
```

## Запуск проекта

Собрать и запустить:

```
docker compose up --build
```

Приложение будет доступно по адресу:

```
http://localhost:8080
```

## Проверка работы

Главная страница:

```
curl http://localhost:8080/
```

Проверка состояния:

```
curl http://localhost:8080/health
```

Получение данных:

```
curl http://localhost:8080/users
```

## Остановка

```
docker compose down
```

## Полная очистка

Удаляет контейнеры и данные базы:

```
docker compose down -v
```

## Полезные команды

Список контейнеров:

```
docker ps
```

Логи всех сервисов:

```
docker compose logs -f
```

Логи приложения:

```
docker compose logs -f app
```

Логи nginx:

```
docker compose logs -f nginx
```

Логи базы данных:

```
docker compose logs -f db
```

Пересборка:

```
docker compose down
docker compose up --build
```

## Особенности реализации

* наружу опубликован только nginx
* backend-сервис не имеет прямого доступа извне
* база данных не доступна извне
* взаимодействие сервисов происходит через docker-сеть
* nginx проксирует запросы на app
* запуск сервисов зависит от healthcheck

## Healthcheck

* PostgreSQL проверяется через pg_isready
* приложение проверяется через HTTP endpoint /health

## Возможные проблемы

Порт занят:

```
sudo lsof -i :8080
```

Смена порта:

```
ports:
  - "8081:80"
```

Проблемы с базой:

```
docker compose down -v
```

Проверка состояния контейнера:

```
docker inspect flask_app --format='{{json .State.Health}}'
```

## Что демонстрирует проект

* настройку reverse proxy
* изоляцию сервисов
* работу с docker-compose
* взаимодействие контейнеров
* использование переменных окружения
* базовую организацию инфраструктуры

## Автор

Ильшат Нуриев
https://github.com/IlshatNuriev
