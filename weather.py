import requests
api_key = 'b0203f25bd484ec9c5fb13ea50a634f8'

def weather():
    city = input("Enter City: ")
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}").json()
    print("=========================Weather of "+city+"=========================")
    print("Description: "+data["weather"][0]["description"].title())
    print("Lat: "+str(data["coord"]["lat"])+"; Long: "+str(data["coord"]["lon"]))
    print("Temperature: "+str(data["main"]["temp"])+"°C, feels like: "+str(data["main"]["feels_like"])+"°C")
    print("Min. Temp.: "+str(data["main"]["temp_min"])+"°C; Max. Temp.: "+str(data["main"]["temp_max"])+"°C")
    print("Pressure: "+str(data["main"]["pressure"])+" HgPa")
    print("Humidity: "+str(data["main"]["humidity"])+"%")
    print("Wind Speed: "+str(data["wind"]["speed"])+" m/s, Direction: "+degToCompass(data["wind"]["deg"]))
    print("Cloudiness: "+str(data["clouds"]["all"])+"%")
    print("*********************************************************************")

def degToCompass(num):
    val=int((num/22.5)+.5)
    arr=["N","NE","E","SE","S","SW","W","NW"]
    strr=arr[round(num/45)%8]
    return str(val)+"°"+strr
