"""
URL configuration for postgresTest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testdb.views import CategoryViewSet, OperationViewSet
from rest_framework.urlpatterns import format_suffix_patterns

category_list = CategoryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
category_detail = CategoryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

operation_list = OperationViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
operation_detail = OperationViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



urlpatterns = [
    path('admin/', admin.site.urls),
    #path('goals/', goal_list, name='goal_list')
    path('catergories/', category_list, name='category-list'),
    path('catergories/<int:pk>/', category_detail, name='category-detail'),
    path('operations/', operation_list, name='operation-list'),
    path('operations/<int:pk>/', operation_detail, name='operation-detail'),
]
