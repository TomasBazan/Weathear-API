from decouple import config

WEATHER_API_KEY = config("WEATHER_API_KEY", default=None)
WEATHER_API_URL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
