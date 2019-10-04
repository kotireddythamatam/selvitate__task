"""selvitate_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from filterapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('fileupload',views.file_upload),
    path('display',views.display),
    path('pricefilter<int:value>',views.price_filter),
    path('ratingfilter<int:value>',views.rating_filter),
    path('averageprice',views.average_price),
    path('averagerating',views.average_rating),
]
