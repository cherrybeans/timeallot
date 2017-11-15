from rest_framework import serializers
from timeallot.apps.timer.models import (
    Category, ProjectTag, SubTag, Session
)


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('url', 'id', 'category_name')


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectTag
        fields = ('url', 'id', 'user', 'tag_name', 'color', 'category')


class SubtagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubTag
        fields = ('url', 'id', 'user', 'tag_name', 'color', 'parent')


class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = ('url', 'id', 'duration', 'start_time', 'project', 'subtags')
