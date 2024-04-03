from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.utils import timezone
from django.contrib.auth import authenticate
import yfinance as yf
import time


class GetQuotesSerializer(serializers.ModelSerializer):
    currency_pair = serializers.CharField()
    period = serializers.CharField()
    interval = serializers.CharField()

    ticker = yf.Ticker(currency_pair)
    hist = ticker.history(period="1d", interval="1m")  # 1d означает "за один день", interval="1m" - интервал в одну минуту
    last_row = hist.iloc[-1]  # Получаем последнюю доступную запись

    ret

