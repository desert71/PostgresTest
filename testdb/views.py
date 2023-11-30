#from django.shortcuts import render
#from django.http import JsonResponse
#from .models import Goal
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Operation, Category
from .serializers import OperationSerializer, CategorySerializer

# def goal_list(request):
#     goals = Goal.objects.goals()
#     data = {"goals": list(goals.values())}
#     return JsonResponse(data)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
