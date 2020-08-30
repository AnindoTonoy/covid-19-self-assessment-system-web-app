# covid-19-self-assessment-system-web-app
A simple covid-19-self-assessment-system django app which store participant's assessment score and other data in a sqlite3 database.

## Prerequisites
```bash
python== 3.8 or up and django==3.1
```
## Run
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
## To use admin panel you need to create super user using this command
```bash
python manage.py createsuperuser
```
## To run the program in local server use the following command
```bash
python manage.py runserver
```
Then go to http://127.0.0.1:8000 in your browser

## Project snapshot

### Assessment form UI - Personal data collection
![screencapture-127-0-0-1-8000-2020-08-31-00_24_31](https://user-images.githubusercontent.com/26842902/91666742-2f67c780-eb21-11ea-8dc6-4c9007b3ca06.png)

### Assessment form UI - Symptoms data Collection
![screencapture-127-0-0-1-8000-2020-08-31-00_24_51](https://user-images.githubusercontent.com/26842902/91666785-84a3d900-eb21-11ea-83e9-f711fd4c7734.png)

### Assessment form UI - Additional informations about Symptoms data Collection
![screencapture-127-0-0-1-8000-2020-08-31-00_25_44](https://user-images.githubusercontent.com/26842902/91666828-ea906080-eb21-11ea-9f10-cae7519b9e15.png)

### Admin panel - data object view - 1
![screencapture-127-0-0-1-8000-admin-home-result-2020-08-31-00_36_56](https://user-images.githubusercontent.com/26842902/91666870-435ff900-eb22-11ea-9ff8-74c2d12b7ae5.png)

### Admin panel - data object view - 2
![screencapture-127-0-0-1-8000-admin-home-result-3-change-2020-08-31-00_26_55](https://user-images.githubusercontent.com/26842902/91666890-61c5f480-eb22-11ea-85d7-61d43973d613.png)
