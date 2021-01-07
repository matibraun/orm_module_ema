from django.shortcuts import render
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from crm.models import CoberturaMedicaModel
from crm.serializers import CoberturaMedicaSerializer

# Create your views here.


class CoberturasMedicasView(APIView):
    def get(self, request):
        queryset = CoberturaMedicaModel.objects.all()
        serializer = CoberturaMedicaSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CoberturaMedicaSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request):
        CoberturaMedicaModel.objects.all().delete()
        return Response(data='All records have been deleted.', status=status.HTTP_410_GONE)


class CoberturaMedicaView(APIView):

    def get_object(self, pk):
        try:
            return CoberturaMedicaModel.objects.get(pk=pk)
        except CoberturaMedicaModel.DoesNotExist:
            raise ValueError

    def get(self, request, pk, format=None):
        coberturaMedica = self.get_object(pk)
        serializer = CoberturaMedicaSerializer(coberturaMedica)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        coberturaMedica = self.get_object(pk)
        serializer = CoberturaMedicaSerializer(
            coberturaMedica, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk, format=None):
        coberturaMedica = self.get_object(pk)
        coberturaMedica.delete()
        return Response(data='The record has been deleted.', status=status.HTTP_410_GONE)
