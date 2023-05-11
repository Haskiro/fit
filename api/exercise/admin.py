from django.contrib import admin
from exercise.models import Exercise

# Register your models here.
@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ("title", "approaches")
    ordering = ('?',)
    search_fields = ("title__startswith",)
