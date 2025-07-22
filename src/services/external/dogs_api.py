import requests
from src.utils.constants import DOGS_API_URL, API_KEY

async def get_dogs_breeds():
    breed_list = []
    response = requests.get(
            DOGS_API_URL, 
            headers={'X-Api-Key': API_KEY},
            params={'max_weight': 200}
        )
    for breed in response.json():
        breed_list.append(breed['name'])
    return breed_list