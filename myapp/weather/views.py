from django.shortcuts import render
import requests
import os
from .models import City
from .forms import CityForm



api_key = os.getenv('api_key_weather') 
lat = "55.181950"
lon = "-2.810358"
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)

def index(request):
    # form = CityForm()
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=apikey'
    cities = City.objects.all() #return all the cities in the database

    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate

    form = CityForm()

    weather_data = []

    for city in cities:

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
        
        # print(city, city_weather )

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather) #add the data for the current city into our list

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'weather/index.html', context) #returns the index.html template