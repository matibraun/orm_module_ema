from django.shortcuts import render
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from crm.models import TallerModel
from crm.serializers import TallerSerializer

# Create your views here.

class TalleresView(APIView):
    def get(self, request):
        queryset = TallerModel.objects.all()
        serializer = TallerSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TallerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request):
        TallerModel.objects.all().delete()
        return Response(data='All records has been deleted.', status=status.HTTP_410_GONE)


class TallerView(APIView):

    def get_object(self, pk):
        try:
            return TallerModel.objects.get(pk=pk)
        except TallerModel.DoesNotExist:
            raise ValueError

    def get(self, request, pk, format=None):
        taller = self.get_object(pk)
        serializer = TallerSerializer(taller)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        taller = self.get_object(pk)
        serializer = TallerSerializer(
            taller, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk, format=None):
        taller = self.get_object(pk)
        taller.delete()
        return Response(data='The record has been deleted.', status=status.HTTP_410_GONE)
