from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ParadignView(viewsets.ModelViewSet):
    queryset = Paradign.objects.all()
    serializer_class = ParadignSerializer

class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer