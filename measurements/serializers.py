# TODO: опишите сериализаторы

from rest_framework import serializers
from .models import Project, Measurement


class ProjectSerializer(serializers.Serializer):
    class Meta:
        model = Project
        fields = '__all__'


class MeasurementSerializer(serializers.Serializer):
    class Meta:
        model = Measurement
        fields = '__all__'