from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from listar import serializers
import pandas as pd
import numpy as np

class ListarApiView(APIView):
    """ Clase API para listar elementos """

    serializer_class = serializers.ListarSerializer
    
    def get(self, request, format =  None):
        """ Devulve el saludo por ahora """
        saludo = ['Esto es una prueba para api, solo tiene el metodo post']
        return Response({"mensaje":"Bienvenido", "saludo": saludo})
    
    def post(self, request):
        my_serializer = self.serializer_class(data=request.data)
        if my_serializer.is_valid():
            data = my_serializer.validated_data.get('cantidad')
            listado = [*range(0,data,2)]
            listado2 = [*range(1,data+1,2)]
            
            df = pd.DataFrame({"pares": listado, "impares": listado2})
            #salida = df.to_dict('index')
            salida = df.to_dict('records')
            #salida = df.to_dict('split')

            return Response({"mensaje":"Data frame de pares e impares", "cantidad": data, "salida": salida})
            #esta opcion no me gusto
            #return JsonResponse('salida {}'.format(df), safe=False) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
