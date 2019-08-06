from rest_framework import viewsets
# from rest_framework import mixins
# from rest_framework import generics

from pythonassignment.models import ServiceError
from pythonassignment.serializers import ServiceErrorSerializer


class ServiceErrorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ServiceError.objects.all().order_by('-ts_created')
    serializer_class = ServiceErrorSerializer


class RaiseErrorViewSet(viewsets.ModelViewSet):
    """
    List all snippets, or create a new snippet.
    """
    queryset = ServiceError.objects.all().order_by('-ts_created')
    serializer_class = ServiceErrorSerializer

    def list(self, request, format=None):
        x = 1
        y = 0
        return x/y
