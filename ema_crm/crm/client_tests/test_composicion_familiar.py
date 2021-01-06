import requests

BASE = "http://127.0.0.1:8000/"

# Composicion Familiar

# response = requests.delete(BASE + "crm/composiciones_familiares/")
# print(response.json())

response = requests.post(BASE + "crm/composiciones_familiares/", {"vinculo": "madre", "nombre": "susana", "apellido": "lopez", "fechaNacimiento": "1980-01-01", "email": "susana@gmail.com", "telFijo": "45321321352", "telMovil": "4567487", "ocupacion": "maestra", "esConviviente": True, "paciente": 1})
print(response.json())
response = requests.post(BASE + "crm/composiciones_familiares/", {"vinculo": "padre", "nombre": "juan", "apellido": "lopez", "fechaNacimiento": "1980-01-01", "email": "juan@gmail.com", "telFijo": "45321321352", "telMovil": "4567487", "ocupacion": "maestro", "esConviviente": False, "paciente": 2})
print(response.json())
response = requests.post(BASE + "crm/composiciones_familiares/", {"vinculo": "hermano", "nombre": "jose", "apellido": "lopez", "fechaNacimiento": "1980-01-01", "email": "jose@gmail.com", "telFijo": "45321321352", "telMovil": "4567487", "ocupacion": "maestra", "esConviviente": True, "paciente": 3})
print(response.json())

response = requests.get(BASE + "crm/composiciones_familiares/")
print(response.json())

# response = requests.get(BASE + "crm/composiciones_familiares/4")
# print(response.json())

# response = requests.delete(BASE + "crm/composiciones_familiares/4")
# print(response.json())

# response = requests.get(BASE + "crm/composiciones_familiares/5")
# print(response.json())

# response = requests.put(BASE + "crm/composiciones_familiares/5", {"nombre": "asdasd"})
# print(response.json())
