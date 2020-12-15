from django.shortcuts import render
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from crm.models import ReunionModel
from crm.serializers import ReunionSerializer

# Create your views here.

class ReunionesView(APIView):
    def get(self, request):
        queryset = ReunionModel.objects.all()
        serializer = ReunionSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ReunionSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        ReunionModel.objects.all().delete()
        return Response(data='All Deleted', status=status.HTTP_410_GONE)

class ReunionView(APIView):

    def get_object(self, pk):
        try:
            return ReunionModel.objects.get(pk=pk)
        except ReunionModel.DoesNotExist:
            raise ValueError

    def get(self, request, pk, format=None):
        reunion = self.get_object(pk)
        serializer = ReunionSerializer(reunion)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        reunion = self.get_object(pk)
        serializer = ReunionSerializer(reunion, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        reunion = self.get_object(pk)
        reunion.delete()
        return Response(data='Delete', status=status.HTTP_410_GONE)
