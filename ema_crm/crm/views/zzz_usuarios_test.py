from django.shortcuts import render
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from crm.models import UsuarioModel
from crm.serializers import UsuarioSerializer

# Create your views here.

class UsuariosView(APIView):
    def get(self, request):
        queryset = UsuarioModel.objects.all()
        serializer = UsuarioSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        


class UsuarioView(APIView):

    def get_object(self, pk):
        return UsuarioModel.objects.get(pk=pk)
        
    def get(self, request, pk, format=None):
        try:
            usuario = self.get_object(pk)
            raise Exception("cualquiera")
            serializer = UsuarioSerializer(usuario)
            return Response(serializer.data)
        except UsuarioModel.DoesNotExist:
            return Response("ups", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        usuario = self.get_object(pk)
        usuario.delete()
        return Response(data='Delete', status=status.HTTP_410_GONE)
