from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from listar.serializer import ListarSerializer
import pandas as pd
import numpy as np

class ListarApiView(APIView):
    """ Clase API para listar elementos """

    def get(self, request, format =  None):
        """ Devulve el saludo por ahora """
        saludo = ['Esto es una prueba para api, solo tiene el metodo post']
        return Response({"mensaje":"Bienvenido", "saludo": saludo})
    
    def post(self, request):
        serializer = ListarSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data.get('maximo')
            listado = [*range(data)]
            listado2 = [*range(data)]
            
            df = pd.DataFrame({"col1": listado, "col2": listado2})
            #salida = df.to_dict('index')
            salida = df.to_dict('records')
            #salida = df.to_dict('split')

            return Response({"mensaje":"hola", "salida": salida})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
