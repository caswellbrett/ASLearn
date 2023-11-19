from django.contrib import admin
from .models import Question
from .models import Stage

# Register your models here.

admin.site.register(Stage)
admin.site.register(Question)
