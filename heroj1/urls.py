from django.conf.urls.static import static
from django.urls import path

from djangoHeroj1 import settings
from heroj1 import views

urlpatterns = [
    path("", views.getLekcija, name="index"),
    path("<int:question_id>/", views.pitanje, name="pitanje"),
    path("<int:question_id>/odgovori/", views.odgovori, name="odgovori"),
    path("<int:question_id>/odgovori/", views.ocjene, name="ocjene"),
    path("pitanja/",views.getListaPitanja,name="listaPitanja"),
    path('lekcija/<int:lekcija_id>/', views.getLekcija, name='jednaLekcija'),
    path('obavjest/',views.getObavjest,name='obavjest'),
    path('blogovi/',views.getBlogovi, name='listaBlogova'),
    path('blogovi/<int:blog_id>',views.getBlog, name='blog')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)