from django.shortcuts import render
from django.http import JsonResponse
from .models import Goal

def goal_list(request):
    goals = Goal.objects.goals()
    data = {"goals": list(goals.values())}
    return JsonResponse(data)

