from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from decouple import config

WEATHER_API_KEY = config("WEATHER_API_KEY", default=None)


def check_response_for_errors(r):
    if r.status_code == 400:
        return Response({"message": "Bad Request, check your parameters"}, status=400)
    elif r.status_code == 401:
        return Response({"message": "Internal server error while comunacting with the API"}, status=401)
    elif r.status_code == 404:
        return Response({"message": "Not endpoint found"}, status=404)
    elif r.status_code == 429:
        return Response({"message": "Too many requests"}, status=429)
    elif r.status_code == 500:
        return Response({"message": "Internal third-party server error"}, status=500)
    else:
        return Response(r.json())


@api_view(['GET'])
def get_weather_next_15_days(request: Response, country_code: str, city: str) -> Response:
    r = requests.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{
                     city},{country_code}?key={WEATHER_API_KEY}',
                     timeout=10)
    return check_response_for_errors(r)


@api_view(['GET'])
def get_weather_in_range(request: Response, country_code: str, city: str, date1, date2) -> Response:
    r = requests.get(
        f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city},{country_code}/{date1}/{date2}?key={
            WEATHER_API_KEY}',
        timeout=10
    )
    return check_response_for_errors(r)


@api_view(['GET'])
def get_weather_day_and_hour(request: requests.models.Response, country_code: str, city: str, date, hour) -> Response:
    r = requests.get(
        f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city},{country_code}/{date}T{hour}?key={
            WEATHER_API_KEY}',
        timeout=10)
    return check_response_for_errors(r)
