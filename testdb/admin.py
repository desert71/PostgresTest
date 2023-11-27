from django.contrib import admin
from .models import Goal

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'goal_type', 'start_date', 'finish_date',)
    list_filter = ('goal_type', 'start_date', 'finish_date',)
    search_fields = ('name',)
    ordering = ('-start_date',)