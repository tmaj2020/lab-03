import requests
from typing import Dict

# connect to a "real" API

## Example: OpenWeatherMap
URL = "https://api.openweathermap.org/data/2.5/weather"

# TODO: get an API key from openweathermap.org and fill it in here!
API_KEY = "2f09f5434cbeb9330cc94f0f8f767dd8"

def get_weather(city) -> Dict:
    res = requests.get(URL, params={"q": city, "appid": API_KEY})
    return res.json()

# TODO: try connecting to a another API! e.g. reddit (https://www.reddit.com/dev/api/)

#Attempt 1: Here I try to practice by using a publicly available api, in this case, the catfact api
CATAPI = "https://catfact.ninja/fact"
def get_cat_fact():
	res = requests.get(CATAPI)
	return res.json()

#Attempt 2: Here I try to gain access to another more complicated api, gmail (so far unsuccessful)
MAIL = "https://gmail.googleapis.com/gmail/v1/users/tmajam@usc.edu/messages"
GAPI = "AIzaSyCT7wACqm44-GR9k_tIS28lFxv1hbJQDWE"
def get_inbox():
	res = requests.get(MAIL, params={"appid": GAPI})
	return res.json()

def main():
    temp = get_weather("London")
    fact = get_cat_fact();
    mail = get_inbox();
    
    print(temp)
    print('\n')
    print("Receiving Cat Fact")
    print(fact)
    print('\n')
    print("Receiving mail")
    print(mail)
    

if __name__ == "__main__":
    main()
