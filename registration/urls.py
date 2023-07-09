from django.urls import URLPattern, path
from .views import *

urlpatterns = [
    path('', regform, name = 'registration form'),
]