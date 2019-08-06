from pythonassignment.models import ServiceError
from rest_framework import serializers


class ServiceErrorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServiceError
        fields = ['message', 'representation', 'arguments', 'stacktrace']
