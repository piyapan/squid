from django.db import models

class Container(models.Model):
    STATUS_CHOICES = (
        (-3, 'down'),
        (-2, 'warning'),
        (-1, 'unknown'),
        (0, 'pending'),
        (1, 'healthy'),
        (2, 'starting'),
        (3, 'restart')
    )

    container_key = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    status = models.IntegerField(default=-1, choices=STATUS_CHOICES)
    count_restart = models.PositiveIntegerField(default=0)
    datetime_create = models.DateTimeField()
    datetime_update = models.DateTimeField()
    target_port = models.CharField(max_length=10, default='')
    command = models.CharField(max_length=255, default='')
    endpoint = models.CharField(max_length=255, default='')
    meta_data = models.TextField(default='')
