from django.db import models
from django.utils import timezone

from timeallot.apps.user.models import TimerUser


class AbstractTag(models.Model):
    user = models.ForeignKey(TimerUser, on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=30)
    color = models.CharField(max_length=10, default="e3e3e3")

    class Meta:
        abstract = True


class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.category_name


class ProjectTag(AbstractTag):
    category = models.ForeignKey(Category, related_name='projects', on_delete=models.CASCADE)

    def __str__(self):
        return self.tag_name


class SubTag(AbstractTag):
    parent = models.ForeignKey(ProjectTag, related_name='subtags', on_delete=models.CASCADE)

    def __str__(self):
        return self.tag_name


class Session(models.Model):
    user = models.ForeignKey(TimerUser, on_delete=models.CASCADE)
    duration = models.PositiveSmallIntegerField(default=25)
    start_time = models.DateTimeField(default=timezone.now)
    project = models.ForeignKey(ProjectTag, null=True, blank=True, on_delete=models.CASCADE)
    subtags = models.ManyToManyField(SubTag, blank=True)
