from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from paginas.api import serializers
from paginas import models

class TaskWiewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()