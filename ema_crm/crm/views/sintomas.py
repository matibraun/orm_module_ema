from django.shortcuts import render
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from crm.models import SintomaModel
from crm.serializers import SintomaSerializer

# Create your views here.

class SintomasView(APIView):
    def get(self, request):
        queryset = SintomaModel.objects.all()
        serializer = SintomaSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SintomaSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request):
        SintomaModel.objects.all().delete()
        return Response(data='All records has been deleted.', status=status.HTTP_410_GONE)


class SintomaView(APIView):

    def get_object(self, pk):
        try:
            return SintomaModel.objects.get(pk=pk)
        except SintomaModel.DoesNotExist:
            raise ValueError

    def get(self, request, pk, format=None):
        sintoma = self.get_object(pk)
        serializer = SintomaSerializer(sintoma)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        sintoma = self.get_object(pk)
        serializer = SintomaSerializer(
            sintoma, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk, format=None):
        sintoma = self.get_object(pk)
        sintoma.delete()
        return Response(data='The record has been deleted.', status=status.HTTP_410_GONE)
