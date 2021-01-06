from django.shortcuts import render
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from crm.models import FormaClinicaModel
from crm.serializers import FormaClinicaSerializer

# Create your views here.

class FormasClinicasView(APIView):
    def get(self, request):
        queryset = FormaClinicaModel.objects.all()
        serializer = FormaClinicaSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = FormaClinicaSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request):
        FormaClinicaModel.objects.all().delete()
        return Response(data='All records has been deleted.', status=status.HTTP_410_GONE)


class FormaClinicaView(APIView):

    def get_object(self, pk):
        try:
            return FormaClinicaModel.objects.get(pk=pk)
        except FormaClinicaModel.DoesNotExist:
            raise ValueError

    def get(self, request, pk, format=None):
        formaClinica = self.get_object(pk)
        serializer = FormaClinicaSerializer(formaClinica)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        formaClinica = self.get_object(pk)
        serializer = FormaClinicaSerializer(
            formaClinica, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk, format=None):
        formaClinica = self.get_object(pk)
        formaClinica.delete()
        return Response(data='The record has been deleted.', status=status.HTTP_410_GONE)
