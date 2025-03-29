import requests

# Function to get random advice
def get_advice():
    url = "https://api.adviceslip.com/advice"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        advice_en = data["slip"]["advice"]
        return advice_en
    else:
        return "Erro ao obter conselho."
