from rest_framework import viewsets

from todo.models import Todo
from todo.serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Todo.objects.all().order_by('period_date')
    serializer_class = TodoSerializer
