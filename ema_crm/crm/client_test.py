import requests

BASE = "http://127.0.0.1:8000/"



# response = requests.post(BASE + "crm/provincias/", {"nombre": "cordoba"})
# print(response.json())
# response = requests.post(BASE + "crm/provincias/", {"nombre": "santa cruz"})
# print(response.json())
# response = requests.post(BASE + "crm/provincias/", {"nombre": "salta"})
# print(response.json())

# response = requests.get(BASE + "crm/provincias/")
# print(response.json())

# response = requests.delete(BASE + "crm/provincias/7")
# print(response.json())

# response = requests.get(BASE + "crm/provincias/9")
# print(response.json())

response = requests.put(BASE + "crm/provincias/9", {"nombre": "buenos aires"})
print(response.json())






# response = requests.post(BASE + "crm/pacientes/", {"dni":"555655656", "nombre":"larry", "apellido":"bird", "fechaNacimiento":"1960-04-04", "email":"larry@gmail.com","telFijo":"321354635", "telMovil":"45787878", "fechaAlta":"2020-09-01", "usuarioQueRealizoAlta_id":1, "areaALaQueSeDerivo_id":2, "esSocio":True, "fechaAsociacion":"2015-05-06", "fechaUltimaCuotaPaga":"2020-01-04", "recibeMailing":False,"coberturaMedica_id":2, "lugarDeAtencion":"santoiani","neurologoCabecera":"roberto neurix"})
# print(response.json())