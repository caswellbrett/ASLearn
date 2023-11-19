from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Stage
from .models import Question


def index(request):
    return HttpResponse("Welcome screen!")


def menu(request):
    stage_list = Stage.objects.order_by("-length")
    output = ", ".join([s.title for s in stage_list])
    return HttpResponse(output)

def stage(request, stage_id):
    s = Stage.objects.get(pk=stage_id)
    questions = s.question_set.all()
    output = ", ".join([q.question_text for q in questions])
    return HttpResponse(output)

def question(request, stage_id, question_id):
    return HttpResponse("You're looking at question %s on stage %s!" % (question_id, stage_id))

