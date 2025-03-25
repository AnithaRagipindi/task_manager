# tasks/serializers.py
from rest_framework import serializers
from .models import Task, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'mobile']

class TaskSerializer(serializers.ModelSerializer):
    assigned_users = UserSerializer(many=True, read_only=True)
    assigned_user_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User.objects.all(), source='assigned_users'
    )

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'created_at', 'task_type', 'status', 'completed_at', 'assigned_users_ids']


    