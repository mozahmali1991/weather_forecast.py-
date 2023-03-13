import requests

def get_weather(city):
    api_key = 'your_api_key' # замените на ваш ключ API
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        return f'Temperature: {temp}°C\nDescription: {desc}'
    else:
        return 'Error: Could not retrieve weather data.'

if __name__ == '__main__':
    city = input('Enter city name: ')
    print(get_weather(city))
