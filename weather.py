import requests
from datetime import datetime
import os.path

api_key = '232e496e736fbc317149531b56fcc3a6'
location = input("Enter your Location : ")

full_api_link = 'https://api.openweathermap.org/data/2.5/weather?q='+location+'&appid='+api_key
api_link = requests.get(full_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_des = api_data['weather'][0]['description']
hmdty = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print('---------------------------------------------------------------------------')
print("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print('---------------------------------------------------------------------------')

print("Current Temperature is : {:.2f} deg Celsius".format(temp_city))
print("Current Weather Description : {}".format(weather_des))
print("Current Humidity : {}% :".format(hmdty))
print("Current Wind Speed : {} Kmph".format(wind_spd))

content = "---------------------------------------------------------------------------\nWeather Stats for - {}  || {" \
          "}\n---------------------------------------------------------------------------\nCurrent Temperature is : {" \
          ":.2f} deg Celsius\nCurrent Weather Description : {}\nCurrent Humidity : {}% :\nCurrent Wind Speed : {} Kmph\n".format(location.upper(), date_time, temp_city, weather_des, hmdty, wind_spd)


if os.path.isfile("./Reports.txt"):
    append_file = '\n'+content
    f = open("Reports.txt", 'a')
    f.write(append_file)
    f.close()
    print("Added Report in  Reports.txt ")
else:
    f = open("Reports.txt", 'w')
    f.write(content)
    f.close()
    print("Created Reports.txt and Added Report ")

print('Note : The Reports will be added in Report.txt Whenever you Run This Program ')
