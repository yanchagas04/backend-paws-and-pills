import os

# Constantes utilizadas no projeto que não precisam de .env
DOGS_API_URL="https://api.api-ninjas.com/v1/dogs"
CATS_API_URL="https://api.api-ninjas.com/v1/cats"
DOGS_CATS_API_KEY=os.getenv("DOGS_CATS_API_KEY")