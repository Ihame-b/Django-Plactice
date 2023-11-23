from django.shortcuts import render
from rest_framework import generics
# from serializers import *
from rest_framework.serializers import *
from .models import *

# Create your views here.
class ListTodo(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ModelSerializer

class DetaisToDo(generics.RetrieveUpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ModelSerializer

class CreateTodo(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ModelSerializer

class DeleteToDo(generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ModelSerializer

