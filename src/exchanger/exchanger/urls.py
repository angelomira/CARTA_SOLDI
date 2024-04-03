from django.urls import path, re_path
from drf_yasg.views import get_schema_view
from auth.views import UserRegistrationView, UserLoginView
from main.views import (
    CurrencyQuoteAPIView,
    CryptoCurrencyQuoteAPIView,
    StockQuoteAPIView
)
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API documentation for my project",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user_register'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('currency-quote/', CurrencyQuoteAPIView.as_view(), name='currency_quote'),
    path('crypto-currency-quote/', CryptoCurrencyQuoteAPIView.as_view(), name='crypto_currency_quote'),
    path('stock-quote/', StockQuoteAPIView.as_view(), name='stock_quote'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
