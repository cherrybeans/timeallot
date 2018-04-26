from rest_framework import serializers

from timeallot.apps.timer.models import Category, ProjectTag, Session, SubTag


class SubtagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubTag
        fields = ('id', 'tag_name', 'parent', 'color', 'url', 'user')


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    subtags = SubtagSerializer(many=True)

    class Meta:
        model = ProjectTag
        fields = ('id', 'tag_name', 'category', 'subtags', 'color', 'url', 'user')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    projects = ProjectSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'category_name', 'projects', 'url')


class SessionProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectTag
        fields = ('id', 'tag_name')


class SessionSubtagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubTag
        fields = ('id', 'tag_name')


class SessionSerializer(serializers.HyperlinkedModelSerializer):
    project = SessionProjectSerializer()
    subtags = SessionSubtagSerializer(many=True)

    class Meta:
        model = Session
        fields = ('id', 'duration', 'start_time', 'project', 'subtags', 'url')
