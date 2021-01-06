import requests

BASE = "http://127.0.0.1:8000/"

# Diagnosticos

response = requests.delete(BASE + "crm/diagnosticos/")
print(response.json())

response = requests.post(BASE + "crm/diagnosticos/", {"nombre": "esclerosis multiple"})
print(response.json())
response = requests.post(BASE + "crm/diagnosticos/", {"nombre": "NMO"})
print(response.json())

response = requests.get(BASE + "crm/diagnosticos/")
print(response.json())

# response = requests.get(BASE + "crm/diagnosticos/2")
# print(response.json())

# response = requests.delete(BASE + "crm/diagnosticos/2")
# print(response.json())

# response = requests.get(BASE + "crm/diagnosticos/1")
# print(response.json())

# response = requests.put(BASE + "crm/diagnosticos/1", {"nombre": "asda"})
# print(response.json())
