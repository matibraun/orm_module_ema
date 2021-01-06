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
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        ProvinciaModel.objects.all().delete()
        return Response(data='All Deleted', status=status.HTTP_410_GONE)

class ProvinciaView(APIView):

    def get_object(self, pk):
        try:
            return ProvinciaModel.objects.get(pk=pk)
        except ProvinciaModel.DoesNotExist:
            raise ValueError

    def get(self, request, pk, format=None):
        provincia = self.get_object(pk)
        serializer = ProvinciaSerializer(provincia)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        provincia = self.get_object(pk)
        serializer = ProvinciaSerializer(provincia, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        provincia = self.get_object(pk)
        provincia.delete()
        return Response(data='Delete', status=status.HTTP_410_GONE)
