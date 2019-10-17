from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subject_data', views.subject_data, name='subject_data'),
    path('instructions', views.instructions, name='instructions'),
    path('experiment', views.experiment, name='experiment'),
]
