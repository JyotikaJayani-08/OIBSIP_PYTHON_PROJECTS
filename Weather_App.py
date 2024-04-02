import requests  #Library for making HTTP requests
api_key = 'f5e9379c260563dfa07cd26c12d024aa'  #using API

user_input = input("Enter the city:")
# print(user_input)
weather_data = requests.get(
     f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
# print(weather_data.status_code)
# print(weather_data.json())

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    # print(weather,temp)
    print(f"The weather in {user_input} is : {weather}")
    print(f"The temperature in {user_input} is {temp}ºF")





