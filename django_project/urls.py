from django.contrib import admin
from django.urls import path, include
from page.views import listen
from page.views import home

urlpatterns = [
path("bot/", include('voice_bot.urls')),
path("", home, name="home"),
path("speak/", listen, name="speak"),
    path('admin/', admin.site.urls),
]
