from rest_framework import viewsets

from timeallot.apps.user.models import TimerUser
from timeallot.apps.user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TimerUser.objects.all()
    serializer_class = UserSerializer
