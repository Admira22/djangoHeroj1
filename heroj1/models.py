from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return str(self.id) + " " + self.question_text + "#"


class Answers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=20)
    votes = models.IntegerField(default=0)

class NewCK(models.Model):
    pub_date = models.DateTimeField("date published")
    title = models.CharField(max_length=2000)
    description = models.CharField(max_length=2000)
    text = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='images/', max_length=255)

class Korisnik(models.Model):
    STARIGRAD = "SG"
    CENTAR = "CR"
    NOVOSA = "NS"
    NOVIGRAD = "NG"
    ILIDZA = "IL"
    LOKALNE_ZAJEDNICE = [
        (STARIGRAD , "Stari Grad"),
        (CENTAR, "Centar"),
        (NOVOSA, "Novo Sarajevo"),
        (NOVIGRAD, "Novi Grad"),
        (ILIDZA, "Ilidža"),
    ]
    IMADIJETE = 'Ima'
    NEMADIJETE = 'Nema'
    DJECA = [
        (IMADIJETE, "Da"),
        (NEMADIJETE, "Ne" )
    ]
    firstName = models.CharField(max_length=2000)
    lastName = models.CharField(max_length=2000)
    email = models.CharField(max_length=2000)
    password = models.CharField(max_length=2000)
    lc = models.CharField(
        max_length=10,
        choices=LOKALNE_ZAJEDNICE,
        default=STARIGRAD)
    child = models.CharField(
        max_length=10,
        choices=DJECA,
        default=NEMADIJETE
    )

class KorisnikProgres(models.Model):
    korisnikID = models.ForeignKey(Korisnik, on_delete=models.CASCADE)
    progres = models.IntegerField(default=0)


class Lekcija(models.Model):
    title = models.CharField(max_length=2000)
    subtitle1 = models.CharField(max_length=1000)
    part1 = models.CharField(max_length=2000)
    subtitle2 = models.CharField(max_length=2000)
    part2 = models.CharField(max_length=2000)
    subtitle3 = models.CharField(max_length=2000)
    part3 = models.CharField(max_length=2000)
    video = models.CharField(max_length=2000)


class Pitanje(models.Model):
    lekcijaID = models.ForeignKey(Lekcija, on_delete=models.CASCADE)
    tekst = models.CharField(max_length=2000)

class Odgovor(models.Model):
    pitanjeID = models.ForeignKey(Pitanje, on_delete=models.CASCADE)
    tekst = models.CharField(max_length=2000)

class Blog(models.Model):
    title = models.CharField(max_length=2000)
    subtitle1 = models.CharField(max_length=2000)
    part1 = models.CharField(max_length=2000)
    subtitle2 = models.CharField(max_length=2000)
    part2 = models.CharField(max_length=2000)
    subtitle3 = models.CharField(max_length=2000)
    part3 = models.CharField(max_length=2000)
    video = models.CharField(max_length=2000)


