from django.shortcuts import render
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from crm.models import ComposicionFamiliarModel
from crm.serializers import ComposicionFamiliarSerializer


# Create your views here.

class ComposicionesFamiliaresView(APIView):
    def get(self, request):
        queryset = ComposicionFamiliarModel.objects.all()
        serializer = ComposicionFamiliarSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ComposicionFamiliarSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        ComposicionFamiliarModel.objects.all().delete()
        return Response(data='All Deleted', status=status.HTTP_410_GONE)

class ComposicionFamiliarView(APIView):

    def get_object(self, pk):
        try:
            return ComposicionFamiliarModel.objects.get(pk=pk)
        except ComposicionFamiliarModel.DoesNotExist:
            raise ValueError

    def get(self, request, pk, format=None):
        composicionFamiliar = self.get_object(pk)
        serializer = ComposicionFamiliarSerializer(composicionFamiliar)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        composicionFamiliar = self.get_object(pk)
        serializer = ComposicionFamiliarSerializer(composicionFamiliar, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        composicionFamiliar = self.get_object(pk)
        composicionFamiliar.delete()
        return Response(data='Delete', status=status.HTTP_410_GONE)