from django.urls import path, re_path
from .views import get_weather_next_15_days, get_weather_day_and_hour, get_weather_in_range

DATE_REGEX = r'\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$'


urlpatterns = [
    path('weather/<str:country_code>/<str:city>',
         get_weather_next_15_days, name='get_15_days_weather'),
    re_path(r'^weather/(?P<country_code>\w{2,3})/(?P<city>\w+)/(?P<date1>\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))/(?P<date2>\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))$',
            get_weather_in_range,
            name='get_weather_in_range'),
    re_path(r'^weather/(?P<country_code>\w{2,3})/(?P<city>\w+)/(?P<date>\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))/(?P<hour>([0-1]?[0-9]|2[0-3]):([0-5]?[0-9]):([0-5]?[0-9]))$',
            get_weather_day_and_hour, name='get_weather_day_and_hour'),
]
