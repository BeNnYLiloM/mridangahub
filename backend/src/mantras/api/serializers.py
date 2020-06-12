from rest_framework import serializers

from mantras.models import Family, Group, Mantra

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