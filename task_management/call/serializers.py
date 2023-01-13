from rest_framework import serializers
from call.models import Call


class android_serializers(serializers.ModelSerializer):
    class Meta:
        model=Call
        fields='__all__'