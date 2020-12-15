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
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        FormaClinicaModel.objects.all().delete()
        return Response(data='All Deleted', status=status.HTTP_410_GONE)

class FormaClinicaView(APIView):

    def get_object(self, pk):
        try:
            return FormaClinicaModel.objects.get(pk=pk)
        except FormaClinicaModel.DoesNotExist:
            raise ValueError

    def get(self, request, pk, format=None):
        formaClinica = self.get_object(pk)
        serializer = FormaClinicaSerializer(formaClinica)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        formaClinica = self.get_object(pk)
        serializer = FormaClinicaSerializer(formaClinica, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        formaClinica = self.get_object(pk)
        formaClinica.delete()
        return Response(data='Delete', status=status.HTTP_410_GONE)