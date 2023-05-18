from rest_framework.serializers import ModelSerializer

from heroj1.models import UserProfile


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'