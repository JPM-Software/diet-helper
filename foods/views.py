from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FoodSerializer

from .models import Food


# Create your views here.
@api_view(['GET', 'POST'])
def foods(request):
    if request.method == 'GET':
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FoodSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def food(request, pk):
    if request.method == 'GET':
        food = Food.objects.get(id=pk)
        serializer = FoodSerializer(food, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        food = Food.objects.get(id=pk)
        serializer = FoodSerializer(instance=food, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    elif request.method == 'DELETE':
        food = Food.objects.get(id=pk)
        food.delete()

        return Response('Item succsesfully delete!')
