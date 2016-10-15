from todo.models import Todo
from rest_framework import serializers

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo 
        fields = ('title', 'description', 'period_date')


