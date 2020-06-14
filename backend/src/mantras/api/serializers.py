from rest_framework import serializers
from django.contrib.auth import get_user_model

from mantras.models import Family, Group, Mantra


# Get the UserModel
UserModel = get_user_model()

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fileds = ('id', 'name')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', 'family_id')

class MantraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mantra
        fields = ('id', 'name', 'scheme', 'visual_scheme', 'group_id')

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('pk', 'username', 'email', 'first_name', 'last_name', 'is_superuser')
        read_only_fields = ('email', 'is_superuser')
