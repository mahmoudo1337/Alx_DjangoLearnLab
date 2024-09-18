# notifications/serializers.py

from rest_framework import serializers
from .models import Notification
from django.contrib.contenttypes.models import ContentType

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()
    target = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'target', 'timestamp', 'read']

    def get_target(self, obj):
        return f"{obj.target_content_type} - {obj.target_object_id}"
