from django.core import serializers
from django.http import HttpResponse, Http404
from django.shortcuts import render
from rest_framework.decorators import api_view

from heroj1.models import Question


def index(request):
    list_of_question = Question.objects.all()
    question_string = ""
    for question in list_of_question:
        question_string += " " + question.__str__()

    return HttpResponse(question_string)
def pitanje(request, question_id):
    try:
     question = Question.objects.get(pk=question_id)
     return HttpResponse(question.__str__())
    except Question.DoesNotExist:
        return Http404("Pitanje ne postoji" + str(question_id))

def odgovori(request, question_id):
    return HttpResponse("Odgovori na pitanje" + str(question_id))

def ocjene(request, question_id):
    return HttpResponse("Ocjene za pitanje" + str(question_id))

@api_view(['GET'])
def getListaPitanja(request):
    list_of_question = Question.objects.all()
    res = serializers.serialize('json',list_of_question)
    return HttpResponse(res,content_type="text/json-comment-filtered")