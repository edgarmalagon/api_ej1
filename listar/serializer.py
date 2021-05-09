from rest_framework import serializers

class ListarSerializer(serializers.Serializer):
    maximo = serializers.IntegerField(min_value=0)