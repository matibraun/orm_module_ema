from django.shortcuts import render
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from crm.models import DomicilioModel
from crm.serializers import DomicilioSerializer

# Create your views here.

class DomiciliosView(APIView):
    def get(self, request):
        queryset = DomicilioModel.objects.all()
        serializer = DomicilioSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DomicilioSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request):
        DomicilioModel.objects.all().delete()
        return Response(data='All records has been deleted.', status=status.HTTP_410_GONE)


class DomicilioView(APIView):

    def get_object(self, pk):
        try:
            return DomicilioModel.objects.get(pk=pk)
        except DomicilioModel.DoesNotExist:
            raise ValueError

    def get(self, request, pk, format=None):
        domicilio = self.get_object(pk)
        serializer = DomicilioSerializer(domicilio)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        domicilio = self.get_object(pk)
        serializer = DomicilioSerializer(
            domicilio, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk, format=None):
        domicilio = self.get_object(pk)
        domicilio.delete()
        return Response(data='The record has been deleted.', status=status.HTTP_410_GONE)
