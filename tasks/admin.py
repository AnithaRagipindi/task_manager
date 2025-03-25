from django.contrib import admin
from .models import User, Task

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'mobile')
    search_fields = ('username', 'email')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'task_type', 'status', 'created_at')
    list_filter = ('task_type', 'status')
    search_fields = ('name', 'description')