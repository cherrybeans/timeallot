from rest_framework import serializers
from timeallot.apps.user.models import TimerUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TimerUser
        fields = ('url', 'id', 'email', 'date_joined', 'is_active', 'is_admin')
