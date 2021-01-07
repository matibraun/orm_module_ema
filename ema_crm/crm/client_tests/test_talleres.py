import requests

BASE = "http://127.0.0.1:8000/"

response = requests.delete(BASE + "crm/talleres/")
print(response.json())

response = requests.post(BASE + "crm/talleres/", {"nombre": "musica"})
print(response.json())
response = requests.post(BASE + "crm/talleres/", {"nombre": "salsa"})
print(response.json())
response = requests.post(BASE + "crm/talleres/", {"nombre": "gimnasia"})
print(response.json())
response = requests.post(BASE + "crm/talleres/", {"nombre": "arte"})
print(response.json())
response = requests.post(BASE + "crm/talleres/", {"nombre": "canto"})
print(response.json())
response = requests.post(BASE + "crm/talleres/", {"nombre": "otros"})
print(response.json())

response = requests.get(BASE + "crm/talleres/")
print(response.json())

# response = requests.get(BASE + "crm/talleres/2")
# print(response.json())

# response = requests.delete(BASE + "crm/talleres/2")
# print(response.json())

# response = requests.get(BASE + "crm/talleres/3")
# print(response.json())

# response = requests.put(BASE + "crm/talleres/3", {"nombre": "equitacion"})
# print(response.json())
