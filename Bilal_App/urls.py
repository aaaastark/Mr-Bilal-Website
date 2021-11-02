from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views

app_name = 'bilalapp'

urlpatterns = [
    path('',views.index_view,name='index_view'),
]