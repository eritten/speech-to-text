from django.contrib import admin
from django.urls import path
from page.views import listen
from page.views import home

urlpatterns = [
path("", home, name="home"),
path("speak/", listen, name="speak"),
    path('admin/', admin.site.urls),
]
