from django.contrib import admin
from django.urls import path
from .views import speak
from page.views import home

urlpatterns = [
path("", home, name="home"),
path("speak/", speak, name="speak"),
    path('admin/', admin.site.urls),
]
