

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
"""
Django Views and URL Concepts(day 16)

1. What is the request object that every view receives?
-------------------------------------------------------
The request object is an HttpRequest object that contains information about
the incoming HTTP request sent by the user.

Every Django view receives it as the first parameter:

Example:
def home(request):
    ...

Common request attributes:
1. request.method
   - Returns the HTTP method used (GET, POST, etc.).

2. request.GET
   - Contains data sent through URL query parameters.

3. request.POST
   - Contains data submitted through HTML forms using POST.

4. request.user
   - Contains information about the currently logged-in user.

Other attributes include:
- request.path
- request.FILES
- request.session


2. Difference between HttpResponse and render()
------------------------------------------------
HttpResponse:
- Directly returns an HTTP response with content.
- Used when you want to return simple text or HTML directly.

Example:
return HttpResponse("<h1>Hello</h1>")


render():
- Used to return an HTML template with dynamic data.
- Combines a template file with context data and returns an HttpResponse.

Example:
return render(request, "home.html", {"name": "John"})

Use:
- HttpResponse for simple responses.
- render() for complete web pages using templates.


3. What does include() do in urls.py?
-------------------------------------
The include() function allows Django to include URL patterns from another
URL configuration file.

Example:

path('', include('blog.urls'))

It connects the main project's URLs with an app's URLs.

Why use include()?
- Keeps URLs organized.
- Allows each app to manage its own URLs.
- Makes projects easier to maintain.
- Avoids putting hundreds of URL patterns in one file.


4. What is a URL parameter?
---------------------------
A URL parameter is a value passed through the URL that a view can use.

Example:

URL:
http://127.0.0.1:8000/posts/5/

Here, 5 is the URL parameter.

Define it in urls.py:

path('posts/<int:post_id>/', views.posts)

The value is passed to the view:

def posts(request, post_id):
    return HttpResponse(f"Post number {post_id}")

Django supports different parameter types:
- <int:id>       - Integer values
- <str:name>     - String values
- <slug:slug>    - Slug values
- <uuid:id>      - UUID values
"""
<img width="1599" height="809" alt="image" src="https://github.com/user-attachments/assets/ade3e07f-dd2a-4fb5-b55a-1791c6dd5948" />
<img width="1600" height="800" alt="image" src="https://github.com/user-attachments/assets/f9f68cd6-9bd4-44c8-995e-ec64b7b36914" />
<img width="1594" height="818" alt="image" src="https://github.com/user-attachments/assets/f64defef-6577-4415-95ff-20422915049d" />
<img width="1600" height="817" alt="image" src="https://github.com/user-attachments/assets/fde1268e-bc9a-4859-adc7-f54a6cb1af34" />
<img width="1600" height="822" alt="image" src="https://github.com/user-attachments/assets/164f487e-5516-4f1f-899a-e3fa3ed9447b" />
# Django Blog Project day 18 - Evaluation Answers and Commands


========================
EVALUATION QUESTIONS
========================


1. What is an ORM? What problem does it solve compared to writing raw SQL?

ORM (Object-Relational Mapping) allows developers to interact with the database
using Python objects instead of writing SQL queries manually.

Django ORM converts Python code into SQL queries automatically.

Example:
    Post.objects.all()

Advantages:
- No need to write SQL manually.
- Easier database management.
- Reduces SQL errors.
- Code becomes cleaner and easier to maintain.


========================


2. Difference between makemigrations and migrate

makemigrations:
- Creates migration files based on changes in models.py.
- Prepares database changes.

Command:
    python manage.py makemigrations


migrate:
- Applies migration files to the database.
- Creates or updates database tables.

Command:
    python manage.py migrate


If makemigrations is skipped:
- Django will not create migration files.
- Database will not know about model changes.


If migrate is skipped:
- Migration files exist, but database tables are not updated.


========================


3. What is a ForeignKey? What is on_delete?

ForeignKey creates a relationship between two models.

Example:

    category = models.ForeignKey(Category, on_delete=models.CASCADE)


It represents a many-to-one relationship:

- One Category can have many Posts.
- Each Post belongs to one Category.


on_delete defines what happens when the related object is deleted.


Example:

    models.CASCADE

If a Category is deleted:
- All related Posts are deleted.


Other options:

    models.PROTECT

Prevents deletion if related posts exist.


    models.SET_NULL

Sets the ForeignKey value to NULL.


========================


4. Difference between all(), filter(), and get()


Post.objects.all()

Returns all posts from the database.

Example:

    Post.objects.all()


--------------------------------


Post.objects.filter()

Returns multiple objects matching a condition.

Example:

    Post.objects.filter(published=True)


If no object matches:
Returns an empty QuerySet.


--------------------------------


Post.objects.get()

Returns exactly one object.

Example:

    Post.objects.get(id=1)


get() raises errors:


1. DoesNotExist

When no object is found.

Example:

    Post.objects.get(id=999)


2. MultipleObjectsReturned

When more than one object matches.


Example:

    Post.objects.get(published=True)



========================
COMMANDS USED
========================


Create virtual environment:

    python -m venv venv


Activate virtual environment:

    venv\Scripts\activate


Install Django:

    pip install django


Create app:

    python manage.py startapp django_blog


Create migrations:

    python manage.py makemigrations


Apply migrations:

    python manage.py migrate


Run server:

    python manage.py runserver



========================
DATABASE VERIFICATION
========================


Open shell:

    python manage.py shell


Check database tables:

    from django.db import connection

    connection.introspection.table_names()


Exit shell:

    exit()



========================
DJANGO SHELL OPERATIONS
========================


Import models:

    from django_blog.models import Category, Post
    from django.contrib.auth.models import User


Create user:

    user = User.objects.create_user(
        username="admin",
        password="12345"
    )


Create categories:

    c1 = Category.objects.create(
        name="Technology",
        slug="technology",
        description="Tech articles"
    )


    c2 = Category.objects.create(
        name="Sports",
        slug="sports",
        description="Sports articles"
    )


    c3 = Category.objects.create(
        name="Education",
        slug="education",
        description="Education articles"
    )


Create posts:

    Post.objects.create(
        title="Python Basics",
        slug="python-basics",
        body="Python is easy to learn",
        author=user,
        category=c1,
        published=True
    )


Filter published posts:

    Post.objects.filter(published=True)


Get single post:

    Post.objects.get(id=1)


Update post:

    post = Post.objects.get(id=1)

    post.title = "Updated Title"

    post.save()


Delete post:

    post = Post.objects.get(id=5)

    post.delete()


Count posts per category:

    from django.db.models import Count

    Category.objects.annotate(
        total_posts=Count('post')
    )


Search by keyword:

    Post.objects.filter(
        body__icontains="python"
    )



========================
TEMPLATE SETUP
========================


Created template:

    templates/home.html


Updated settings.py:

    'DIRS': [BASE_DIR / 'templates']


Updated view:

    posts = Post.objects.filter(published=True)

    return render(
        request,
        "home.html",
        {"posts": posts}
    )


"""
<img width="1587" height="769" alt="image" src="https://github.com/user-attachments/assets/6a6af17a-1d00-4d85-85f1-a880655d23b7" />
<img width="1579" height="859" alt="image" src="https://github.com/user-attachments/assets/03a703d1-b398-4b6b-8957-015f794cce4b" />
<img width="1547" height="859" alt="image" src="https://github.com/user-attachments/assets/6315ce6e-bd08-4f05-9efa-0e41cfa85c94" />
<img width="1585" height="858" alt="image" src="https://github.com/user-attachments/assets/7fa06791-44e5-44d1-91ad-8746704f1b70" />






"""
DAY 19  evaluation question answer

Q1. What is the Django admin panel? Who is it for — developers or end users? Explain why.

Answer:
The Django admin panel is a built-in interface that allows authorized users to manage
database records through a web browser. It is primarily intended for developers,
site administrators, and content managers—not for general end users. It provides
tools to create, update, delete, and search data without writing SQL or building
custom management pages.

Q2. What is list_editable? What security consideration should you keep in mind when using it?

Answer:
list_editable is a ModelAdmin option that allows specified fields to be edited
directly from the admin change list page without opening each object individually.
It should only be used for fields that trusted admin users are allowed to modify,
because users with change permission can update those values quickly in bulk.
Avoid making sensitive fields directly editable unless necessary.

Q3. What is prepopulated_fields? What does it do in practice and what model field does it typically target?

Answer:
prepopulated_fields automatically fills one field based on the value of another
field while typing in the admin form. It is commonly used to generate a slug from
the title of a model. For example:
prepopulated_fields = {"slug": ("title",)}
This automatically creates a URL-friendly slug as the title is entered.

Q4. How do you create a custom admin action? What are the required components?

Answer:
A custom admin action is created by:
1. Defining a function that accepts three parameters:
   - modeladmin
   - request
   - queryset
2. Decorating it with @admin.action(description="Action Name") (optional but recommended).
3. Adding the function to the ModelAdmin using the actions list.

Example:
@admin.action(description="Mark selected posts as published")
def mark_selected_posts_as_published(modeladmin, request, queryset):
    queryset.update(published=True)

class PostAdmin(admin.ModelAdmin):
    actions = [mark_selected_posts_as_published]
"""
<img width="1586" height="557" alt="image" src="https://github.com/user-attachments/assets/48d16e12-0005-4cc2-a710-fe2271f84ec7" />
<img width="1600" height="611" alt="image" src="https://github.com/user-attachments/assets/4757e80b-369e-4e5a-acd3-0b2ad46d2fde" />
<img width="1600" height="652" alt="image" src="https://github.com/user-attachments/assets/059f4a53-c739-4487-9d97-daa06971cade" />
<img width="1600" height="682" alt="image" src="https://github.com/user-attachments/assets/e79f4f2c-290f-4482-9d30-21d9967a74e5" />
<img width="1599" height="514" alt="image" src="https://github.com/user-attachments/assets/fcfdf594-6dcc-4fe8-b088-d0ea988018cf" />







