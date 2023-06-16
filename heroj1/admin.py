from django.contrib import admin


from heroj1.models import Obavjest
from heroj1.models import Lekcija
from heroj1.models import Pitanje
from heroj1.models import Odgovor
from heroj1.models import Blog
from heroj1.models import UserProfile
from heroj1.models import FirstAid
from heroj1.models import KvizRezultati

# Register your models here.
admin.site.register(Obavjest)
admin.site.register(Lekcija)
admin.site.register(Pitanje)
admin.site.register(Odgovor)
admin.site.register(Blog)
admin.site.register(UserProfile)
admin.site.register(FirstAid)
admin.site.register(KvizRezultati)