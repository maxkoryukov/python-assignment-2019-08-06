from django.db import models


class ServiceError(models.Model):
    app_label = 'service-error'

    id = models.AutoField(primary_key=True)

    message = models.CharField(max_length=10000)
    representation = models.CharField(max_length=10000)
    arguments = models.CharField(max_length=10000)
    stacktrace = models.CharField(max_length=10000)

    ts_created = models.DateTimeField(auto_now_add=True)
