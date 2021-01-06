import requests

BASE = "http://127.0.0.1:8000/"

# Reuniones

# response = requests.delete(BASE + "crm/reuniones/")
# print(response.json())

response = requests.post(BASE + "crm/reuniones/", {"contenido": "el paciente tiene diarrea", "paciente": 1, "usuario": 1, "areaAlQueSeDerivo":2})
print(response.json())
response = requests.post(BASE + "crm/reuniones/", {"contenido": "el paciente se dio de alta", "paciente": 2, "usuario": 1, "areaAlQueSeDerivo":3})
print(response.json())
response = requests.post(BASE + "crm/reuniones/", {"contenido": "el paciente tiene vomitos", "paciente": 3, "usuario": 1})
print(response.json())
response = requests.post(BASE + "crm/reuniones/", {"contenido": "el paciente esta ciego", "paciente": 2, "usuario": 1, "areaAlQueSeDerivo":3})
print(response.json())

response = requests.get(BASE + "crm/reuniones/")
print(response.json())

# response = requests.get(BASE + "crm/reuniones/5")
# print(response.json())

# response = requests.delete(BASE + "crm/reuniones/5")
# print(response.json())

# response = requests.get(BASE + "crm/reuniones/6")
# print(response.json())

# response = requests.put(BASE + "crm/reuniones/6", {"contenido": "blablabla"})
# print(response.json())
