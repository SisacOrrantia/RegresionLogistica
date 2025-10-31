from rest_framework import serializers

class PredictionSerializer(serializers.Serializer):
    x = serializers.IntegerField(min_value=18, max_value=100)
