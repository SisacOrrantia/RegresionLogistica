from rest_framework import serializers

class PredictionSerializer(serializers.Serializer):
    x = serializers.IntegerField(min_value=0, max_value=100)
