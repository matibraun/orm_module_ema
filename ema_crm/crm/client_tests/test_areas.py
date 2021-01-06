import requests

BASE = "http://127.0.0.1:8000/"

# Areas

response = requests.delete(BASE + "crm/areas/")
print(response.json())

response = requests.post(BASE + "crm/areas/", {"nombre": "legal"})
print(response.json())
response = requests.post(BASE + "crm/areas/", {"nombre": "medico"})
print(response.json())
response = requests.post(BASE + "crm/areas/", {"nombre": "social"})
print(response.json())
response = requests.post(BASE + "crm/areas/", {"nombre": "recepcion"})
print(response.json())

# response = requests.get(BASE + "crm/areas/")
# print(response.json())

# response = requests.get(BASE + "crm/areas/16")
# print(response.json())

# response = requests.delete(BASE + "crm/areas/16")
# print(response.json())

# response = requests.get(BASE + "crm/areas/17")
# print(response.json())

# response = requests.put(BASE + "crm/areas/17", {"nombre": "social"})
# print(response.json())
