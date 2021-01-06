import requests

BASE = "http://127.0.0.1:8000/"

# TerapiaRehabilitacion OK

response = requests.delete(BASE + "crm/terapias_y_rehabilitaciones/")
print(response.json())

response = requests.post(BASE + "crm/terapias_y_rehabilitaciones/", {"nombre": "psicologia"})
print(response.json())
response = requests.post(BASE + "crm/terapias_y_rehabilitaciones/", {"nombre": "kinesiologia"})
print(response.json())
response = requests.post(BASE + "crm/terapias_y_rehabilitaciones/", {"nombre": "terapia ocupacional"})
print(response.json())
response = requests.post(BASE + "crm/terapias_y_rehabilitaciones/", {"nombre": "neuropsicologia"})
print(response.json())
response = requests.post(BASE + "crm/terapias_y_rehabilitaciones/", {"nombre": "musicoterapia"})
print(response.json())
response = requests.post(BASE + "crm/terapias_y_rehabilitaciones/", {"nombre": "otros"})
print(response.json())

response = requests.get(BASE + "crm/terapias_y_rehabilitaciones/")
print(response.json())

# response = requests.get(BASE + "crm/terapias_y_rehabilitaciones/2")
# print(response.json())

# response = requests.delete(BASE + "crm/terapias_y_rehabilitaciones/2")
# print(response.json())

# response = requests.get(BASE + "crm/terapias_y_rehabilitaciones/3")
# print(response.json())

# response = requests.put(BASE + "crm/terapias_y_rehabilitaciones/3", {"nombre": "fisioterapia"})
# print(response.json())
