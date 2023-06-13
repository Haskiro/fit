from django.contrib import admin
from program.models import Program


# Register your models here.
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("title", "target", "body_type", "complexity")
    ordering = ("?",)
    search_fields = ("title__startswith",)


# Register your models here.
