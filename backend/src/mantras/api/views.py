from rest_framework import viewsets

from mantras.models import Family, Group, Mantra
from .serializers import FamilySerializer, GroupSerializer, MantraSerializer

class FamilyViewSet(viewsets.ModelViewSet):
    serializer_class = FamilySerializer
    queryset = Family.objects.all()

class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

class MantraViewSet(viewsets.ModelViewSet):
    serializer_class = MantraSerializer
    queryset = Mantra.objects.all()