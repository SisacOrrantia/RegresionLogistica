from rest_framework import serializers

class PredictionSerializer(serializers.Serializer):
    edad = serializers.IntegerField(min_value=18, max_value=100)
    salario = serializers.FloatField(min_value=0)
