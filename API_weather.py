import requests
import time
import sched
import json
import csv
from datetime import datetime


while(1):
    url = 'http://api.openweathermap.org/data/2.5/weather?id=1261481&APPID=a1a98e4e5f70f02ddb5ea6df28f36a2f&units=metric'
    page = requests.get(url)
    jsonstr = page.content.decode("utf-8")
    # csv_file=open('WeatherData.json','a')
    # csv_file.write(page.content.decode("utf-8"))
    # csv_file.close()
    parsed_json = json.loads(jsonstr)
    csvw = open('weather.csv', 'a',newline="")

    # create the csv writer object

    csvwriter = csv.writer(csvw)

    count = 0

    print(parsed_json["coord"])


    dt = (datetime.fromtimestamp(parsed_json["dt"]))
    print(dt)
    ''' csvwriter.writerow(["date-time" , "humidity", "temp" , "visibility" , "WindSpeed", "Pressure"]) '''
    csvwriter.writerow([dt,parsed_json["main"]["humidity"], parsed_json["main"]["temp"], parsed_json["visibility"], parsed_json["wind"]["speed"], parsed_json["main"]["pressure"]])
    print("written")

    
    csvw.close()

    time.sleep(60)



