from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models


class Image(models.Model):
    repository = models.CharField(max_length=255)
    tag = models.CharField(max_length=255),
    create_date = models.DateTimeField(),
    size = models.PositiveIntegerField(default=0)

    is_authenticate = models.BooleanField(default=False)
    authenticate_username = models.CharField(max_length=255, default='')
    authenticate_password = models.CharField(max_length=255, default='')

    datetime_create = models.DateTimeField(auto_now_add=True, auto_created=True)
    datetime_update = models.DateTimeField(auto_now_add=True, auto_created=True)


class Content(models.Model):
    image = models.ForeignKey('image.Image', on_delete=models.CASCADE)
    content_type = models.ForeignKey('contenttypes.ContentType', on_delete=models.CASCADE)
    content_id = models.PositiveIntegerField()
    content = GenericForeignKey('content_type', 'content_id')
