from django.urls import path

from heroj1 import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.pitanje, name="pitanje"),
    path("<int:question_id>/odgovori/", views.odgovori, name="odgovori"),
    path("<int:question_id>/odgovori/", views.ocjene, name="ocjene"),
    path("pitanja/",views.getListaPitanja,name="listaPitanja")
]