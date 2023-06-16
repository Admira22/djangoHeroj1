from rest_framework.serializers import ModelSerializer

from heroj1.models import UserProfile
from heroj1.models import FirstAid


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
class FirstAidSerializer(ModelSerializer):
    class Meta:
        model = FirstAid
        fields = '__all__'