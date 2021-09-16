# Error Fixing:
If you get an error stating: 
```
"You are trying to add a non-nullable field '' to '' without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py" 
```
Please either:
1) Pull into new dir. 
2) Delete everything in 'migrations' folders except __init__.py 


# Enter Your Answer - Project: Thunder Cats

The official git repo for our group project

# Installation
1) Clone the repo
2) Create a conda env based off the requirements.txt file AND activate
3) Cd to to parent yieldPredictions and type "python runserver.py". 
4) Go to webaddress listed


# Quick Overview On Django:

admin.py registers database tables to the admin interface at /admin:
    - if you want a particular database table to be listed on /admin, you have to register it here
    - this is not very important, you do not have to add database tables to this file for it too work.

apps.py can be ignored - it just a file that registers this directory essentially

models.py contains all of the database tables:
    - Once you finish adding or changing any tables in this file go to the console and write:
        1) python manage.py makemigrations :: Register the changes with django (kinda like git add)
        2) python manage.py migrate :: Commit the changes to the database (like git commit)


serializers.py is how we translate information between json and whaterver format we store it as or vias versa:
    - For any request, we should have a 'get' version and a 'post version'

tests.py contains all of our unit tests (once we do them)

urls.py contains all our url routes, it points a url to a view:
    - path('GetUserModel/', UserModelView.as_view()) points the url .../GetUserModel/ to the view UserModelView

views.py is the main file which we use. It facilitates and uses most of the above files to interact with the frontend, including updating database tables, checking requests etc.










