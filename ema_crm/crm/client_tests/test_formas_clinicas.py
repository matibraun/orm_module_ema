import requests

BASE = "http://127.0.0.1:8000/"

# FormasClinicas

response = requests.delete(BASE + "crm/formas_clinicas/")
print(response.json())

response = requests.post(BASE + "crm/formas_clinicas/", {"nombre": "brotes y remisiones"})
print(response.json())
response = requests.post(BASE + "crm/formas_clinicas/", {"nombre": "primaria progresiva"})
print(response.json())
response = requests.post(BASE + "crm/formas_clinicas/", {"nombre": "secundaria progresiva"})
print(response.json())
response = requests.post(BASE + "crm/formas_clinicas/", {"nombre": "sindrome desmielinizante"})
print(response.json())

response = requests.get(BASE + "crm/formas_clinicas/")
print(response.json())

# response = requests.get(BASE + "crm/formas_clinicas/2")
# print(response.json())

# response = requests.delete(BASE + "crm/formas_clinicas/2")
# print(response.json())

# response = requests.get(BASE + "crm/formas_clinicas/1")
# print(response.json())

# response = requests.put(BASE + "crm/formas_clinicas/1", {"nombre": "asda"})
# print(response.json())

