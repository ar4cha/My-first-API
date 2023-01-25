import json
import requests

data = requests.get("https://api.chucknorris.io/jokes/categories")
print(data.text)
print(data.status_code)
#["animal","career","celebrity","dev","explicit","fashion","food","history","money","movie","music","political","religion","science","sport","travel"]
# value = "fashion"
#params={'key': fas}
print("-----------------------------------------------------------------------------------------")
print("random category")
print("\n")

choice = 'fashion'
random_jokes = requests.get("https://api.chucknorris.io/jokes/random?")
#Šādi Tu izprintē pilnu Json 
print(random_jokes.text)
#Šādi Tu izprintē tikai joka tekstu
print(random_jokes.json()['value'])

print("----------------------------------------------------------------------------------------")
print("history jokes")
print("\n")
history_jokes = requests.get("https://api.chucknorris.io/jokes/random?category={history}")
history_jokes_text = json.loads(history_jokes.text)
print(history_jokes_text)
# Diemžēl pašā API šis nestrādā šobrīd