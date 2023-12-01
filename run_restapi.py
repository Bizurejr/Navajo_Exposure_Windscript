from flask import Flask, jsonify
from celery import Celery
from celery.result import AsyncResult
from wind_script import fetch_weather_data   

app = Flask(__name__)

 
app.config['CELERY_BROKER_URL'] = 'pyamqp://guest:guest@localhost//'
app.config['CELERY_RESULT_BACKEND'] = 'rpc://'
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@app.route('/')
def index():
    return 'Flask REST API with Celery'

@app.route('/run-wind-analysis')
def run_wind_analysis():
    # Enqueue the background task
    background_wind_analysis.delay()
    return jsonify({"message": "Wind analysis task enqueued"})

@celery.task
def background_wind_analysis():
    #this function is from the wind_script.py file, we are basically calling
    #on it
    fetch_weather_data()
    print("Wind analysis task completed")
    
    #Summary of this api:Implemented a Flask REST API with Celery integration for asynchronous wind analysis tasks. 
    # The API includes routes to trigger and enqueue background tasks using Celery. 
    # The wind analysis logic, defined in the 'wind_script.py' file, is imported and executed asynchronously through Celery workers. 
    # Configuration settings for Celery include using RabbitMQ as the message broker.
    #resources " Tech With Tim Python REST API Tutorial - Building a Flask REST API"
    #link https://youtu.be/GMppyAPbLYk?si=Di9rVLWpZJk5LIvl

