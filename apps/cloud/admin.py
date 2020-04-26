from django.contrib import admin

from apps.subject.models import (
    Subject,
    SubjectExercise,
)

admin.site.register(Subject)
admin.site.register(SubjectExercise)
