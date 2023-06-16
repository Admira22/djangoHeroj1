from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import *
from django.core.validators import FileExtensionValidator

def validate_mp4(value):
    if not value.name.endswith('.mp4'):
        raise ValidationError("Unesite MP4 datoteku.")

class Obavjest(models.Model):
    pub_date = models.DateTimeField("date published")
    title = models.CharField(max_length=2000)
    description = models.CharField(max_length=2000)
    text = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='images/', max_length=255)
class Lekcija(models.Model):
    title = models.CharField(max_length=2000)
    subtitle1 = models.CharField(max_length=1000)
    part1 = models.CharField(max_length=2000)
    subtitle2 = models.CharField(max_length=2000)
    part2 = models.CharField(max_length=2000)
    subtitle3 = models.CharField(max_length=2000)
    part3 = models.CharField(max_length=2000)
    video = models.FileField(
        upload_to='videos/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4']), validate_mp4]
    )
    image = models.ImageField(upload_to='images/', max_length=255)

class Pitanje(models.Model):
    lekcijaID = models.ForeignKey(Lekcija, on_delete=models.CASCADE)
    tekst = models.CharField(max_length=2000)

class Odgovor(models.Model):
    pitanjeID = models.ForeignKey(Pitanje, on_delete=models.CASCADE)
    tekst = models.CharField(max_length=2000)

class Blog(models.Model):
    title = models.CharField(max_length=2000)
    subtitle1 = models.CharField(max_length=2000)
    part1 = models.CharField(max_length=3500)
    subtitle2 = models.CharField(max_length=2000)
    part2 = models.CharField(max_length=3500)
    subtitle3 = models.CharField(max_length=2000)
    part3 = models.CharField(max_length=3500)
    sadrzaj = models.CharField(max_length=3500)
    image = models.ImageField(upload_to='Blog/', max_length=255)

class UserProfile(models.Model):
    user_fk = models.OneToOneField(User,on_delete=models.CASCADE)
    STARIGRAD = "Stari grad"
    CENTAR = "Centar"
    NOVOSA = "Novo Sarajevo"
    NOVIGRAD = "Novi grad"
    ILIDZA = "Ilidža"
    LOKALNE_ZAJEDNICE = [
        (STARIGRAD, "Stari Grad"),
        (CENTAR, "Centar"),
        (NOVOSA, "Novo Sarajevo"),
        (NOVIGRAD, "Novi Grad"),
        (ILIDZA, "Ilidža"),
    ]
    IMADIJETE = 'Da'
    NEMADIJETE = 'Ne'
    DJECA = [
        (IMADIJETE, "Yes"),
        (NEMADIJETE, "No")
    ]
    firstName = models.CharField(max_length=2000,default='ime')
    lastName = models.CharField(max_length=2000,default='prezime')
    lc = models.CharField(
        max_length=2000,
        choices=LOKALNE_ZAJEDNICE,
        default=STARIGRAD)
    child = models.CharField(
        max_length=10,
        choices=DJECA,
        default=NEMADIJETE
    )
    progres = models.IntegerField(default=0)
    email = models.CharField(max_length=2000, default='email')
class FirstAid(models.Model):
    maintitle = models.CharField(max_length=2000)
    description = models.CharField(max_length=2000)
    title = models.CharField(max_length=2000)
    subtitle1 = models.CharField(max_length=1000)
    part1 = models.CharField(max_length=2000)
    subtitle2 = models.CharField(max_length=2000)
    part2 = models.CharField(max_length=2000)
    subtitle3 = models.CharField(max_length=2000)
    part3 = models.CharField(max_length=2000)
    subtitle4 = models.CharField(max_length=2000)
    part4 = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='images/', max_length=255)
class KvizRezultati(models.Model):
    user_id=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    brojTacnih=models.IntegerField(default=0)

