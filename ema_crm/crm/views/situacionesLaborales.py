from django.shortcuts import render
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from crm.models import SituacionLaboralModel
from crm.serializers import SituacionLaboralSerializer

# Create your views here.


class SituacionesLaboralesView(APIView):
    def get(self, request):
        queryset = SituacionLaboralModel.objects.all()
        serializer = SituacionLaboralSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SituacionLaboralSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request):
        SituacionLaboralModel.objects.all().delete()
        return Response(data='All records have been deleted.', status=status.HTTP_410_GONE)


class SituacionLaboralView(APIView):

    def get_object(self, pk):
        try:
            return SituacionLaboralModel.objects.get(pk=pk)
        except SituacionLaboralModel.DoesNotExist:
            raise ValueError

    def get(self, request, pk, format=None):
        situacionLaboral = self.get_object(pk)
        serializer = SituacionLaboralSerializer(situacionLaboral)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        situacionLaboral = self.get_object(pk)
        serializer = SituacionLaboralSerializer(
            situacionLaboral, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk, format=None):
        situacionLaboral = self.get_object(pk)
        situacionLaboral.delete()
        return Response(data='The record has been deleted.', status=status.HTTP_410_GONE)
