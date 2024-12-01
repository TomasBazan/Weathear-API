from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from django.core.cache import cache
import requests
from .utils import check_response_for_errors
from .constants import WEATHER_API_KEY, WEATHER_API_URL


@api_view(['GET'])
def get_weather_next_15_days(request: Response,
                             country_code: str,
                             city: str
                             ) -> Response:

    r = requests.get(f'{WEATHER_API_URL}{city},{country_code}?key={
        WEATHER_API_KEY}',
        timeout=10)
    return check_response_for_errors(r)


@api_view(['GET'])
def get_weather_in_range(request: Response,
                         country_code: str,
                         city: str,
                         date1,
                         date2
                         ) -> Response:
    r = requests.get(
        f'{WEATHER_API_URL}{city},{country_code}/{date1}/{date2}?key={
            WEATHER_API_KEY}',
        timeout=10
    )
    return check_response_for_errors(r)


@api_view(['GET'])
def get_weather_day_and_hour(request: requests.models.Response,
                             country_code: str,
                             city: str,
                             date,
                             hour
                             ) -> Response:
    r = requests.get(
        f'{WEATHER_API_URL}{city},{country_code}/{date}T{hour}?key={
            WEATHER_API_KEY}',
        timeout=10)
    return check_response_for_errors(r)
