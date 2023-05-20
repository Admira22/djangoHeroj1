from django.core import serializers
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from heroj1.models import Question, Obavjest, Lekcija, Blog, Pitanje, UserProfile,Odgovor
from .serializers import ProfileSerializer


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

@api_view(['GET'])
def getLekcije(request):
    lesson = Lekcija.objects.all()
    res = serializers.serialize('json',lesson)

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

@api_view(['GET'])
def getBlogovi(request):
     lista_blogova = Blog.objects.all()
     rezultat = serializers.serialize('json',lista_blogova)

     data = []
     for blog in serializers.deserialize('json',rezultat):
         fields = blog.object
         data.append({
             'id': fields.pk,
             'title': fields.title,
             'subtitle1': fields.subtitle1,
             'part1': fields.part1,
             'subtitle2': fields.subtitle2,
             'part2': fields.part2,
             'subtitle3': fields.subtitle3,
             'part3': fields.part3,
             'sadrzaj': fields.sadrzaj,
             'image': request.build_absolute_uri(fields.image.url) if fields.image else None,
         })
     return JsonResponse(data,safe=False)
@api_view(['GET'])
def getBlog(request,blog_id):
    blog = Blog.objects.get(pk=blog_id)
    rezultat = serializers.serialize('json', [blog, ])

    data = []
    for blog1 in serializers.deserialize('json', rezultat):
         fields = blog1.object
         data.append({
             'id': fields.pk,
             'title': fields.title,
             'subtitle1': fields.subtitle1,
             'part1': fields.part1,
             'subtitle2': fields.subtitle2,
             'part2': fields.part2,
             'subtitle3': fields.subtitle3,
             'part3': fields.part3,
             'sadrzaj': fields.sadrzaj,
             'image': request.build_absolute_uri(fields.image.url) if fields.image else None,
         })
    return JsonResponse(data, safe=False)

@api_view(['GET'])
def getPitanja(request, lekcijaID):
    questions = Pitanje.objects.filter(lekcijaID_id=lekcijaID)
    data = [{'id': q.pk, 'tekst': q.tekst} for q in questions]
    return JsonResponse(data, safe=False)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh'
    ]

    return Response(routes)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfile(request):
    user = request.user
    profile = user.userprofile  # Assuming a one-to-one relationship between User and UserProfile
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)
@api_view(['GET'])
def getOdgovor(request,pitanjeID):
    odgovor = Odgovor.objects.filter(pitanjeID_id=pitanjeID)
    data = [{'id': o.pk, 'tekst': o.tekst} for o in odgovor]
    return JsonResponse(data, safe=False)