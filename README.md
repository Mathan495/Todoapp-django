# Todo App

## Overview
This is a simple yet powerful todo application built using Django. The application allows users to manage their tasks efficiently and helps in improving productivity.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Mathan495/Todoapp-django.git
   cd Todoapp-django
   ```
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the migrations:
   ```bash
   python manage.py migrate
   ```
2. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```
3. Run the development server:
   ```bash
   python manage.py runserver
   ```
4. Access the application at `http://127.0.0.1:8000/`

## Features
- User authentication (login, logout, registration)
- Create, read, update, and delete todos
- Mark todos as completed or pending
- User-friendly interface
- Responsive design

## Project Structure
```
Todoapp-django/
├── manage.py
├── todo/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── todoapp/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
└── README.md
```

## Requirements
- Python 3.x
- Django 3.x or later

## Contribution Guidelines
1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Make your changes and push to the branch:
   ```bash
   git push origin feature/your-feature
   ```
4. Open a pull request to the main branch with a clear description of your changes.

Happy Coding!