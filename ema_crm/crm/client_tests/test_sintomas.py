import requests

BASE = "http://127.0.0.1:8000/"

# Sintomas

response = requests.delete(BASE + "crm/sintomas/")
print(response.json())

response = requests.post(BASE + "crm/sintomas/", {"nombre": "tos"})
print(response.json())
response = requests.post(BASE + "crm/sintomas/", {"nombre": "fiebre"})
print(response.json())
response = requests.post(BASE + "crm/sintomas/", {"nombre": "vomitos"})
print(response.json())
response = requests.post(BASE + "crm/sintomas/", {"nombre": "otros"})
print(response.json())


response = requests.get(BASE + "crm/sintomas/")
print(response.json())

# response = requests.get(BASE + "crm/sintomas/2")
# print(response.json())

# response = requests.delete(BASE + "crm/sintomas/2")
# print(response.json())

# response = requests.get(BASE + "crm/sintomas/1")
# print(response.json())

# response = requests.put(BASE + "crm/sintomas/1", {"nombre": "asda"})
# print(response.json())
