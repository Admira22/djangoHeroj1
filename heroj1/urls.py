from django.urls import path

from heroj1 import views

urlpatterns = [
    path("", views.index, name="index"),
]