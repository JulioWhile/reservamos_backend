# Weather Forecast API

This API provides weather forecasts for cities in Mexico. It leverages the Reservamos API to fetch city data and the OpenWeather API to get weather forecasts.

## Setup

### Requirements

- Python 3.x
- Django
- Django REST framework
- Requests
- CloudsScraper

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/weather-forecast-api.git
    cd weather-forecast-api
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your OpenWeather API key:

    - Sign up on [OpenWeather](https://openweathermap.org/) to get an API key.
    - Create a `.env` file in the project root and add your OpenWeather API key:

    ```plaintext
    OPENWEATHER_API_KEY=your_openweather_api_key
    ```

5. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Get Weather Forecast

**URL:** `/api/weather/`

**Method:** `GET`

**Query Parameters:**

- `city`: The name (or part of the name) of the city to get the weather forecast for.

**Example Requests:**

1. **Monterrey**

    ```
    http://127.0.0.1:8000/api/weather/?city=Monterrey
    ```

2. **Mo**

    ```
    http://127.0.0.1:8000/api/weather/?city=Mo
    ```

3. **Guad**

    ```
    http://127.0.0.1:8000/api/weather/?city=Guad
    ```

4. **Guadalajara**

    ```
    http://127.0.0.1:8000/api/weather/?city=Guadalajara
    ```

5. **Mexico**

    ```
    http://127.0.0.1:8000/api/weather/?city=Mexico
    ```

**Response:**

The response is a JSON array containing the weather forecasts for the matching cities. Each city object includes the city name, state, country, and a forecast array with daily weather information.

**Example Response:**

```json
[
    {
        "city": "Ciudad de México",
        "state": "Distrito Federal",
        "country": "México",
        "forecast": [
            {
                "date": 1718992800,
                "min_temp": 15.54,
                "max_temp": 19.59
            },
            {
                "date": 1719079200,
                "min_temp": 15.5,
                "max_temp": 25.79
            },
            {
                "date": 1719165600,
                "min_temp": 16.64,
                "max_temp": 24.09
            },
            {
                "date": 1719252000,
                "min_temp": 15.88,
                "max_temp": 23.52
            },
            {
                "date": 1719338400,
                "min_temp": 16.34,
                "max_temp": 23.97
            },
            {
                "date": 1719424800,
                "min_temp": 16.22,
                "max_temp": 23.19
            },
            {
                "date": 1719511200,
                "min_temp": 16.54,
                "max_temp": 24.68
            },
            {
                "date": 1719597600,
                "min_temp": 16.36,
                "max_temp": 23.91
            }
        ]
    }
]
```