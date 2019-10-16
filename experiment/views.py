from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("You're at the splash page for the Sensation and Perception experiment")


def consent(request):
    return HttpResponse("You're at the consent page for the Sensation and Perception experiment")


def subject_data(request):
    return HttpResponse("You're at the subject data entry page")


def instructions(request):
    return HttpResponse("Instructions for the Sensation and Perception experiment")


def experiment(request):
    return HttpResponse("experiment!")
