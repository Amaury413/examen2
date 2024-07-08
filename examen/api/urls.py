from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TasksViewSet
from . import views

router = DefaultRouter()
router.register(r'tarea', TasksViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('actividades/ids/', views.get_all_actividades_ids, name='get_all_actividades_ids'),
    path('actividades/ids-titles/', views.get_all_actividades_ids_titles, name='get_all_actividades_ids_titles'),
    path('actividades/notfinish-ids-titles/', views.get_notfinish_actividades_ids_titles, name='get_notfinish_actividades_ids_titles'),
    path('actividades/finish-ids-titles/', views.get_finish_actividades_ids_titles, name='get_finish_actividades_ids_titles'),
    path('actividades/ids-userids/', views.get_all_actividades_ids_userids, name='get_all_actividades_ids_userids'),
    path('actividades/finish-ids-userids/', views.get_finish_actividades_ids_userids, name='get_finish_actividades_ids_userids'),
    path('actividades/notfinish-ids-userids/', views.get_notfinish_actividades_ids_userids, name='get_notfinish_actividades_ids_userids'),
]