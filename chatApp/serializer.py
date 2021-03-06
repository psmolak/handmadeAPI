from rest_framework import serializers

from chatApp.models import Message
from user.models import User


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='nickname', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='nickname', queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']