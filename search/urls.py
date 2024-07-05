# newapp/urls.py
from django.urls import path
from .views import search_view_minecode

urlpatterns = [
    path('minecode/', search_view_minecode, name='search_view_minecode'),
    # path('minecode/', search_view_minecode.as_view(), name='search_view_minecode'),
]
