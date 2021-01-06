from django.shortcuts import render
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from crm.models import ComposicionFamiliarModel
from crm.serializers import ComposicionFamiliarSerializer

# Create your views here.

class ComposicionesFamiliaresView(APIView):
    def get(self, request):
        queryset = ComposicionFamiliarModel.objects.all()
        serializer = ComposicionFamiliarSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ComposicionFamiliarSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request):
        ComposicionFamiliarModel.objects.all().delete()
        return Response(data='All records has been deleted.', status=status.HTTP_410_GONE)


class ComposicionFamiliarView(APIView):

    def get_object(self, pk):
        try:
            return ComposicionFamiliarModel.objects.get(pk=pk)
        except ComposicionFamiliarModel.DoesNotExist:
            raise ValueError

    def get(self, request, pk, format=None):
        composicionFamiliar = self.get_object(pk)
        serializer = ComposicionFamiliarSerializer(composicionFamiliar)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        composicionFamiliar = self.get_object(pk)
        serializer = ComposicionFamiliarSerializer(
            composicionFamiliar, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk, format=None):
        composicionFamiliar = self.get_object(pk)
        composicionFamiliar.delete()
        return Response(data='The record has been deleted.', status=status.HTTP_410_GONE)
