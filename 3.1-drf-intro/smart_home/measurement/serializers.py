from rest_framework import serializers
from .models import Measurement, Sensor


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ['sensor_id', 'temperature', 'created_at', 'shot']

    def to_representation(self, obj):
        rep = super(MeasurementSerializer, self).to_representation(obj)
        rep.pop('sensor_id', None)
        return rep


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']

