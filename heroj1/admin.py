from django.contrib import admin

from heroj1.models import Question
from heroj1.models import Answers

# Register your models here.
admin.site.register(Question)
admin.site.register(Answers)