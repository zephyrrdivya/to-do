from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwnerOrReadOnly


# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'tasks': reverse('task-list', request=request, format=format)
#     })


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
