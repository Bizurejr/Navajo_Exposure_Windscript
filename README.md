# Navajo_Exposure_Windscript

---

## Weather Data Analysis Script

This Python script fetches weather data from specified stations, processes the information, and calculates the mean wind speed and mode wind direction for each station over the past two days. The script utilizes the [Iowa State University ASOS](http://mesonet.agron.iastate.edu/) service to obtain data.

### Features:

- **Data Download:**
  - Fetches weather data for selected stations.
  - Handles retries in case of download errors.

- **Data Cleaning:**
  - Cleans and preprocesses the downloaded data for further analysis.
  - Generates cleaned CSV files for each station.

- **Wind Analysis:**
  - Calculates mean wind speed and mode wind direction using trigonometric transformations.

- **Results Storage:**
  - Stores results, including date, longitude, latitude, mean wind speed, and mode wind direction, in a CSV file.

### Usage:

1. Clone the repository.
2. Run the script to fetch, clean, and analyze weather data.
3. Review the generated `combined_data.csv` for results.

### Weather Stations:

- Stations: GNT, GUP, FMN, RQE, INW, PGA, GCN, CMR, BDG, AEG, CEZ, ONM

### Dependencies:

- Python 3.x
- pandas




