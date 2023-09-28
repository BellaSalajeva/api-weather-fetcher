# Need a module that will allow to send a request to the API
# Will hit a url on remote server, will give us data
import requests

API_KEY = "31418b5fd387b79e407a8f0d13c11174"
BASE_URL = "https://api.openweathermap.org/data/2.5/"

city = input("\nEnter a city name: ")
task = input("Would you like to know the current weather(current), the daily forecast for 5day/3hour(forecast), or air pollution(air pollution): ").lower()

if task == "current":
    request_url = f"{BASE_URL}weather?appid={API_KEY}&q={city}&units=metric"
    response = requests.get(request_url)
    # Code 200 means success
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        weather = data['weather'][0]['description']
        wind = data['wind']['speed']
        #gust = data['wind']['gust']
        cloudiness = data['clouds']['all']
        humidity = data['main']['humidity']
        visibility = data['visibility']
    
        print("\n")
        print("Temperature:", temperature, "Celsius")
        print("Weather:", weather)
        print("Wind:", wind, "m/s")
        #print("Wind:", wind, "m/s, with gusts of", gust, "m/s.")
        print("Cloudiness:", cloudiness, "%")
        print("Humidity:", humidity, "%")
        print("Visibility:", visibility, "metres ahead.")       
    else:
        print("An error occurred. The error code is ", response.status_code)

elif task == "forecast":
    requests_url_forecast = f"{BASE_URL}forecast?appid={API_KEY}&q={city}&units=metric"
    response = requests.get(requests_url_forecast)

    if response.status_code == 200:
        data = response.json()
        for i in range(40):
            date_time = data['list'][i]['dt_txt']
            temperature = data['list'][i]['main']['temp']
            weather = data['list'][i]['weather'][0]['description']
            wind = data['list'][i]['wind']['speed']
            gust = data['list'][i]['wind']['gust']
            cloudiness = data['list'][i]['clouds']['all']
            humidity = data['list'][i]['main']['humidity']
            visibility = data['list'][i]['visibility']
        
            print("\n")
            print("Date and Time:", date_time)
            print("Temperature:", temperature, "Celsius")
            print("Weather:", weather)
            print("Wind:", wind, "m/s, with gusts of", gust, "m/s.")
            print("Cloudiness:", cloudiness, "%")
            print("Humidity:", humidity, "%")
            print("Visibility:", visibility, "metres ahead.")       
    else:
        print("An error occurred. The error code is ", response.status_code)

elif task == "air pollution":
    requests_url_air_pollution = f"{BASE_URL}air_pollution?appid={API_KEY}&lat=50&lon=50"
    response = requests.get(requests_url_air_pollution)

    if response.status_code == 200:
        data = response.json()
        aqi = data['list'][0]['main']['aqi']

        
        air_quality = ""
        if aqi == 1:
            air_quality = "Good"
        elif aqi == 2:
            air_quality = "Fair"
        elif aqi == 3:
            air_quality = "Moderate"
        elif aqi == 4:
            air_quality = "Poor"
        elif aqi == 5:
            air_quality = "Very Poor"
        else:
            print("Bug getting aqi")
        print(f"Air Quality Index is {aqi}. This means the air quality is {air_quality}.")

        components = input("Would you like to know the pollutant concentration (μg/m^3)? ").lower()

        if components == "yes":
            pollutant = data['list'][0]['components']
            for poll in pollutant.keys():
                print(poll, ":", pollutant[poll])
        else: print("Pollutant composition not wanted")

    else:
        print("An error occurred. The error code is ", response.status_code)
        
else:
    print("Error. Please enter your answer again.")



