from __future__ import absolute_import, unicode_literals
from celery.decorators import task

from .models import ServiceError


@task(name='save_exception_task')
def save_exception_task(message, representation, arguments, stacktrace):
    # print('Request: {0!r}'.format(self.request))

    #from pythonassignment import models
    #d = models.ServiceError(message, representation, arguments, stacktrace)

    service_error = ServiceError.objects.create()
    service_error.message = message
    service_error.representation = representation
    service_error.arguments = arguments
    service_error.stacktrace = stacktrace
    service_error.save()
