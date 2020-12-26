from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, UserDetailsSerializer

from .models import User, UserDetails


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
            serializer.save()

        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def user(request, pk):
    if request.method == 'GET':
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        user = User.objects.get(id=pk)
        serializer = UserSerializer(instance=user, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    elif request.method == 'DELETE':
        user = User.objects.get(id=pk)
        user.delete()

        return Response('Item succsesfully delete!')


@api_view(['GET', 'PUT'])
def userDetails(request, pk):
    if request.method == 'GET':
        userDetails = UserDetails.objects.get(user=pk)
        serializer = UserDetailsSerializer(userDetails, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        userDetails = UserDetails.objects.get(user=pk)
        serializer = UserDetailsSerializer(instance=userDetails, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
