from django.shortcuts import render
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from crm.models import Paciente, Provincia
from crm.serializers import PacienteSerializer, ProvinciaSerializer


# Create your views here.


class Pacientes(APIView):
    def get(self, request):
        queryset = Paciente.objects.all()
        serializer = PacienteSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PacienteSerializer(request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class Provincias(APIView):
    def get(self, request):
        queryset = Provincia.objects.all()
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


class ProvinciaView(APIView):

    def get_object(self, pk):
        try:
            return Provincia.objects.get(pk=pk)
        except Provincia.DoesNotExist:
            raise ValueError

    def get(self, request, pk, format=None):
        provincia = self.get_object(pk)
        serializer = ProvinciaSerializer(provincia)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        provincia = self.get_object(pk)
        serializer = ProvinciaSerializer(provincia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        provincia = self.get_object(pk)
        provincia.delete()
        return Response(data='Delete', status=status.HTTP_410_GONE)