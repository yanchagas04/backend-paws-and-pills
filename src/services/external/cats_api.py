import requests
from src.utils.constants import CATS_API_URL, DOGS_CATS_API_KEY

async def get_cat_breeds():
    breed_list = []
    response = requests.get(
            CATS_API_URL, 
            headers={'X-Api-Key': DOGS_CATS_API_KEY},
            params={'max_weight': 200}
        )
    for breed in response.json():
        breed_list.append(breed['name'])
    return breed_list