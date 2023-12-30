from django.shortcuts import render
from .models import WorkoutDetails
from django.contrib import messages
from django.db.models import Q


def index(request):

    workouts = WorkoutDetails.objects.all()
    search_query = ""
    if request.method == "POST": 
        if "addworkout" in request.POST:
            name = request.POST.get("name")
            reps = request.POST.get("reps")
            sets = request.POST.get("sets")
            kg = request.POST.get("kg")
            date = request.POST.get("date")
            WorkoutDetails.objects.create(
                name=name,
                reps=reps,
                sets=sets,
                kg=kg,
                date=date,
            )
            messages.success(request, "Workout Added successfully")
    
        elif "update" in request.POST:
            id = request.POST.get("id")
            name = request.POST.get("name")
            reps = request.POST.get("reps")
            sets = request.POST.get("sets")
            kg = request.POST.get("kg")
            date = request.POST.get("date")
            workout = WorkoutDetails.objects.get(id=id)
            workout.name = name
            workout.reps = reps
            workout.sets = sets
            workout.kg = kg
            workout.date = date
            workout.save()
            messages.success(request, "Workout Updated Successfully")
    
        elif "delete" in request.POST:
            id = request.POST.get("id")
            WorkoutDetails.objects.get(id=id).delete()

            messages.success(request, "Workout Deleted Successfully")
        
        elif "search" in request.POST:
            search_query = request.POST.get("query")
            workouts = WorkoutDetails.objects.filter(Q(name__icontains=search_query))



    context = { "workouts": workouts, "search_query": search_query}
    return render(request, "index.html", context=context)
