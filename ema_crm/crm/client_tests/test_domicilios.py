import requests

BASE = "http://127.0.0.1:8000/"

# Domicilios OK

response = requests.delete(BASE + "crm/domicilios/")
print(response.json())

response = requests.post(BASE + "crm/domicilios/", {"calle": "ibera", "numero": "2415", "piso": "45", "localidad": "villa ortuzar", "codigoPostal": "465", "paciente": 1, "provincia": 1})
print(response.json())
response = requests.post(BASE + "crm/domicilios/", {"calle": "pampa", "numero": "422", "piso": "45", "localidad": "belgrano", "codigoPostal": "465", "paciente": 2, "provincia": 2})
print(response.json())
response = requests.post(BASE + "crm/domicilios/", {"calle": "tronador", "numero": "1232", "piso": "45", "localidad": "palermo", "codigoPostal": "465", "paciente": 3, "provincia": 3})
print(response.json())
response = requests.post(BASE + "crm/domicilios/", {"calle": "callao", "numero": "2415", "piso": "45", "localidad": "barrio norte", "codigoPostal": "465", "paciente": 4, "provincia": 4})
print(response.json())

response = requests.get(BASE + "crm/domicilios/")
print(response.json())

# response = requests.get(BASE + "crm/domicilios/5")
# print(response.json())

# response = requests.delete(BASE + "crm/domicilios/5")
# print(response.json())

# response = requests.get(BASE + "crm/domicilios/6")
# print(response.json())

# response = requests.put(BASE + "crm/domicilios/6", {"calle": "QUESADA"})
# print(response.json())
