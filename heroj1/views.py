from django.contrib.auth.models import User, AnonymousUser
from django.core import serializers
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from heroj1.models import Obavjest, Lekcija, Blog, Pitanje, UserProfile, Odgovor, FirstAid, KvizRezultati
from .serializers import ProfileSerializer, FirstAidSerializer


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
            'video': request.build_absolute_uri(fields.video.url) if fields.video else None,
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
            'video': request.build_absolute_uri(fields.video.url) if fields.video else None,
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
@api_view(['GET'])
def getBolest(request,firstaid_id):
    bolest = FirstAid.objects.get(pk=firstaid_id)
    res = serializers.serialize('json',[bolest,])

    data=[]
    for bolest1 in serializers.deserialize('json',res):
        fields = bolest1.object
        data.append({
            'id': fields.pk,
            'maintitle': fields.maintitle,
            'description': fields.description,
            'title': fields.title,
            'subtitle1': fields.subtitle1,
            'part1': fields.part1,
            'subtitle2': fields.subtitle2,
            'part2': fields.part2,
            'subtitle3': fields.subtitle3,
            'part3': fields.part3,
            'subtitle4': fields.subtitle4,
            'part4': fields.part4,
            'image': request.build_absolute_uri(fields.image.url) if fields.image else None,

        })
    return JsonResponse(data,safe=False)
@api_view(['GET'])
def getListaOdgovora(request):
    lista_odgovora = Odgovor.objects.all()
    rezultat = serializers.serialize('json', lista_odgovora)

    data = []
    for odgovor in serializers.deserialize('json', rezultat):
        fields = odgovor.object
        pitanje = fields.pitanjeID
        data.append({
            'id': fields.pk,
            'tekst':fields.tekst,
            'pitanje':{
                'id2':pitanje.pk
            }
        })
    return JsonResponse(data, safe=False)
@api_view(['GET'])
def getLPitanja(request):
    lista_pitanja = Pitanje.objects.all()
    rezultat = serializers.serialize('json', lista_pitanja)

    data = []
    for pitanje in serializers.deserialize('json', rezultat):
        fields = pitanje.object
        data.append({
            'id': fields.pk,
            'tekst':fields.tekst,
        })
    return JsonResponse(data, safe=False)
@api_view(['GET'])
def getKvizRezultate(request):
    lista_rezultata=KvizRezultati.objects.all()
    rez=serializers.serialize('json',lista_rezultata)

    data=[]
    for rezultatic in serializers.deserialize('json',rez):
        fields=rezultatic.object
        data.append({
            'user_id':fields.user_id,
            'brojTacnih':fields.brojTacnih
        })
    return JsonResponse(data,safe=False)
@api_view(['POST'])
def posaljiRezultate(request):
    data = request.data
    brojTacnih = int(data.get('brojTacnih'))
    print(brojTacnih)
    user_id = int(data.get('user_id'))
    user_profile = get_object_or_404(UserProfile, id=user_id)
    KvizRezultati.objects.create(brojTacnih=brojTacnih, user_id=user_profile)
    if brojTacnih == 7 or brojTacnih == 8:
        return Response({'redirect': '/certifikat'})
    else:
        return Response({'redirect': '/Test'})
@api_view(['POST'])
def setProgres(request):
    if isinstance(request.user, AnonymousUser):
        return JsonResponse({'error': 'User not authenticated'})

    user_profile = UserProfile.objects.get(user_fk=request.user)
    user_profile.progres += 20
    user_profile.save()

    return JsonResponse({'success': True})

class search(generics.ListCreateAPIView):
    queryset = FirstAid.objects.all()
    serializer_class = FirstAidSerializer
    #filter_backends = [filters.SearchFilter]
    filter_backends = [SearchFilter]
    search_fields = ['^maintitle']


@api_view(['POST'])
def register(request):
    data = request.data

    user_data = {
        'username': data.get('username'),
        'password': data.get('password'),
        'email': data.get('email')
    }

    profile_data = {
        'firstName': data.get('firstName'),
        'lastName': data.get('lastName'),
        'email': data.get('email')
    }

    try:
        # Create a new User instance
        user = User.objects.create_user(**user_data)

        # Create a new UserProfile instance and associate it with the User
        profile = UserProfile.objects.create(user_fk=user, **profile_data)

        # Return a success response
        return Response({'success': 'User profile created successfully!'}, status=201)
    except Exception as e:
        return Response({'error': str(e)}, status=400)
