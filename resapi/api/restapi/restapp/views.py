from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TaskSerializer, UserSerializer
from .models import Task
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView

# Create your views here.
class TaskViewset(viewsets.ModelViewSet):
    Permission_classes=(IsAuthenticated,)
    queryset=Task.objects.all().order_by('-date')
    serializer_class=TaskSerializer

class DueTaskViewset(viewsets.ModelViewSet):
    queryset=Task.objects.all().order_by('-date').filter(completed=False)
    serializer_class=TaskSerializer

class CreateuserView(CreateAPIView):
    model = 'get_user_model'
    permission_classes = (AllowAny,)
    serializer_class =UserSerializer



class CompleteTaskViewset(viewsets.ModelViewSet):
    queryset=Task.objects.all().order_by('-date').filter(completed=True)
    serializer_class=TaskSerializer