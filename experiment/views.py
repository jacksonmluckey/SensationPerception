from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('experiment/index.html')
    context = {'hacky_solution': True} # Provides the necessary dictionary for the render function (alternative solution requires me to make changes to urls.py and use TemplateView.as_view according to StackOverflow)
    return HttpResponse(template.render(context, request))


def subject_data(request):
    return HttpResponse("You're at the subject data entry page")


def instructions(request):
    return HttpResponse("Instructions for the Sensation and Perception experiment")


def experiment(request):
    template = loader.get_template('experiment/experiment.html')
    context = {'hacky_solution': True}
    return HttpResponse(template.render(context, request))
