from django.shortcuts import render
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from crm.models import PacienteModel
from crm.serializers import PacienteSerializer

# Create your views here.


class PacientesView(APIView):
    def get(self, request):
        queryset = PacienteModel.objects.all()
        serializer = PacienteSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PacienteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request):
        PacienteModel.objects.all().delete()
        return Response(data='All records have been deleted.', status=status.HTTP_410_GONE)


class PacienteView(APIView):

    def get_object(self, pk):
        try:
            return PacienteModel.objects.get(pk=pk)
        except PacienteModel.DoesNotExist:
            raise ValueError

    def get(self, request, pk, format=None):
        paciente = self.get_object(pk)
        serializer = PacienteSerializer(paciente)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        paciente = self.get_object(pk)
        serializer = PacienteSerializer(
            paciente, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk, format=None):
        paciente = self.get_object(pk)
        paciente.delete()
        return Response(data='The record has been deleted.', status=status.HTTP_410_GONE)
