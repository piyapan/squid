from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models


class Controller(models.Model):
    max_memory = models.PositiveIntegerField(default=0, max_length=90)
    max_cpu = models.PositiveIntegerField(default=0, max_length=90)
    min_memory = models.PositiveIntegerField(default=0)
    min_cpu = models.PositiveIntegerField(default=0)

    is_auto_scale = models.BooleanField(default=False)
    max_scale = models.PositiveIntegerField(default=0)
    min_scale = models.PositiveIntegerField(default=0)


class Mode(models.Model):
    controller = models.ForeignKey('controller.Controller', on_delete=models.CASCADE)
    content_type = models.ForeignKey('contenttypes.ContentType', related_name='+', on_delete=models.CASCADE)
    content_id = models.PositiveIntegerField()
    content = GenericForeignKey('content_type', 'content_id')
    is_active = models.BooleanField(default=False)
