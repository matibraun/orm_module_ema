import requests

BASE = "http://127.0.0.1:8000/"

# Situacion Laboral

response = requests.delete(BASE + "crm/situaciones_laborales/")
print(response.json())

response = requests.post(BASE + "crm/situaciones_laborales/", {"nombre": "en relacion de dependencia"})
print(response.json())
response = requests.post(BASE + "crm/situaciones_laborales/", {"nombre": "independiente"})
print(response.json())
response = requests.post(BASE + "crm/situaciones_laborales/", {"nombre": "autonomo"})
print(response.json())
response = requests.post(BASE + "crm/situaciones_laborales/", {"nombre": "monotributo"})
print(response.json())


response = requests.get(BASE + "crm/situaciones_laborales/")
print(response.json())

# response = requests.get(BASE + "crm/situaciones_laborales/2")
# print(response.json())

# response = requests.delete(BASE + "crm/situaciones_laborales/2")
# print(response.json())

# response = requests.get(BASE + "crm/situaciones_laborales/1")
# print(response.json())

# response = requests.put(BASE + "crm/situaciones_laborales/1", {"nombre": "asdasd"})
# print(response.json())
