from rest_framework import serializers
from notification_admin.models import NotificationAdmin


class android_serializers(serializers.ModelSerializer):
    class Meta:
        model=NotificationAdmin
        fields='__all__'