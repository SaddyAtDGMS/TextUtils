"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
# from search import views

# from search import views

urlpatterns = [
    # path("aentry/", include("aentry.urls")),
    
    
    path('',views.index, name= 'index'), 
    path("aentry/", include("aentry.urls")),
    path('admin/', admin.site.urls),  
    path('analyze',views.analyze, name= 'analyze'), 
    path('temp1',views.temp1, name= 'temp1'),
    path('contact_us',views.contact_us, name= 'contact_us'),

    path('search/', include('search.urls')),
    path('minecode-redirect/', views.search_minecode_view, name='search_minecode_view'),
    # path('search/minecode/', views.search_minecode, name='search_minecode'),
    # path('search/minecode/', search/views.search_view, name='search_minecode'),
    # path('search/minecode/', views.search_minecode_view, name='search_minecode_view' ),
]
