from rest_framework import serializers
from .models import Food, DailyDiary


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class DailyDiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyDiary
        fields = '__all__'
        depth = 1

class DailyDiarySaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyDiary
        fields = '__all__'