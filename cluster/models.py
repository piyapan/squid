from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models


class Cluster(models.Model):
    name = models.CharField(max_length=255)
    token = models.CharField(max_length=255, unique=True)
    datetime_create = models.DateTimeField(auto_created=True, auto_now_add=True)
    datetime_update = models.DateTimeField(auto_created=True, auto_now_add=True)


class Instance(models.Model):
    ROL_CHOICES = (
        (0, 'not set'),
        (1, 'master'),
        (2, 'worker'),
        (3, 'shooter'),
    )
    STATUS_CHOICES = (
        (-3, 'down'),
        (-2, 'warning'),
        (-1, 'unknown'),
        (0, 'pending'),
        (1, 'healthy'),
        (2, 'starting'),
    )

    role = models.IntegerField(choices=ROL_CHOICES, default=0)
    cluster = models.ForeignKey('cluster.Cluster', null=True, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='')
    ip_address = models.IPAddressField(),
    status = models.IntegerField(choices=STATUS_CHOICES, default=-1)

    datetime_create = models.DateTimeField(auto_created=True, auto_now_add=True)
    datetime_update = models.DateTimeField(auto_created=True, auto_now_add=True)


class Content(models.Model):
    instance = models.ForeignKey('cluster.Instance', on_delete=models.CASCADE)
    content_type = models.ForeignKey('contenttypes.ContentType', related_name='+', on_delete=models.CASCADE)
    content_id = models.PositiveIntegerField()
    content = GenericForeignKey('content_type', 'content_id')
