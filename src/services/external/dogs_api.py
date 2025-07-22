import requests

def get_dogs_breeds():
    response = requests.get("https://api.api-ninjas.com/v1/dogs")
    return response.json()