import wiotp.sdk.device
import time
import random
import requests, json
myConfig = { 
    "identity": {
        "orgId": "n8qnr4",
        "typeId": "ESP32",
        "deviceId":"90596"
    },
    
    "auth": {
        "token": "@07102001"
    }
}
api_key = "902856e07c32938df0024a47e76f9ae4"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name : ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)
x = response.json()
def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']


client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
   if x["cod"] != "404":
  
    # store the value of "main"
    # key in variable y
        y = x["main"]
  
    # store the value corresponding
    # to the "temp" key of y
        current_temperature = y["temp"]
  
    # store the value corresponding
    # to the "pressure" key of y
        current_pressure = y["pressure"]
      
    # store the value corresponding
    # to the "humidity" key of y
        current_humidity = y["humidity"]
  
    # store the value of "weather"
    # key in variable z
        z = x["weather"]
  
    # store the value corresponding 
    # to the "description" key at 
    # the 0th index of z
        weather_description = z[0]["description"]
    #storing value corresponding to visibility
        visibility=x["visibility"]
        
    
        myData={'temperature':current_temperature, 'humidity':current_humidity, 'description':weather_description, 'visibility':visibility }
        client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
        print("Published data Successfully: %s", myData)
        client.commandCallback = myCommandCallback
        time.sleep(2)
client.disconnect()
