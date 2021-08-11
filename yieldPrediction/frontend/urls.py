from django.urls import path, re_path
from .views import index

"""
Anytime you add a new route to React, you need to add it also to the url 
patterns e.g. #path('home', index). Where 'home', is the name of the url, 
and index is the name of the function contained in views.py
"""
urlpatterns = [
    path('', index),
    # catch all pages, but denies 404 errors.
    #re_path(r'.*', index),
]
