from django.shortcuts import render
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from crm.models import TallerPacienteModel
from crm.serializers import TallerPacienteSerializer

# Create your views here.


class TalleresPacientesView(APIView):
    def get(self, request):
        queryset = TallerPacienteModel.objects.all()
        serializer = TallerPacienteSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TallerPacienteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request):
        TallerPacienteModel.objects.all().delete()
        return Response(data='All records have been deleted.', status=status.HTTP_410_GONE)


class TallerPacienteView(APIView):

    def get_object(self, pk):
        try:
            return TallerPacienteModel.objects.get(pk=pk)
        except TallerPacienteModel.DoesNotExist:
            raise ValueError

    def get(self, request, pk, format=None):
        tallerPaciente = self.get_object(pk)
        serializer = TallerPacienteSerializer(tallerPaciente)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        tallerPaciente = self.get_object(pk)
        serializer = TallerPacienteSerializer(
            tallerPaciente, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk, format=None):
        tallerPaciente = self.get_object(pk)
        tallerPaciente.delete()
        return Response(data='The record has been deleted.', status=status.HTTP_410_GONE)
