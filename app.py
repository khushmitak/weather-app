from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)

@app.route('/')
def index():
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    city = 'Las Vegas'
    
    r = requests.get(url.format(city)).json()
    print(r)
    
    weather = {
        'city' : city,
        'temperature' : ,
        'description' : ,
        'icon' : ,
    }
    
    return render_template('weather.html')