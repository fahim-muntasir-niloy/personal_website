import os, requests, json
from dotenv import load_dotenv
from pyscript import document

load_dotenv()
quoteApi = os.getenv('QUOTES_API')

category = 'knowledge'
api_url = f'https://api.api-ninjas.com/v1/quotes?category={category}'

def get_quote():
    response = requests.get(api_url, headers={'X-Api-Key': quoteApi})
    if response.status_code == requests.codes.ok:
        output = json.loads(response.text)
        
        quote_text = document.querySelector("#quote")
        quote_text.innerText = output[0]['quote']
        autor_text = document.querySelector("#author")
        autor_text.innerText = output[0]['author']

    else:
        return f"Error: {response.status_code, response.text}"

