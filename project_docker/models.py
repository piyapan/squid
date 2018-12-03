from django.db import models


class Stack(models.Model):
    ORCHESTRATOR_CHOICES = (
        (1, 'docker'),
        (2, 'k8s')
    )
    stack_key = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    count = models.PositiveIntegerField(default=0)
    orchestrator = models.IntegerField(choices=ORCHESTRATOR_CHOICES, default=1)
    meta_data = models.TextField(default='')
    datetime_update = models.DateTimeField()
    datetime_create = models.DateTimeField()


class Service(models.Model):
    STATUS_CHOICES = (
        (-3, 'down'),
        (-2, 'warning'),
        (-1, 'unknown'),
        (0, 'pending'),
        (1, 'healthy'),
        (2, 'starting'),
        (3, 'restart')
    )

    stack = models.ForeignKey('project_docker.Stack', on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    service_key = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    count = models.IntegerField(default=0)
    meta_data = models.TextField(default='')

    datetime_update = models.DateTimeField()
    datetime_create = models.DateTimeField()
