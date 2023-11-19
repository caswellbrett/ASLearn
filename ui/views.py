from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Stage
from .models import User
from .models import Question
from django.shortcuts import get_object_or_404, render

current_user = ""

def index(request):
    return render(request, "ui/index.html", {})

def menu(request):
    global current_user
    username = request.POST.get('name', '')
    completed_stage = request.POST.get('completed_stage', '')

    if (username != ""): # if the page has been loaded from login screen
        try:
            user = User.objects.get(pk=username)
        except (KeyError, User.DoesNotExist):
            u = User(name=username)
            u.save()
            user = User.objects.get(pk=username)
        current_user = username
    else:
        user = User.objects.get(pk=current_user)

    if (completed_stage != ""): #the page has been loaded from a stage
        s = int(completed_stage)
        new_stage = s + 1
        if (new_stage > user.current_question):
            user.current_question = new_stage
            user.save()

    stage_list = Stage.objects.order_by("-length")
    context = { "stage_list": stage_list, "user": user}
    return render(request, "ui/menu.html", context)


def question(request, stage_id, question_id):
    if (stage_id == 1):
        question = Question.objects.get(pk=question_id)
    else:
        question = Question.objects.get(pk=10 + question_id)
    stage = Stage.objects.get(pk=stage_id)
    next = question.q_num + 1
    context = {"question": question, "stage": stage, "next": next}
    return render(request, "ui/question.html", context)

