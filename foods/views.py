from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FoodSerializer, DailyDiarySerializer

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

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


@api_view(['GET'])
def diaries_by_user(request, pk):
    if request.method == 'GET':
        daily_diaries = DailyDiary.objects.filter(user=pk)
        serializer = DailyDiarySerializer(daily_diaries, many=True)
        return Response(serializer.data)


# @api_view(['GET'])
# def diaries_by_user_today(request, pk):
#     if request.method == 'GET':
#         daily_diary = None
#         today_diary = DailyDiary()
#         daily_diaries = DailyDiary.objects.filter(user=pk, date=today_diary.date)
#
#         if daily_diaries is None:
#             try:
#                 user_object = User.objects.get(id=pk)
#             except User.DoesNotExist:
#                 user_object = None
#             if user_object:
#                 today_diary.user = user_object
#
#                 serializer = DailyDiarySerializer(today_diary)
#
#                 if serializer.is_valid():
#                     serializer.save()
#
#                 return Response(serializer.data)
#             else:
#                 # user does not exist
#                 pass
#
#         serializer = DailyDiarySerializer(daily_diaries, many=False)
#         return Response(serializer.data)


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
