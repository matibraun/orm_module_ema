import requests

BASE = "http://127.0.0.1:8000/"

response = requests.delete(BASE + "crm/talleres_pacientes/")
print(response.json())

response = requests.post(BASE + "crm/talleres_pacientes/", {"paciente": 6, "taller": 1})
response = requests.post(BASE + "crm/talleres_pacientes/", {"paciente": 7, "taller": 3})
response = requests.post(BASE + "crm/talleres_pacientes/", {"paciente": 8, "taller": 4})
response = requests.post(BASE + "crm/talleres_pacientes/", {"paciente": 8, "taller": 5})


response = requests.get(BASE + "crm/talleres_pacientes/")
print(response.json())

# response = requests.get(BASE + "crm/talleres/2")
# print(response.json())

# response = requests.delete(BASE + "crm/talleres/2")
# print(response.json())

# response = requests.get(BASE + "crm/talleres/3")
# print(response.json())

# response = requests.put(BASE + "crm/talleres/3", {"nombre": "equitacion"})
# print(response.json())
