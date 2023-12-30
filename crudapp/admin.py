from django.contrib import admin
from .models import WorkoutDetails


@admin.register(WorkoutDetails)
class WorkoutDetails(admin.ModelAdmin):
    list_display = ["id", "name", "reps", "sets", "kg", "date"]
