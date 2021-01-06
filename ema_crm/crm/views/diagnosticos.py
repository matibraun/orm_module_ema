from django.shortcuts import render
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from crm.models import DiagnosticoModel
from crm.serializers import DiagnosticoSerializer

# Create your views here.

class DiagnosticosView(APIView):
    def get(self, request):
        queryset = DiagnosticoModel.objects.all()
        serializer = DiagnosticoSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DiagnosticoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request):
        DiagnosticoModel.objects.all().delete()
        return Response(data='All records has been deleted.', status=status.HTTP_410_GONE)


class DiagnosticoView(APIView):

    def get_object(self, pk):
        try:
            return DiagnosticoModel.objects.get(pk=pk)
        except DiagnosticoModel.DoesNotExist:
            raise ValueError

    def get(self, request, pk, format=None):
        diagnostico = self.get_object(pk)
        serializer = DiagnosticoSerializer(diagnostico)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        diagnostico = self.get_object(pk)
        serializer = DiagnosticoSerializer(
            diagnostico, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk, format=None):
        diagnostico = self.get_object(pk)
        diagnostico.delete()
        return Response(data='The record has been deleted.', status=status.HTTP_410_GONE)
