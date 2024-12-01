## Description
This is a personal project to learn how to use cache and redis, the idea is to ask to a third party API for the information and store the responses from the Third party API to reproduce the situation where I would like to reduce latency and possibles costs.

## Requirements
- Python 3.12.3+
- Pip 24.0
- Docker version 27.3.1
- docker-compose version 1.29.2

## Usage
- Clone repository
```bash
git clone 
```
- Activate the environment
```bash
source venv/bin/activate
```
- Execute redis image
```bash
docker-compose up -d
```
- run executable
```bash
python manage.py runserver
```

## Query accepted
home-page/weather/<parameters>
where parameters can take differents shapes:
- If you want to check the next two weeks you can use <parameters> as Country-Code/City-Name
- If you want to check a specific range of days you can use <parameters> as Country-Code/City-Name/YYYY-MM-DD/YYY-MM-DD (where the first date correspond to the start and the second one to the end)
- If you want to check for a specific hour you can use <parameters> as Country-Code/City-Name/YYY-MM-DD/HH:MM:SS (the hour must be in the 24 hours format)