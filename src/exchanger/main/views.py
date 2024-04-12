import json

import yfinance as yf
from django.http import JsonResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from loguru import logger
from rest_framework import status, views
from rest_framework.response import Response


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

        data = {
            'currency_pair': currency_pair,
            'period': period,
            'interval': interval,
        }

        if not all([currency_pair, period, interval]):
            return Response({"error": "Отсутствует один из обязательных заголовков: currency_pair, period, interval."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            ticker = yf.Ticker(currency_pair.upper() + '=X')
            hist = ticker.history(period=period, interval=interval)
            hist.reset_index(inplace=True)
            currency = ticker.info['currency']
            name = ticker.info['longName']
            json_data = hist.to_json(orient='records', date_format='iso')
            data_list = json.loads(json_data)

            end_dict = {'info': {
                'name': name,
                'currency': currency
            },
                'data': data_list
            }

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
            hist.reset_index(inplace=True)
            currency = ticker.info['currency']
            name = ticker.info['longName']
            json_data = hist.to_json(orient='records', date_format='iso')
            data_list = json.loads(json_data)

            end_dict = {'info': {
                'name': name,
                'currency': currency
            },
                'data': data_list
            }
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
            hist.reset_index(inplace=True)
            currency = ticker.info['currency']
            name = ticker.info['longName']
            json_data = hist.to_json(orient='records', date_format='iso')
            data_list = json.loads(json_data)

            end_dict = {'info': {
                'name': name,
                'currency': currency
            },
                'data': data_list
            }
            return JsonResponse(end_dict)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TestAPIView(views.APIView):
    @logger.catch()
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
                description="Период - длительность диапазона. "
                            "К примеру 30d означает от текщуего дня до этого же дня месяц назад.",
                type=openapi.TYPE_STRING,
                required=True
            ),
            openapi.Parameter(
                name='interval',
                in_=openapi.IN_HEADER,
                description="Интервал - ограничение на внутридневные данные. "
                            "К примеру период в 30d с интервалом 5d выведет 6 записей "
                            "с разницей в 5 дней сежду каждой.",
                type=openapi.TYPE_STRING,
                required=True
            ),
        ]
    )
    def get(self, request, *args, **kwargs):

        logger.debug(request.body)
        logger.debug(request.headers)

        currency_pair: str = request.headers.get('currency-pair')
        period: str = request.headers.get('period')
        interval: str = request.headers.get('interval')

        data = {
            'currency_pair': currency_pair,
            'period': period,
            'interval': interval,
        }

        if not all([currency_pair, period, interval]):
            return Response({"error": "Отсутствует один из обязательных заголовков: currency_pair, period, interval."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            ticker = yf.Ticker(currency_pair.upper() + '=X')
            hist = ticker.history(period=period, interval=interval)
            hist.reset_index(inplace=True)
            currency = ticker.info['currency']
            name = ticker.info['longName']
            json_data = hist.to_json(orient='records', date_format='iso')
            data_list = json.loads(json_data)

            end_dict = {'info': {
                'name': name,
                'currency': currency
            },
                'data': data_list
            }

            response = JsonResponse(end_dict, status=status.HTTP_200_OK)
            response['Access-Control-Allow-Origin'] = '*'
            response['Access-Control-Allow-Headers'] = 'Content-Type, currency-pair, period, interval, ngrok-skip-browser-warning'

            return response
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
