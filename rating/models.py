from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel


class RatingElement(TimeStampedModel):
    element_type = models.CharField(max_length=50)
    score = models.SmallIntegerField(blank=True, null=True)
    comment = models.CharField(blank=True, null=True, max_length=512)

    class Meta:
        ordering = ('id', )


class ObjectRating(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_type = models.CharField(blank=True, null=True, max_length=50)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    elements = models.ManyToManyField(RatingElement)

    class Meta:
        ordering = ('id', )