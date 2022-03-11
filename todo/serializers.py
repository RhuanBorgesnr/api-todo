from importlib.metadata import files
from todo.models import Todo

from rest_framework import serializers

#serialization
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'name', 'done', 'create_at']