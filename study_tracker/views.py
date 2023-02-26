from django.shortcuts import render
from study_tracker.models import Assignment
# Create your views here.
def show_tracker(request):
    assignment_data = Assignment.objects.all()
    context = {
        'list_of_assignments' : assignment_data
    }
    return render(request, "home.html", context)
