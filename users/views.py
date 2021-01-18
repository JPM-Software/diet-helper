from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, UserDetailsSerializer

from .models import User, UserDetails

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status


# Create your views here.
@api_view(['GET', 'POST'])
def users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user_login = request.data['login']

            user = User.objects.filter(login=user_login).first()

            if user is not None:
                return Response({'message': 'Login jest zajety'}, status=status.HTTP_409_CONFLICT)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user(request, pk):
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        return Response({'message': 'Uzytkownik nie istnieje'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(instance=user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response({'message': 'Uzytkownik zostal pomyslnie usuniety'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def userLogin(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            login = request.data['login']
            user = User.objects.filter(login=login).first()

            if user is None:
                return Response({'message': 'Uzytkownik nie istnieje'}, status=status.HTTP_404_NOT_FOUND)

            password = request.data['password']
            if user.password == password:
                userToReturn = UserSerializer(user, many=False)
                return Response(userToReturn.data, status=status.HTTP_200_OK)

            return Response({'message': 'Podane dane sa nieprawidlowe'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'message': 'Przeslany JSON jest niepoprawny'}, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def userDetails(request, pk):
    try:
        userDetails = UserDetails.objects.get(user=pk)
    except UserDetails.DoesNotExist:
        return Response({'message': 'Brak danych uzytkownika'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserDetailsSerializer(userDetails, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserDetailsSerializer(instance=userDetails, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
