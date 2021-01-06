import requests

BASE = "http://127.0.0.1:8000/"

# Usuarios

# response = requests.delete(BASE + "crm/usuarios/")
# print(response.json())

print('sending request...')
response = requests.post(BASE + "crm/usuarios/", {"username": "iuyuiooiasd", "password": "12345678", "dni": "4564887", "nombre": "larry", "apellido": "bird",
                                                  "fechaNacimiento": "1960-04-04", "email": "larrrry@gmail.com", "telFijo": "321354635", "telMovil": "45787878", "area": 1})
print('status', response.status_code)
try:
    print(response.json())
except:
    pass

# response = requests.post(BASE + "crm/usuarios/", {"dni":"354321321", "nombre":"mugsy", "apellido":"boggs", "fechaNacimiento":"1960-04-04", "email":"mugsy@gmail.com","telFijo":"321354635", "telMovil":"45787878", "area": 13})
# print(response.json())
# response = requests.post(BASE + "crm/usuarios/", {"dni":"4565786", "nombre":"jason", "apellido":"kidd", "fechaNacimiento":"1960-04-04", "email":"jason@gmail.com","telFijo":"321354635", "telMovil":"45787878", "area": 14})
# print(response.json())

# response = requests.get(BASE + "crm/usuarios/")
# print(response.json())

# response = requests.get(BASE + "crm/usuarios/4")
# print(response.json())

# response = requests.delete(BASE + "crm/usuarios/4")
# print(response.json())

# response = requests.get(BASE + "crm/usuarios/5")
# print(response.json())

# response = requests.put(BASE + "crm/usuarios/5", {"nombre": "MICHAEL"})
# print(response.json())
