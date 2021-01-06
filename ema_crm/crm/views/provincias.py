from django.shortcuts import render
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from crm.models import ProvinciaModel
from crm.serializers import ProvinciaSerializer

# Create your views here.

class ProvinciasView(APIView):
    def get(self, request):
        queryset = ProvinciaModel.objects.all()
        serializer = ProvinciaSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProvinciaSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request):
        ProvinciaModel.objects.all().delete()
        return Response(data='All records has been deleted.', status=status.HTTP_410_GONE)


class ProvinciaView(APIView):

    def get_object(self, pk):
        try:
            return ProvinciaModel.objects.get(pk=pk)
        except ProvinciaModel.DoesNotExist:
            raise ValueError

    def get(self, request, pk, format=None):
        provincia = self.get_object(pk)
        serializer = ProvinciaSerializer(provincia)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        provincia = self.get_object(pk)
        serializer = ProvinciaSerializer(
            provincia, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk, format=None):
        provincia = self.get_object(pk)
        provincia.delete()
        return Response(data='The record has been deleted.', status=status.HTTP_410_GONE)
