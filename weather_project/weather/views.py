import cloudscraper
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
import logging

logger = logging.getLogger(__name__)

RESERVAMOS_API_URL = "https://search.reservamos.mx/api/v2/places"
OPENWEATHER_API_URL = "https://api.openweathermap.org/data/2.5/onecall"
OPENWEATHER_API_KEY = "a5a47c18197737e8eeca634cd6acb581"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}


@api_view(['GET'])
def get_weather_forecast(request):
    city_name = request.query_params.get('city')
    if not city_name:
        raise ValidationError("City name is required")

    try:
        with cloudscraper.create_scraper() as scraper:
            reservamos_params = {'term': city_name, 'country': 'México'}
            reservamos_response = scraper.get(RESERVAMOS_API_URL, params=reservamos_params, headers=HEADERS)
            reservamos_response.raise_for_status()
            cities = reservamos_response.json()

        filtered_cities = [
            city for city in cities
            if city_name.lower() in city.get('city_name', '').lower() and
               city.get('country', '').lower() == 'méxico' and
               'lat' in city and 'long' in city
        ]

        if not filtered_cities:
            raise ValidationError("No cities found matching the query in México")

        results = []
        unique_cities = set()

        for city in filtered_cities:
            city_key = (city['city_name'].lower(), city['state'].lower())
            if city_key not in unique_cities:
                openweather_params = {
                    'lat': city['lat'],
                    'lon': city['long'],
                    'exclude': 'current,minutely,hourly,alerts',
                    'appid': OPENWEATHER_API_KEY,
                    'units': 'metric'
                }

                openweather_response = requests.get(OPENWEATHER_API_URL, params=openweather_params)
                openweather_response.raise_for_status()

                weather_data = openweather_response.json()
                forecast = [
                    {
                        "date": day["dt"],
                        "min_temp": day["temp"]["min"],
                        "max_temp": day["temp"]["max"]
                    }
                    for day in weather_data.get('daily', [])
                ]

                results.append({
                    "city": city['city_name'],
                    "state": city.get('state', ''),
                    "forecast": forecast
                })
                unique_cities.add(city_key)
        return Response(results)

    except requests.exceptions.RequestException as e:
        logger.exception("Error fetching data from external API: %s", e)
        raise
    except ValidationError as e:
        return Response({'error': e.detail}, status=400)
    except Exception as e:
        logger.exception("Internal server error: %s", e)
        raise
