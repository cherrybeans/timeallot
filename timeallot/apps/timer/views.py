from rest_framework import viewsets
from rest_framework import permissions
from timeallot.apps.timer.models import (
    Category, ProjectTag, SubTag, Session
)
from timeallot.apps.timer.serializers import (
    CategorySerializer, ProjectSerializer, SubtagSerializer, SessionSerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    queryset = ProjectTag.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SubtagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows subtags to be viewed or edited.
    """
    queryset = SubTag.objects.all()
    serializer_class = SubtagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SessionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sessions to be viewed or edited.
    """
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)