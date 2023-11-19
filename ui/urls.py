from django.urls import path

from . import views

app_name = "asl"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:stage_id>/<int:question_id>", views.question, name="question"),
    path("menu", views.menu, name="menu"),
]