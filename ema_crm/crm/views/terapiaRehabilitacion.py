from django.shortcuts import render
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from crm.models import TerapiaRehabilitacionModel
from crm.serializers import TerapiaRehabilitacionSerializer

# Create your views here.

class TerapiasRehabilitacionesView(APIView):
    def get(self, request):
        queryset = TerapiaRehabilitacionModel.objects.all()
        serializer = TerapiaRehabilitacionSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TerapiaRehabilitacionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request):
        TerapiaRehabilitacionModel.objects.all().delete()
        return Response(data='All records has been deleted.', status=status.HTTP_410_GONE)


class TerapiaRehabilitacionView(APIView):

    def get_object(self, pk):
        try:
            return TerapiaRehabilitacionModel.objects.get(pk=pk)
        except TerapiaRehabilitacionModel.DoesNotExist:
            raise ValueError

    def get(self, request, pk, format=None):
        terapiaRehabilitacion = self.get_object(pk)
        serializer = TerapiaRehabilitacionSerializer(terapiaRehabilitacion)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        terapiaRehabilitacion = self.get_object(pk)
        serializer = TerapiaRehabilitacionSerializer(
            terapiaRehabilitacion, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk, format=None):
        terapiaRehabilitacion = self.get_object(pk)
        terapiaRehabilitacion.delete()
        return Response(data='The record has been deleted.', status=status.HTTP_410_GONE)
