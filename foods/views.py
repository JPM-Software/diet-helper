from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import FoodSerializer, DailyDiarySerializer, DailyDiarySaveSerializer
from django.http import Http404
from datetime import date
from django.utils.dateparse import parse_date

from .models import Food, DailyDiary, User
from rest_framework.parsers import JSONParser


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
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def food(request, pk):
    try:
        food = Food.objects.get(id=pk)
    except Food.DoesNotExist:
        return Response({'message': 'Posilek nie istnieje'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FoodSerializer(food, many=False)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        food.delete()
        return Response({'message': 'Posilek zostal pomyslnie usuniety'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def foods_for_diary(request, pk):
    if request.method == 'GET':
        daily_diary = DailyDiary.objects.get(id=pk)
        if daily_diary is None:
            return Response({'message': 'Dziennik nie istnieje'}, status=status.HTTP_404_NOT_FOUND)
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
        serializer = DailyDiarySaveSerializer(data=request.data)

        if serializer.is_valid():

            user_id = request.data['user']
            date_str = request.data['date']
            date_parsed = parse_date(date_str)
            daily_diary = DailyDiary.objects.filter(user=user_id).filter(date=date_parsed).first()

            if daily_diary is not None:
                return Response({'message': 'Istnieje juz dziennik dla tego uzytkownika w tym dniu'},
                                status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


@api_view(['GET'])
def diaries_by_user(request, pk):
    if request.method == 'GET':
        daily_diaries = DailyDiary.objects.filter(user=pk)
        if daily_diaries is None:
            return Response({'message': 'Brak dziennikow dla tego uzytkownika'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DailyDiarySerializer(daily_diaries, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def diaries_by_user_today(request, pk):
    if request.method == 'GET':
        today = date.today()
        daily_diary = DailyDiary.objects.filter(user=pk).filter(date=today).first()
        if daily_diary is None:
            try:
                user_from_db = User.objects.get(id=pk)
            except User.DoesNotExist:
                return Response({'message': 'Uzytkownik o podanym id nie zostal odnaleziony'},
                                status=status.HTTP_404_NOT_FOUND)

            serializer = DailyDiarySaveSerializer(data={'user': user_from_db.id})

            if serializer.is_valid():
                serializer.save()
                id = serializer.data['id']
                try:
                    daily_diary = DailyDiary.objects.get(id=id)
                except DailyDiary.DoesNotExist:
                    return Response({'message': 'Nieokreslony blad podczas tworzenia dziennika'},
                                    status=status.HTTP_400_BAD_REQUEST)

                serializer_response = DailyDiarySerializer(daily_diary, many=False)
                return Response(serializer_response.data)

        serializer = DailyDiarySerializer(daily_diary)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def diary(request, pk):
    try:
        daily_diary = DailyDiary.objects.get(id=pk)
    except DailyDiary.DoesNotExist:
        return Response({'message': 'Dziennik nie istnieje'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DailyDiarySerializer(daily_diary, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DailyDiarySaveSerializer(instance=daily_diary, data=request.data)

        if serializer.is_valid():
            user_id = request.data['user']
            if user_id is None:
                return Response({'message': 'Podaj obecnego uzytkownika'}, status=status.HTTP_400_BAD_REQUEST)
            if user_id != daily_diary.user.id:
                return Response({'message': 'Id usera sie nie zgadza'}, status=status.HTTP_400_BAD_REQUEST)
            date_str = request.data['date']
            if date_str is None:
                return Response({'message': 'Podaj obecna date'}, status=status.HTTP_400_BAD_REQUEST)
            date_parsed = parse_date(date_str)
            if date_parsed == daily_diary.date:
                serializer.save()
                return Response(serializer.data)

            return Response({'message': 'Data musi pozostac niezmieniona'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        daily_diary.delete()
        return Response({'message': 'Dziennik zostal pomyslnie usuniety'}, status=status.HTTP_204_NO_CONTENT)
