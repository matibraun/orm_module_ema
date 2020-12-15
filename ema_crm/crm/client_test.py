import requests

BASE = "http://127.0.0.1:8000/"

# Provincias

# response = requests.delete(BASE + "crm/provincias/")
# print(response.json())

# response = requests.post(BASE + "crm/provincias/", {"nombre": "cordoba"})
# print(response.json())
# response = requests.post(BASE + "crm/provincias/", {"nombre": "santa cruz"})
# print(response.json())
# response = requests.post(BASE + "crm/provincias/", {"nombre": "salta"})
# print(response.json())
# response = requests.post(BASE + "crm/provincias/", {"nombre": "neuquen"})
# print(response.json())

# response = requests.get(BASE + "crm/provincias/")
# print(response.json())

# response = requests.get(BASE + "crm/provincias/16")
# print(response.json())

# response = requests.delete(BASE + "crm/provincias/16")
# print(response.json())

# response = requests.get(BASE + "crm/provincias/17")
# print(response.json())

# response = requests.put(BASE + "crm/provincias/17", {"nombre": "buenos aires"})
# print(response.json())


#############################################################################################

# Areas

# response = requests.delete(BASE + "crm/areas/")
# print(response.json())

# response = requests.post(BASE + "crm/areas/", {"nombre": "legal"})
# print(response.json())
# response = requests.post(BASE + "crm/areas/", {"nombre": "medico"})
# print(response.json())
# response = requests.post(BASE + "crm/areas/", {"nombre": "social"})
# print(response.json())
# response = requests.post(BASE + "crm/areas/", {"nombre": "recepcion"})
# print(response.json())

# response = requests.get(BASE + "crm/areas/")
# print(response.json())

# response = requests.get(BASE + "crm/areas/16")
# print(response.json())

# response = requests.delete(BASE + "crm/areas/16")
# print(response.json())

# response = requests.get(BASE + "crm/areas/17")
# print(response.json())

# response = requests.put(BASE + "crm/areas/17", {"nombre": "social"})
# print(response.json())


#############################################################################################

# Tratamientos

# response = requests.delete(BASE + "crm/tratamientos/")
# print(response.json())

# response = requests.post(BASE + "crm/tratamientos/", {"fecha": "1-1-2020", "medicoTratante": "pepe", "tratamiento": "tratamiento 1", "droga": "droga a", "marca": "pfizer", "paciente": 1})
# print(response.json())
# response = requests.post(BASE + "crm/tratamientos/", {"fecha": "1-2-2020", "medicoTratante": "jose", "tratamiento": "tratamiento 2", "droga": "droga b", "marca": "bago", "paciente": 2})
# print(response.json())
# response = requests.post(BASE + "crm/tratamientos/", {"fecha": "3-1-2020", "medicoTratante": "juan", "tratamiento": "tratamiento 3", "droga": "droga c", "marca": "sputnik", "paciente": 3})
# print(response.json())
# response = requests.post(BASE + "crm/tratamientos/", {"fecha": "4-1-2020", "medicoTratante": "josele", "tratamiento": "tratamiento 4", "droga": "droga d", "marca": "roche", "paciente": 4})
# print(response.json())

# response = requests.get(BASE + "crm/tratamientos/")
# print(response.json())

# response = requests.get(BASE + "crm/tratamientos/2")
# print(response.json())

# response = requests.delete(BASE + "crm/tratamientos/2")
# print(response.json())

# response = requests.get(BASE + "crm/tratamientos/3")
# print(response.json())

# response = requests.put(BASE + "crm/tratamientos/3", {"nombre": "sutebah"})
# print(response.json())


#############################################################################################

# CoberturasMedicas

# response = requests.delete(BASE + "crm/coberturas_medicas/")
# print(response.json())

# response = requests.post(BASE + "crm/coberturas_medicas/", {"nombre": "medicus"})
# print(response.json())
# response = requests.post(BASE + "crm/coberturas_medicas/", {"nombre": "swiss medical"})
# print(response.json())
# response = requests.post(BASE + "crm/coberturas_medicas/", {"nombre": "osde"})
# print(response.json())
# response = requests.post(BASE + "crm/coberturas_medicas/", {"nombre": "accord"})
# print(response.json())

# response = requests.get(BASE + "crm/coberturas_medicas/")
# print(response.json())

# response = requests.get(BASE + "crm/coberturas_medicas/2")
# print(response.json())

# response = requests.delete(BASE + "crm/coberturas_medicas/2")
# print(response.json())

# response = requests.get(BASE + "crm/coberturas_medicas/3")
# print(response.json())

# response = requests.put(BASE + "crm/coberturas_medicas/3", {"nombre": "sutebah"})
# print(response.json())


#############################################################################################

# Tratamientos NO ANDA FK A PACIENTE

# response = requests.delete(BASE + "crm/tratamientos/")
# print(response.json())

# response = requests.post(BASE + "crm/tratamientos/", {"medicoTratante": "pepe", "tratamiento": "tratamiento 1", "droga": "droga a", "marca": "pfizer", "paciente": 1})
# print(response.json())
# response = requests.post(BASE + "crm/tratamientos/", {"medicoTratante": "jose", "tratamiento": "tratamiento 2", "droga": "droga b", "marca": "bago", "paciente": 2})
# print(response.json())
# response = requests.post(BASE + "crm/tratamientos/", {"medicoTratante": "juan", "tratamiento": "tratamiento 3", "droga": "droga c", "marca": "sputnik", "paciente": 3})
# print(response.json())
# response = requests.post(BASE + "crm/tratamientos/", {"medicoTratante": "josele", "tratamiento": "tratamiento 4", "droga": "droga d", "marca": "roche", "paciente": 4})
# print(response.json())

# response = requests.get(BASE + "crm/tratamientos/")
# print(response.json())

# response = requests.get(BASE + "crm/tratamientos/2")
# print(response.json())

# response = requests.delete(BASE + "crm/tratamientos/2")
# print(response.json())

# response = requests.get(BASE + "crm/tratamientos/3")
# print(response.json())

# response = requests.put(BASE + "crm/tratamientos/3", {"nombre": "sutebah"})
# print(response.json())


#############################################################################################

# TerapiaRehabilitacion OK

# response = requests.delete(BASE + "crm/terapias_y_rehabilitaciones/")
# print(response.json())

# response = requests.post(BASE + "crm/terapias_y_rehabilitaciones/", {"nombre": "psicologia"})
# print(response.json())
# response = requests.post(BASE + "crm/terapias_y_rehabilitaciones/", {"nombre": "kinesiologia"})
# print(response.json())
# response = requests.post(BASE + "crm/terapias_y_rehabilitaciones/", {"nombre": "terapia ocupacional"})
# print(response.json())
# response = requests.post(BASE + "crm/terapias_y_rehabilitaciones/", {"nombre": "neuropsicologia"})
# print(response.json())
# response = requests.post(BASE + "crm/terapias_y_rehabilitaciones/", {"nombre": "musicoterapia"})
# print(response.json())
# response = requests.post(BASE + "crm/terapias_y_rehabilitaciones/", {"nombre": "otros"})
# print(response.json())

# response = requests.get(BASE + "crm/terapias_y_rehabilitaciones/")
# print(response.json())

# response = requests.get(BASE + "crm/terapias_y_rehabilitaciones/2")
# print(response.json())

# response = requests.delete(BASE + "crm/terapias_y_rehabilitaciones/2")
# print(response.json())

# response = requests.get(BASE + "crm/terapias_y_rehabilitaciones/3")
# print(response.json())

# response = requests.put(BASE + "crm/terapias_y_rehabilitaciones/3", {"nombre": "fisioterapia"})
# print(response.json())


#############################################################################################

# Talleres ANDA SIN EL FK A PACIENTE

# response = requests.delete(BASE + "crm/talleres/")
# print(response.json())

# response = requests.post(BASE + "crm/talleres/", {"nombre": "musica"})
# print(response.json())
# response = requests.post(BASE + "crm/talleres/", {"nombre": "salsa"})
# print(response.json())
# response = requests.post(BASE + "crm/talleres/", {"nombre": "gimnasia"})
# print(response.json())
# response = requests.post(BASE + "crm/talleres/", {"nombre": "arte"})
# print(response.json())
# response = requests.post(BASE + "crm/talleres/", {"nombre": "canto"})
# print(response.json())
# response = requests.post(BASE + "crm/talleres/", {"nombre": "otros"})
# print(response.json())

# response = requests.get(BASE + "crm/talleres/")
# print(response.json())

# response = requests.get(BASE + "crm/talleres/2")
# print(response.json())

# response = requests.delete(BASE + "crm/talleres/2")
# print(response.json())

# response = requests.get(BASE + "crm/talleres/3")
# print(response.json())

# response = requests.put(BASE + "crm/talleres/3", {"nombre": "equitacion"})
# print(response.json())


#############################################################################################

# Usuarios OK

# response = requests.delete(BASE + "crm/usuarios/")
# print(response.json())

# response = requests.post(BASE + "crm/usuarios/", {"dni": "4564887", "nombre": "larry", "apellido": "bird", "fechaNacimiento": "1960-04-04", "email": "larrrry@gmail.com", "telFijo": "321354635", "telMovil": "45787878", "area": 12})
# print(response.json())
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


#############################################################################################

# Pacientes

# response = requests.delete(BASE + "crm/pacientes/")
# print(response.json())

# response = requests.post(BASE + "crm/pacientes/", {"dni":"748765465", "nombre":"kareem", "apellido":"abdul", "fechaNacimiento":"1960-04-04", "email":"kareem@gmail.com","telFijo":"5465", "telMovil":"857486", "fechaAlta":"2020-09-01", "usuarioQueRealizoAlta":5, "areaALaQueSeDerivo":12, "esSocio":True, "fechaAsociacion":"2015-05-06", "fechaUltimaCuotaPaga":"2020-01-04", "recibeMailing":False,"coberturaMedica":3, "lugarDeAtencion":"santoiani","neurologoCabecera":"roberto neurix", "actividadFisica": True, "antecedentesEnfermedades": "resfrio, varices", "fechaDiagnostico": "2000-05-05", "fechaVencimientoCUD": "2000-05-05", "fumadorTabaco": True, "participaGrupoApoyoFamiliar": False, "participaGrupoApoyoPacientes": True, "tieneCUD": True })
# print(response.json())
# response = requests.post(BASE + "crm/pacientes/", {"dni":"85764546", "nombre":"scottie", "apellido":"pippen", "fechaNacimiento":"1960-04-04", "email":"scottie@gmail.com","telFijo":"5465", "telMovil":"857486", "fechaAlta":"2020-09-01", "usuarioQueRealizoAlta":5, "areaALaQueSeDerivo":12, "esSocio":True, "fechaAsociacion":"2015-05-06", "fechaUltimaCuotaPaga":"2020-01-04", "recibeMailing":False,"coberturaMedica":3, "lugarDeAtencion":"santoiani","neurologoCabecera":"roberto neurix", "actividadFisica": True, "antecedentesEnfermedades": "resfrio, varices", "fechaDiagnostico": "2000-05-05", "fechaVencimientoCUD": "2000-05-05", "fumadorTabaco": True, "participaGrupoApoyoFamiliar": False, "participaGrupoApoyoPacientes": True, "tieneCUD": True })
# print(response.json())
# response = requests.post(BASE + "crm/pacientes/", {"dni":"3321321", "nombre":"steve", "apellido":"kerr", "fechaNacimiento":"1960-04-04", "email":"steve@gmail.com","telFijo":"5465", "telMovil":"857486", "fechaAlta":"2020-09-01", "usuarioQueRealizoAlta":5, "areaALaQueSeDerivo":12, "esSocio":True, "fechaAsociacion":"2015-05-06", "fechaUltimaCuotaPaga":"2020-01-04", "recibeMailing":False,"coberturaMedica":3, "lugarDeAtencion":"santoiani","neurologoCabecera":"roberto neurix", "actividadFisica": True, "antecedentesEnfermedades": "resfrio, varices", "fechaDiagnostico": "2000-05-05", "fechaVencimientoCUD": "2000-05-05", "fumadorTabaco": True, "participaGrupoApoyoFamiliar": False, "participaGrupoApoyoPacientes": True, "tieneCUD": True })
# print(response.json())
# response = requests.post(BASE + "crm/pacientes/", {"dni":"5463413", "nombre":"shaq", "apellido":"oneall", "fechaNacimiento":"1960-04-04", "email":"shaq@gmail.com","telFijo":"5465", "telMovil":"857486", "fechaAlta":"2020-09-01", "usuarioQueRealizoAlta":5, "areaALaQueSeDerivo":12, "esSocio":True, "fechaAsociacion":"2015-05-06", "fechaUltimaCuotaPaga":"2020-01-04", "recibeMailing":False,"coberturaMedica":3, "lugarDeAtencion":"santoiani","neurologoCabecera":"roberto neurix", "actividadFisica": True, "antecedentesEnfermedades": "resfrio, varices", "fechaDiagnostico": "2000-05-05", "fechaVencimientoCUD": "2000-05-05", "fumadorTabaco": True, "participaGrupoApoyoFamiliar": False, "participaGrupoApoyoPacientes": True, "tieneCUD": True })
# print(response.json())


# response = requests.get(BASE + "crm/pacientes/")
# print(response.json())

# response = requests.get(BASE + "crm/pacientes/6")
# print(response.json())

# response = requests.delete(BASE + "crm/pacientes/6")
# print(response.json())

# response = requests.get(BASE + "crm/pacientes/7")
# print(response.json())

# response = requests.put(BASE + "crm/pacientes/7", {"nombre": "MICHAEL"})
# print(response.json())


#############################################################################################


# Domicilios OK

# response = requests.delete(BASE + "crm/domicilios/")
# print(response.json())

# response = requests.post(BASE + "crm/domicilios/", {"calle": "ibera", "numero": "2415", "piso": "45", "localidad": "villa ortuzar", "codigoPostal": "465", "paciente": 7, "provincia": 14})
# print(response.json())
# response = requests.post(BASE + "crm/domicilios/", {"calle": "pampa", "numero": "422", "piso": "45", "localidad": "belgrano", "codigoPostal": "465", "paciente": 5, "provincia": 15})
# print(response.json())
# response = requests.post(BASE + "crm/domicilios/", {"calle": "tronador", "numero": "1232", "piso": "45", "localidad": "palermo", "codigoPostal": "465", "paciente": 7, "provincia": 15})
# print(response.json())
# response = requests.post(BASE + "crm/domicilios/", {"calle": "callao", "numero": "2415", "piso": "45", "localidad": "barrio norte", "codigoPostal": "465", "paciente": 8, "provincia": 17})
# print(response.json())

# response = requests.get(BASE + "crm/domicilios/")
# print(response.json())

# response = requests.get(BASE + "crm/domicilios/5")
# print(response.json())

# response = requests.delete(BASE + "crm/domicilios/5")
# print(response.json())

# response = requests.get(BASE + "crm/domicilios/6")
# print(response.json())

# response = requests.put(BASE + "crm/domicilios/6", {"calle": "QUESADA"})
# print(response.json())


#############################################################################################


# Reuniones

response = requests.delete(BASE + "crm/reuniones/")
print(response.json())

response = requests.post(BASE + "crm/reuniones/", {"contenido": "el paciente tiene diarrea", "paciente": 7, "usuario": 5, "areaAlQueSeDerivo":12})
print(response.json())
response = requests.post(BASE + "crm/reuniones/", {"contenido": "el paciente se dio de alta", "paciente": 8, "usuario": 6, "areaAlQueSeDerivo":13})
print(response.json())
response = requests.post(BASE + "crm/reuniones/", {"contenido": "el paciente tiene vomitos", "paciente": 8, "usuario": 6})
print(response.json())
response = requests.post(BASE + "crm/reuniones/", {"contenido": "el paciente esta ciego", "paciente": 5, "usuario": 5, "areaAlQueSeDerivo":13})
print(response.json())

# response = requests.get(BASE + "crm/reuniones/")
# print(response.json())

# response = requests.get(BASE + "crm/reuniones/2")
# print(response.json())

# response = requests.delete(BASE + "crm/reuniones/2")
# print(response.json())

# response = requests.get(BASE + "crm/reuniones/3")
# print(response.json())

# response = requests.put(BASE + "crm/reuniones/3", {"nombre": "equitacion"})
# print(response.json())


#############################################################################################
