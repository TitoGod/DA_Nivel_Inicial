# Importar las librerías necesarias.

import requests
import pandas as pd
from pandas import json_normalize
from datetime import datetime
from config import password

def get_weather_data(city, coords):
    """Esta función busca los datos de las ciudades y 
    coordenadas que se le pasa por parámetro y los guarda
    en un archivo con formato csv"""

    # Endpoint de OpenWeatherMap:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    api_key = password

    # La URL completa con las coordenadas:
    url = f"{BASE_URL}{coords}&appid={api_key}"

    # Realizar la una solicitud HTTP a la API:
    response = requests.get(url)
    
    # Verificar si la solicitud fue exitosa:
    if response.status_code == 200:
        data = response.json()
        # Convertir los datos JSON a un DataFrame de pandas:
        df = json_normalize(data)
    
    else:
        print(f"No se pudieron obtener los datos del clima de {city}")

    # Obtener la fecha actual para utilizarla en el nombre del archivo CSV:
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Definir la ruta y nombre del archivo CSV donde se almacenarán los datos:
    file_path = f"weather_data/{city.lower()}_{current_date}.csv".replace(" ", "_")

    # Guardas los datos en formato CSV:
    with open(file_path, 'w') as output_file:
        df.to_csv(output_file, index=False)

    return 1


# Ciudades y coordenadas:
cityList = ["London", "New York", "Cordoba", "Taipei", "Buenos Aires", "Mexico DF", "Dublin", "Tilfis", "Bogota", "Tokio"]
coordList = ["lat=31&lon=64", "lat=40&lon=-73", "lat=-31&lon=-64", "lat=25&lon=64", "lat=-34&lon=-58", "lat=19&lon=-99", "lat=53&lon=6", "lat=41&lon=44", "lat=4&lon=74", "lat=35&lon=139"]

# Ejecución:

if __name__ == "__main__":
    for city, coords in zip(cityList, coordList):
        get_weather_data(city, coords)