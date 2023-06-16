from django.conf.urls.static import static
from django.urls import path

from djangoHeroj1 import settings
from heroj1 import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from heroj1.views import MyTokenObtainPairView, search

urlpatterns = [
    path("", views.getRoutes, name="index"),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/register/', views.register, name='register'),
    path('lekcija/<int:lekcija_id>/', views.getLekcija, name='jednaLekcija'),
    path('lekcije/',views.getLekcije, name='sveLekcije'),
    path('pitanja/<int:lekcijaID>/',views.getPitanja, name='pitanjaJedneLekcije'),
    path('obavjest/',views.getObavjest,name='obavjest'),
    path('blogovi/',views.getBlogovi, name='listaBlogova'),
    path('blogovi/<int:blog_id>',views.getBlog, name='blog'),
    path('profile/', views.getProfile,name='profile'),
    path('odgovor/<int:pitanjeID>',views.getOdgovor,name="odgovorNaPitanje"),
    path('bolest/<int:firstaid_id>/',views.getBolest,name="jednaBolest"),
    path('pretraga/<int:firstaid_id>/',views.getBolest,name='jednaBolestReg'),
    path('odgovori/',views.getListaOdgovora,name="odgovori"),
    path('pitanja/',views.getLPitanja,name="pitanja"),
    path('rezultati/',views.getKvizRezultate,name="rezultati"),
    path('posaljiRezultate/',views.posaljiRezultate,name="poslani"),
    path('progres/',views.setProgres,name='progres'),
    path('search/',search.as_view(),name='progres'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)