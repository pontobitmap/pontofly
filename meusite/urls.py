from django.urls import path

from .views import index

app_name = "meusite"

urlpatterns = [
    path("", index, name="index"),
]
