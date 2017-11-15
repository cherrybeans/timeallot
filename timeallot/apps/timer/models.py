from django.db import models
from timeallot.apps.user.models import TimerUser
from django.utils import timezone


class AbstractTag(models.Model):
    user = models.ForeignKey(TimerUser)
    tag_name = models.CharField(max_length=30, unique=True)
    color = models.CharField(max_length=10, default="e3e3e3")

    class Meta:
        abstract = True


class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)


class ProjectTag(AbstractTag):
    category = models.ForeignKey(Category, related_name='projects', default=1)


class SubTag(AbstractTag):
    parent = models.ForeignKey(ProjectTag, related_name='subtags')


class Session(models.Model):
    duration = models.PositiveSmallIntegerField(default=25)
    start_time = models.DateTimeField(default=timezone.now)
    project = models.ForeignKey(ProjectTag, null=True, blank=True)
    subtags = models.ManyToManyField(SubTag, blank=True)
