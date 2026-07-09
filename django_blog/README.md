

1. Difference Between a Django Project and a Django App
-------------------------------------------------------
- A Django Project is the complete web application. It contains the project's
  settings, URL configuration, and one or more Django apps.
- A Django App is a reusable module that provides a specific feature or
  functionality, such as authentication, blog management, or payments.
- A single Django project can contain multiple apps.

2. Purpose of manage.py
-----------------------
The manage.py file is a command-line utility used to manage and interact with
a Django project.

Common manage.py commands:
1. python manage.py runserver
   - Starts the development server.

2. python manage.py makemigrations
   - Creates migration files based on model changes.

3. python manage.py migrate
   - Applies database migrations.

4. python manage.py createsuperuser
   - Creates an administrator account.

5. python manage.py startapp <app_name>
   - Creates a new Django application.

3. Purpose of settings.py
-------------------------
The settings.py file stores the project's configuration, including:
- Database settings
- Installed applications
- Middleware
- Templates
- Static and media file settings
- Security settings
- Time zone and language
- Secret key

If DEBUG = False during development:
- Detailed error pages are disabled.
- Generic error pages are displayed instead.
- ALLOWED_HOSTS must be configured.
- Static files are not served automatically by Django's development server.
- Debugging becomes more difficult.

4. Purpose of the admin/ URL
----------------------------
The /admin/ URL provides access to Django's built-in administration interface.
It allows authorized users to:
- Add, edit, and delete database records.
- Manage registered models.
- Manage users and permissions.

To access the admin site:
1. Create a superuser:
   python manage.py createsuperuser

2. Start the development server:
   python manage.py runserver

3. Open a browser and visit:
   http://127.0.0.1:8000/admin/

4. Log in using the superuser credentials.


   <img width="1596" height="860" alt="image" src="https://github.com/user-attachments/assets/2ee00930-37e0-455e-a17c-c28bb0db55be" />

"""
