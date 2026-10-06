from datetime import datetime
import re


# Validaciones del login
def validar_nombre(nombre):
    return nombre and len(nombre) > 4


def validar_contrasena(password):
    malas = ["1234", "admin1", "odio a mis Aux >:(2"]
    return bool(re.search(r"\d", password)) and not password in malas and len(password) > 4



#Validaciones del register
def validar_mail(mail):
    return "@" in mail


def validar_region(region):
    return bool(region)


def validar_comuna(comuna):
    return bool(comuna)


def validar_telefono(fono):
    return len(fono) > 7

def validar_registro(nombre, fono, mail, region, comuna, contrasena, contrasena2):
    return validar_nombre(nombre) and validar_telefono(fono) and validar_mail(mail) and validar_region(region) and validar_comuna(comuna) and validar_contrasena(contrasena) and validar_contrasena(contrasena2) and (contrasena == contrasena2)


#Validaciones del panel

def validar_ave(ave):
    return bool(ave)

def validar_fecha(fecha):
    fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
    return fecha <= datetime.now().date()

def validar_lugar(lugar):
    return bool(lugar)

def validar_foto(foto):
    return bool(foto)

def validar_video(video):
    return bool(video)

def validar_comentario(comentario):
    return bool(comentario)

def validar_avis(ave, fecha, lugar, foto, comentario):
    return validar_ave(ave) and validar_fecha(fecha) and validar_lugar(lugar) and validar_foto(foto) and validar_comentario(comentario)