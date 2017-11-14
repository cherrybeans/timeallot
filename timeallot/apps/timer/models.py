from django.db import models
from timeallot.apps.user.models import TimerUser


class AbstractTag(models.Model):
    user = models.ForeignKey(TimerUser)
    tag_name = models.CharField(max_length=30)
    color = models.CharField(max_length=10)

    class Meta:
        abstract = True


class Category(models.Model):
    category_name = models.CharField(max_length=30)


class ProjectTag(AbstractTag):
    category = models.ForeignKey(Category, default=None)


class SubTag(AbstractTag):
    parent = models.ForeignKey(ProjectTag, related_name='subtags', null=False)


class Session(models.Model):
    duration = models.PositiveSmallIntegerField(default=25)
    starttime = models.DateTimeField()
    project = models.ForeignKey(ProjectTag, null=True)
    subtags = models.ManyToManyField(SubTag)
