from rest_framework import serializers

class ListarSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField(min_value=0)