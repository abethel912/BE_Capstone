from django.shortcuts import render
from .models import Activity
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ActivitySerializer
# Create your views here.


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.AllowAny]

