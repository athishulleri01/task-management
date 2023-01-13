from rest_framework import serializers
from sub_task.models import SubTask


class android_serializers(serializers.ModelSerializer):
    class Meta:
        model=SubTask
        fields='__all__'