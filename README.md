# Django Boilerplate 🚀

<p align="center">
  <img src="https://static.djangoproject.com/img/logos/django-logo-positive.svg" alt="Django Logo" width="150"/>
</p>

<p align="center">
  A feature-rich Django boilerplate for starting new projects quickly.
</p>

<p align="center">
  <!-- Badges -->
  <img src="https://img.shields.io/badge/Python-3.12-blue.svg" alt="Python 3.12">
  <img src="https://img.shields.io/badge/Django-6.0-green.svg" alt="Django 6.0">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
</p>

---

## ✨ Features

-   📦 **Django 6.0**: The web framework for perfectionists with deadlines.
-   🐘 **PostgreSQL**: The world's most advanced open source relational database.
-   🔧 **REST Framework**: Powerful and flexible toolkit for building Web APIs.
-   🔐 **JWT Authentication**: Using `djangorestframework-simplejwt`.
-   🧑‍🤝‍🧑 **User Management**: With `djoser` and `django-allauth`.
-   🚀 **Celery**: For background tasks with Redis as a broker.
-   🐳 **Docker**: Fully containerized for development and production.
-   ⚙️ **Split Settings**: Separate settings for `dev` and `pro` environments.
-   ⚡ **HTMX**: For modern, dynamic front-ends without complex JavaScript.
-   🕵️ **Debugging & Profiling**: With `django-debug-toolbar` and `django-silk`.
-   🧹 **Code Quality**: Pre-configured with `ruff` for linting and formatting.

## 🏗️ Project Structure

```
.
├── core/                 # Core app for shared functionality
├── home/                 # Example app
├── users/                # User management app
├── mainProject/
│   ├── settings/
│   │   ├── common.py     # Common settings
│   │   ├── dev.py        # Development settings
│   │   └── pro.py        # Production settings
│   ├── urls.py
│   └── ...
├── manage.py
├── Docker/
│   └── docker-compose.yml # Docker services definition
├── Pipfile
├── Pipfile.lock
├── .env.example          # Example environment variables
└── README.md
```

## 🚀 Getting Started

### Prerequisites

-   Python 3.12+
-   Pipenv
-   Docker and Docker Compose

### 1. Clone the repository

```bash
git clone <repository-url>
cd Django-Boilerplate
```

### 2. Set up the environment

Create a `.env` file in the project root. You can copy the example:

```bash
cp .env.example .env
cp docker/.env.example docker/.env
```

Then, fill in the `.env` file with your database credentials, `DJANGO_KEY`, and other settings.

### 3. Install dependencies

```bash
pipenv install
pipenv install --dev
```

### 4. Start Docker services

Use the custom management command to start the PostgreSQL, Redis, and SMTP4Dev containers in the background:

```bash
pipenv run python manage.py startdockerservers
```

### 5. Run database migrations

```bash
pipenv run python manage.py migrate
```

### 6. Start the development server

```bash
pipenv run python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000`.

## Other Commands

You can run various services using Django's management commands.

-   **Start Redis:**

    ```bash
    pipenv run python manage.py start_redis
    ```

-   **Start SMTP4Dev:**

    ```bash
    pipenv run python manage.py start_smtp4dev
    ```

-   **Run Celery Worker:**

    ```bash
    pipenv run python manage.py start_celery_worker
    ```

-   **Run Celery Beat:**
    ```bash
    pipenv run python manage.py start_celery_beat
    ```

-   **Run Flower (Celery Monitoring):**

    ```bash
    pipenv run python manage.py start_celery_flower
    ```

    Flower will be available at `http://localhost:5555`.

-   **Run Locust:**
    ```bash
    pipenv run python manage.py start_locust
    ```
    Then, open your browser to `http://localhost:8089` to start the test.

## 🛠️ Technology Stack

-   **Backend**: Django, Django REST Framework
-   **Database**: PostgreSQL, Redis
-   **Async Tasks**: Celery
-   **Containerization**: Docker
-   **Frontend**: Django Templates, HTMX
-   **Authentication**: `django-allauth`, `djoser`, `rest_framework_simplejwt`
-   **Development**: `django-debug-toolbar`, `django-silk`

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
