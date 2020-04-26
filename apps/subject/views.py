from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.subject.models import SubjectExercise


@login_required(login_url="login")
def subject_exercises_view(request, pk):
    exercises = SubjectExercise.objects.filter(subject=pk).order_by("-date_created")
    context = {
        "exercises": exercises,
    }
    return render(request, 'subject/exercises.html', context)
