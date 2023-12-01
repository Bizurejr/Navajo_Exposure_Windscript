
# Weather Data Analysis Script

This Python script fetches weather data from specified stations, processes the information, and calculates the mean wind speed and mode wind direction for each station over the past two days. The script utilizes the Iowa State University ASOS service to obtain data.

## Features

### Data Download

- Fetches weather data for selected stations.
- Handles retries in case of download errors.

### Data Cleaning

- Cleans and preprocesses the downloaded data for further analysis.
- Generates cleaned CSV files for each station.

### Wind Analysis

- Calculates mean wind speed and mode wind direction using trigonometric transformations.

### Flask REST API with Celery Integration

- Implements a Flask REST API for triggering and enqueuing wind analysis tasks.
- Uses Celery for asynchronous execution of wind analysis logic.
- Background task can be triggered through the `/run-wind-analysis` API endpoint.

### Results Storage

- Stores results, including date, longitude, latitude, mean wind speed, and mode wind direction, in a CSV file.

## Usage

1. Clone the repository.
2. Run the script to fetch, clean, and analyze weather data.
3. Review the generated `combined_data.csv` for results.

## Weather Stations

Stations: GNT, GUP, FMN, RQE, INW, PGA, GCN, CMR, BDG, AEG, CEZ, ONM

## Dependencies

- Python 3.x
- pandas

## Flask REST API Configuration

The repository now includes a Flask REST API with Celery integration. To use it:

1. Install required dependencies using `pip install -r requirements.txt`.
2. Ensure RabbitMQ is installed and running.
3. Run the Flask app using `python run_restapi.py`.
4. Access the Flask API at `http://127.0.0.1:5000/`.

To enqueue a wind analysis task, visit `http://127.0.0.1:5000/run-wind-analysis`.

