from rest_framework import status, views
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import yfinance as yf
import json
from django.http import JsonResponse
from loguru import logger


class CurrencyQuoteAPIView(views.APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='currency-pair',
                in_=openapi.IN_HEADER,
                description="Валюта-Валюта",
                type=openapi.TYPE_STRING,
                required=True
            ),
            openapi.Parameter(
                name='period',
                in_=openapi.IN_HEADER,
                description="Период (К примеру: 1d)",
                type=openapi.TYPE_STRING,
                required=True
            ),
            openapi.Parameter(
                name='interval',
                in_=openapi.IN_HEADER,
                description="Интервал (К примеру: 1m)",
                type=openapi.TYPE_STRING,
                required=True
            ),
        ]
    )
    def get(self, request, *args, **kwargs):

        logger.debug(request.headers)

        currency_pair: str = request.headers.get('currency-pair')
        period: str = request.headers.get('period')
        interval: str = request.headers.get('interval')

        if not all([currency_pair, period, interval]):
            return Response({"error": "Отсутствует один из обязательных заголовков: currency_pair, period, interval."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            ticker = yf.Ticker(currency_pair.upper()+'=X')
            hist = ticker.history(period=period, interval=interval)
            currency = ticker.info['currency']
            name = ticker.info['longName']
            last_row = hist.iloc[-1].to_dict()  # Преобразуем последнюю запись в словарь
            last_row['Name'] = name
            last_row['Currency'] = currency

            new_currency_pair = currency_pair[3:] + currency_pair[:3]

            ticker = yf.Ticker(new_currency_pair.upper())
            hist = ticker.history(period=period, interval=interval)
            currency = ticker.info['currency']
            name = ticker.info['longName']
            new_last_row = hist.iloc[-1].to_dict()  # Преобразуем последнюю запись в словарь
            new_last_row['Name'] = name
            new_last_row['Currency'] = currency

            end_dict = {f'{currency_pair}': last_row, f'{new_currency_pair}': new_last_row}

            return JsonResponse(end_dict)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CryptoCurrencyQuoteAPIView(views.APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='crypto-currency-pair',
                in_=openapi.IN_HEADER,
                description="Криптовалюта-Валюта",
                type=openapi.TYPE_STRING,
                required=True
            ),
            openapi.Parameter(
                name='period',
                in_=openapi.IN_HEADER,
                description="Период (К примеру: 1d)",
                type=openapi.TYPE_STRING,
                required=True
            ),
            openapi.Parameter(
                name='interval',
                in_=openapi.IN_HEADER,
                description="Интервал (К примеру: 1m)",
                type=openapi.TYPE_STRING,
                required=True
            ),
        ]
    )
    def get(self, request, *args, **kwargs):

        logger.debug(request.headers)

        crypto_currency_pair: str = request.headers.get('crypto-currency-pair')
        period: str = request.headers.get('period')
        interval: str = request.headers.get('interval')

        if not all([crypto_currency_pair, period, interval]):
            return Response({"error": "Отсутствует один из обязательных заголовков: currency_pair, period, interval."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            crypto_currency_pair = crypto_currency_pair[:3].upper() + '-' + crypto_currency_pair[3:].upper()

            ticker = yf.Ticker(crypto_currency_pair)
            hist = ticker.history(period=period, interval=interval)
            currency = ticker.info['currency']
            name = ticker.info['longName']
            last_row = hist.iloc[-1].to_dict()  # Преобразуем последнюю запись в словарь
            last_row['Name'] = name
            last_row['Currency'] = currency

            end_dict = {f'{crypto_currency_pair}': last_row}

            return JsonResponse(end_dict)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class StockQuoteAPIView(views.APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='stock',
                in_=openapi.IN_HEADER,
                description="Акция",
                type=openapi.TYPE_STRING,
                required=True
            ),
            openapi.Parameter(
                name='period',
                in_=openapi.IN_HEADER,
                description="Период (К примеру: 1d)",
                type=openapi.TYPE_STRING,
                required=True
            ),
            openapi.Parameter(
                name='interval',
                in_=openapi.IN_HEADER,
                description="Интервал (К примеру: 1m)",
                type=openapi.TYPE_STRING,
                required=True
            ),
        ]
    )
    def get(self, request, *args, **kwargs):

        logger.debug(request.headers)

        stock: str = request.headers.get('stock').upper()
        period: str = request.headers.get('period')
        interval: str = request.headers.get('interval')

        if not all([stock, period, interval]):
            return Response({"error": "Отсутствует один из обязательных заголовков: stock, period, interval."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:

            ticker = yf.Ticker(stock)
            hist = ticker.history(period=period, interval=interval)
            currency = ticker.info['currency']
            name = ticker.info['longName']
            last_row = hist.iloc[-1].to_dict()  # Преобразуем последнюю запись в словарь
            last_row['Name'] = name
            last_row['Currency'] = currency

            end_dict = {f'{stock}': last_row}
            return JsonResponse(end_dict)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)