from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Task
from .serializer import TaskSerializer

class TasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

def get_all_actividades_ids(request):
    actividades = Task.objects.values_list('id', flat=True)
    return JsonResponse(list(actividades), safe=False)

def get_all_actividades_ids_titles(request):
    actividades = Task.objects.values('id', 'title')
    return JsonResponse(list(actividades), safe=False)

def get_notfinish_actividades_ids_titles(request):
    actividades = Task.objects.filter(completed=False).values('id', 'title')
    return JsonResponse(list(actividades), safe=False)

def get_finish_actividades_ids_titles(request):
    actividades = Task.objects.filter(completed=True).values('id', 'title')
    return JsonResponse(list(actividades), safe=False)

def get_all_actividades_ids_userids(request):
    actividades = Task.objects.values('id', 'user_id')
    return JsonResponse(list(actividades), safe=False)

def get_finish_actividades_ids_userids(request):
    actividades = Task.objects.filter(completed=True).values('id', 'user_id')
    return JsonResponse(list(actividades), safe=False)

def get_notfinish_actividades_ids_userids(request):
    actividades = Task.objects.filter(completed=False).values('id', 'user_id')
    return JsonResponse(list(actividades), safe=False)