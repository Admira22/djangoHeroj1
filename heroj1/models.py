from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return str(self.id) + " " + self.question_text + "#"


class Answers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class NewCK(models.Model):
    pub_date = models.DateTimeField("date published")
    title = models.CharField(max_length=2000)
    description = models.CharField(max_length=2000)
    text = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='images/', max_length=255)


class News(models.Model):
    pub_date = models.DateTimeField("date publiched")
    title = models.CharField(max_length=2000)
    description = models.CharField(max_length=2000)
    text = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='images/', height_field='height', width_field='width', max_length=255)
