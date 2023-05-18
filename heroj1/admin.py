from django.contrib import admin


from heroj1.models import Obavjest
from heroj1.models import Korisnik
from heroj1.models import KorisnikProgres
from heroj1.models import Lekcija
from heroj1.models import Pitanje
from heroj1.models import Odgovor
from heroj1.models import Blog
from heroj1.models import UserProfile

# Register your models here.
admin.site.register(Obavjest)
admin.site.register(Korisnik)
admin.site.register(KorisnikProgres)
admin.site.register(Lekcija)
admin.site.register(Pitanje)
admin.site.register(Odgovor)
admin.site.register(Blog)
admin.site.register(UserProfile)