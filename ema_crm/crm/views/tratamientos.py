from django.shortcuts import render
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from crm.models import TratamientoModel
from crm.serializers import TratamientoSerializer

# Create your views here.

class TratamientosView(APIView):
    def get(self, request):
        queryset = TratamientoModel.objects.all()
        serializer = TratamientoSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TratamientoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request):
        TratamientoModel.objects.all().delete()
        return Response(data='All Deleted', status=status.HTTP_410_GONE)


class TratamientoView(APIView):

    def get_object(self, pk):
        try:
            return TratamientoModel.objects.get(pk=pk)
        except TratamientoModel.DoesNotExist:
            raise ValueError

    def get(self, request, pk, format=None):
        tratamiento = self.get_object(pk)
        serializer = TratamientoSerializer(tratamiento)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        tratamiento = self.get_object(pk)
        serializer = TratamientoSerializer(
            tratamiento, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tratamiento = self.get_object(pk)
        tratamiento.delete()
        return Response(data='Delete', status=status.HTTP_410_GONE)
