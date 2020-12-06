from django.shortcuts import render
from .models import Project
from skills.models import Skill

def home(request):
    projects = Project.objects
    skills = Skill.objects
    return render(request, 'projects/home.html', {'projects':projects, 'skills':skills})
