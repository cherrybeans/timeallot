from rest_framework import serializers

from timeallot.apps.user.models import TimerUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TimerUser
        fields = ('id', 'email', 'display_name', 'date_joined', 'last_login', 'is_active', 'is_admin', 'url')
