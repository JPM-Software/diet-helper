from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FoodSerializer, DailyDiarySerializer
from django.http import Http404
from datetime import date

from .models import Food, DailyDiary, User


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


@api_view(['GET', 'DELETE'])
def food(request, pk):
    if request.method == 'GET':
        food = Food.objects.get(id=pk)
        serializer = FoodSerializer(food, many=False)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        food = Food.objects.get(id=pk)
        food.delete()

        return Response('Item succsesfully delete!')


@api_view(['GET'])
def foods_for_diary(request, pk):
    if request.method == 'GET':
        daily_diary = DailyDiary.objects.get(id=pk)
        foods = daily_diary.foods
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def diaries(request):
    if request.method == 'GET':
        daily_diaries = DailyDiary.objects.all()
        serializer = DailyDiarySerializer(daily_diaries, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DailyDiarySerializer(data=request.data)
        print(request.data)
        print('============')
        print(serializer)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


@api_view(['GET'])
def diaries_by_user(request, pk):
    if request.method == 'GET':
        daily_diaries = DailyDiary.objects.filter(user=pk)
        serializer = DailyDiarySerializer(daily_diaries, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def diaries_by_user_today(request, pk):
    if request.method == 'GET':
        today = date.today()
        daily_diary = DailyDiary.objects.filter(user=pk).filter(date=today).first()
        if daily_diary is None:
            user_from_db = User.objects.get(id=pk)
            if user_from_db is not None:
                serializer = DailyDiarySerializer(data={'user': user_from_db.id})
                print(serializer)

                if serializer.is_valid():
                    print("Serializer is valid")
                    serializer.save()
                print("Serializer is not valid")
                return Response(serializer.data)
            raise Http404

        serializer = DailyDiarySerializer(daily_diary)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def diary(request, pk):
    if request.method == 'GET':
        daily_diary = DailyDiary.objects.get(id=pk)
        serializer = DailyDiarySerializer(daily_diary, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        daily_diary = DailyDiary.objects.get(id=pk)
        serializer = DailyDiarySerializer(instance=daily_diary, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    elif request.method == 'DELETE':
        daily_diary = DailyDiary.objects.get(id=pk)
        daily_diary.delete()

        return Response('Item succsesfully delete!')
