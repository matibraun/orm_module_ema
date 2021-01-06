from django.shortcuts import render
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from crm.models import SituacionHabitacionalModel
from crm.serializers import SituacionHabitacionalSerializer

# Create your views here.

class SituacionesHabitacionalesView(APIView):
    def get(self, request):
        queryset = SituacionHabitacionalModel.objects.all()
        serializer = SituacionHabitacionalSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SituacionHabitacionalSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request):
        SituacionHabitacionalModel.objects.all().delete()
        return Response(data='All records has been deleted.', status=status.HTTP_410_GONE)


class SituacionHabitacionalView(APIView):

    def get_object(self, pk):
        try:
            return SituacionHabitacionalModel.objects.get(pk=pk)
        except SituacionHabitacionalModel.DoesNotExist:
            raise ValueError

    def get(self, request, pk, format=None):
        situacionHabitacional = self.get_object(pk)
        serializer = SituacionHabitacionalSerializer(situacionHabitacional)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        situacionHabitacional = self.get_object(pk)
        serializer = SituacionHabitacionalSerializer(
            situacionHabitacional, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk, format=None):
        situacionHabitacional = self.get_object(pk)
        situacionHabitacional.delete()
        return Response(data='The record has been deleted.', status=status.HTTP_410_GONE)
