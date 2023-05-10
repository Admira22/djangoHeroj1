from django.core import serializers
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from heroj1.models import Question, Obavjest, Lekcija


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


@api_view(['GET'])
def getLekcija(request,lekcija_id):
    lesson = Lekcija.objects.get(pk=lekcija_id)
    res = serializers.serialize('json',[lesson,])

    data=[]
    for lesson1 in serializers.deserialize('json',res):
        fields = lesson1.object
        data.append({
            'id': fields.pk,
            'title': fields.title,
            'subtitle1': fields.subtitle1,
            'part1': fields.part1,
            'subtitle2': fields.subtitle2,
            'part2': fields.part2,
            'subtitle3': fields.subtitle3,
            'part3': fields.part3,
            'video': fields.video,
            'image': request.build_absolute_uri(fields.image.url) if fields.image else None,

        })
    return JsonResponse(data,safe=False)

api_view(['GET'])
def getObavjest(request):
    list_of_obavjesti = Obavjest.objects.all()
    res = serializers.serialize('json',list_of_obavjesti)

    data = []
    for obavjest in serializers.deserialize('json',res):
        fields = obavjest.object
        data.append({
            'id': fields.pk,
            'pub_date': fields.pub_date,
            'title': fields.title,
            'description': fields.description,
            'text': fields.text,
            'image': request.build_absolute_uri(fields.image.url) if fields.image else None,
        })
    return JsonResponse(data,safe=False)

# def getNajnovijaObavjest(request):
#     info = Obavjest.objects.all()
#     res = serializers.serialize('json',info)
#
#     data = []
#     for info1 in serializers.deserialize('json',res):
#         fields = info1.object
#         data.append({
#             'id': fields.pk,
#             'pub_date': fields.pub_date,
#             'title': fields.title,
#             'description': fields.description,
#             'text': fields.text,
#             'image': request.build_absolute_uri(fields.image.url) if fields.image else None,
#         })
#     return JsonResponse(data,safe=False)

@api_view(['GET'])
def getListaPitanja(request):
    list_of_questions = Question.objects.all()
    res = serializers.serialize('json', list_of_questions)

    data = []
    for question in serializers.deserialize('json', res):
        fields = question.object
        data.append({
            'id': fields.pk,
            'questionText': fields.question_text,
            'pubDate': fields.pub_date
        })

    return JsonResponse(data, safe=False)

