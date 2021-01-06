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
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        SituacionHabitacionalModel.objects.all().delete()
        return Response(data='All Deleted', status=status.HTTP_410_GONE)

class SituacionHabitacionalView(APIView):

    def get_object(self, pk):
        try:
            return SituacionHabitacionalModel.objects.get(pk=pk)
        except SituacionHabitacionalModel.DoesNotExist:
            raise ValueError

    def get(self, request, pk, format=None):
        situacionHabitacional = self.get_object(pk)
        serializer = SituacionHabitacionalSerializer(situacionHabitacional)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        situacionHabitacional = self.get_object(pk)
        serializer = SituacionHabitacionalSerializer(situacionHabitacional, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        situacionHabitacional = self.get_object(pk)
        situacionHabitacional.delete()
        return Response(data='Delete', status=status.HTTP_410_GONE)