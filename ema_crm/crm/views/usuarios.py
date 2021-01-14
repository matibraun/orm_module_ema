from django.shortcuts import render
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from crm.models import UserExtendidoModel
from crm.serializers import UsuarioSerializer, UserSerializer
from django.contrib.auth.models import User


# Create your views here.

class UsuariosView(APIView):
    def get(self, request):
        queryset = UserExtendidoModel.objects.all()
        serializer = UsuarioSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer_user = UserSerializer(data=request.data)
        # TODO: SUPER IMPORTANTE, TRANSACCION!!!
        if serializer_user.is_valid(raise_exception=False):
            user = serializer_user.save()
            serializer_usuario = UsuarioSerializer(data=request.data)
            if serializer_usuario.is_valid(raise_exception=False):
                serializer_usuario.save(user=user)
                return Response({**serializer_usuario.data, **serializer_user.data}, status=status.HTTP_201_CREATED)
            return Response(serializer_usuario.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(serializer_user.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request):
        UserExtendidoModel.objects.all().delete()
        return Response(data='All Deleted', status=status.HTTP_410_GONE)


class UsuarioView(APIView):

    def get_object(self, pk):
        try:
            return UserExtendidoModel.objects.get(pk=pk)
        except UserExtendidoModel.DoesNotExist:
            raise ValueError

    def get(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(
            usuario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        usuario = self.get_object(pk)
        usuario.delete()
        return Response(data='Delete', status=status.HTTP_410_GONE)
