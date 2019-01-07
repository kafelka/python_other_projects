#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 14:22:09 2019

@author: mag
"""
from bs4 import BeautifulSoup
import requests
from datetime import datetime

def selectDate(location):
    isDate = int(input("Select a date: 0 - today, 1 - tomorrow, 2 - day after tomorrow, n - nth day in advance. "))
    if isDate == 0:
        return f'https://www.bbc.co.uk/weather/{location}'
    else:
        return f'https://www.bbc.co.uk/weather/{location}/day{isDate}' 
    
    
def selectCity():
    city = input("Search city or postcode: ")
    r = requests.get(f"https://www.bbc.co.uk/weather/0/search?s={city}")
    soup = BeautifulSoup(r.text, 'html.parser')
    selectedCity = soup.find("a", {"class": "location-search-results__result__link"})
    return selectedCity["href"]
    
    
def parseHour(html):
    hour = html.find("span", {"class": "wr-time-slot-primary__hours"})
    temperature = html.find("span", {"class": "wr-value--temperature--c"})
    weatherDetailed = html.find("span", {"class": "wr-time-slot-secondary__weather-type-text"})
    weatherType = html.find("div", {"class": "wr-time-slot-primary__weather-type-description"})
    precipitation = html.find("div", {"class": "wr-time-slot-primary__precipitation"}).children
    wind_kph = html.find("span", {"class": "wr-value--windspeed wr-value--windspeed--kph"})
    windDirection = html.find("div", {"class": "wr-time-slot-secondary__wind-direction"})
    return {
        "time": hour.text,
        "details": weatherDetailed.text,
        "temperature": temperature.text,
        "weather type": weatherType.text,
        "precipitation": list(precipitation)[1].text.split("c")[0],
        "wind": wind_kph.text,
        "wind details": windDirection.text
    }


if __name__ == "__main__":
    locationID = selectCity()
    url = selectDate(locationID)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    li = soup.find_all("li", {"class": "wr-time-slot wr-js-time-slot "})
    
    for item in li:
        print(parseHour(item))

