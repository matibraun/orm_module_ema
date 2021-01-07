import requests

BASE = "http://127.0.0.1:8000/"

# Pacientes

# response = requests.delete(BASE + "crm/pacientes/")
# print(response.json())

# response = requests.post(BASE + "crm/pacientes/", {"dni":"748765465", "nombre":"kareem", "apellido":"abdul", "fechaNacimiento":"1960-04-04", "email":"kareem@gmail.com","telFijo":"5465", "telMovil":"857486", "fechaAlta":"2020-09-01", "usuarioQueRealizoAlta":1, "areaALaQueSeDerivo":2, "esSocio":True, "fechaAsociacion":"2015-05-06", "fechaUltimaCuotaPaga":"2020-01-04", "recibeMailing":False,"coberturaMedica":3, "lugarDeAtencion":"santoiani","neurologoCabecera":"roberto neurix", "actividadFisica": True, "antecedentesEnfermedades": "resfrio, varices", "fechaDiagnostico": "2000-05-05", "fechaVencimientoCUD": "2000-05-05", "fumadorTabaco": True, "participaGrupoApoyoFamiliar": False, "participaGrupoApoyoPacientes": True, "tieneCUD": True })
# print(response.json())
# response = requests.post(BASE + "crm/pacientes/", {"dni":"85764546", "nombre":"scottie", "apellido":"pippen", "fechaNacimiento":"1960-04-04", "email":"scottie@gmail.com","telFijo":"5465", "telMovil":"857486", "fechaAlta":"2020-09-01", "usuarioQueRealizoAlta":1, "areaALaQueSeDerivo":1, "esSocio":True, "fechaAsociacion":"2015-05-06", "fechaUltimaCuotaPaga":"2020-01-04", "recibeMailing":False,"coberturaMedica":3, "lugarDeAtencion":"santoiani","neurologoCabecera":"roberto neurix", "actividadFisica": True, "antecedentesEnfermedades": "resfrio, varices", "fechaDiagnostico": "2000-05-05", "fechaVencimientoCUD": "2000-05-05", "fumadorTabaco": True, "participaGrupoApoyoFamiliar": False, "participaGrupoApoyoPacientes": True, "tieneCUD": True })
# print(response.json())
# response = requests.post(BASE + "crm/pacientes/", {"dni":"3321321", "nombre":"steve", "apellido":"kerr", "fechaNacimiento":"1960-04-04", "email":"steve@gmail.com","telFijo":"5465", "telMovil":"857486", "fechaAlta":"2020-09-01", "usuarioQueRealizoAlta":1, "areaALaQueSeDerivo":4, "esSocio":True, "fechaAsociacion":"2015-05-06", "fechaUltimaCuotaPaga":"2020-01-04", "recibeMailing":False,"coberturaMedica":4, "lugarDeAtencion":"santoiani","neurologoCabecera":"roberto neurix", "actividadFisica": True, "antecedentesEnfermedades": "resfrio, varices", "fechaDiagnostico": "2000-05-05", "fechaVencimientoCUD": "2000-05-05", "fumadorTabaco": True, "participaGrupoApoyoFamiliar": False, "participaGrupoApoyoPacientes": True, "tieneCUD": True })
# print(response.json())
# response = requests.post(BASE + "crm/pacientes/", {"dni":"5463413", "nombre":"shaq", "apellido":"oneall", "fechaNacimiento":"1960-04-04", "email":"shaq@gmail.com","telFijo":"5465", "telMovil":"857486", "fechaAlta":"2020-09-01", "usuarioQueRealizoAlta":1, "areaALaQueSeDerivo":2, "esSocio":True, "fechaAsociacion":"2015-05-06", "fechaUltimaCuotaPaga":"2020-01-04", "recibeMailing":False,"coberturaMedica":1, "lugarDeAtencion":"santoiani","neurologoCabecera":"roberto neurix", "actividadFisica": True, "antecedentesEnfermedades": "resfrio, varices", "fechaDiagnostico": "2000-05-05", "fechaVencimientoCUD": "2000-05-05", "fumadorTabaco": True, "participaGrupoApoyoFamiliar": False, "participaGrupoApoyoPacientes": True, "tieneCUD": True })
# print(response.json())


response = requests.get(BASE + "crm/pacientes/")
print(response.json())

# response = requests.get(BASE + "crm/pacientes/6")
# print(response.json())

# response = requests.delete(BASE + "crm/pacientes/6")
# print(response.json())

# response = requests.get(BASE + "crm/pacientes/7")
# print(response.json())

# response = requests.put(BASE + "crm/pacientes/7", {"nombre": "MICHAEL"})
# print(response.json())
