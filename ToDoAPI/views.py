from rest_framework import generics
from .models import Todo
from .serializer import TodoSerializer

class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
