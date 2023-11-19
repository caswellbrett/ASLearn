from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:stage_id>/", views.stage, name="stage"),
    path("<int:stage_id>/<int:question_id>", views.question, name="question"),
    path("menu", views.menu, name="menu")
]