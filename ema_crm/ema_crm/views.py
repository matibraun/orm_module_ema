from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

@api_view(['GET', 'POST'])
def index(request):

    print (request.user)
    print (request.auth)
    

    if request.method == 'GET':
        return Response(data={'message': 'Hello from Django'}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        print (request.data)
        return Response(data=request.data, status=status.HTTP_200_OK)
    else:
        return Response('The method is not right')

class Message(APIView):
    def get(self, request):
        print ('Hit by Api Call')
        return Response(data='This is a class based view hit by getttt request', status=status.HTTP_200_OK)

    def post(self, request):
        print ('Hit by Post Call')
        print (request.data)
        return Response(data=request.data, status=status.HTTP_200_OK)


class Paciente()
