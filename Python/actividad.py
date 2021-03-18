from datetime import datetime, timedelta
import requests

def obtener_actividad(usuario):
    direccion = 'https://lichess.org/api/user/{}/activity'.format(usuario)

    actividad = requests.get(direccion)
    actividad = actividad.json()


    hoy = datetime.today()
    diferencia = (hoy.weekday() + 1) % 7
    domingo = hoy - timedelta(7 + diferencia)

    partidas = {"total": 0, "ganadas": 0, "perdidas": 0, "tablas":0}

    for intervalo in actividad:
        st = int(str(intervalo["interval"]["start"])[:10])
        startTime = datetime.fromtimestamp(st)

        if(startTime > domingo):
            if "blitz" in intervalo["games"]:
                partidas["total"] += intervalo["games"]["blitz"]["win"] + intervalo["games"]["blitz"]["loss"] + intervalo["games"]["blitz"]["draw"]      
                partidas["ganadas"] += intervalo["games"]["blitz"]["win"]
                partidas["perdidas"] += intervalo["games"]["blitz"]["loss"]
                partidas["tablas"] += intervalo["games"]["blitz"]["draw"]
            if "rapid" in intervalo["games"]:
                partidas["total"] += intervalo["games"]["rapid"]["win"] + intervalo["games"]["rapid"]["loss"] + intervalo["games"]["rapid"]["draw"]      
                partidas["ganadas"] += intervalo["games"]["rapid"]["win"]
                partidas["perdidas"] += intervalo["games"]["rapid"]["loss"]
                partidas["tablas"] += intervalo["games"]["rapid"]["draw"]
            if "classic" in intervalo["games"]:
                partidas["total"] += intervalo["games"]["classic"]["win"] + intervalo["games"]["classic"]["loss"] + intervalo["games"]["classic"]["draw"]      
                partidas["ganadas"] += intervalo["games"]["classic"]["win"]
                partidas["perdidas"] += intervalo["games"]["classic"]["loss"]
                partidas["tablas"] += intervalo["games"]["classic"]["draw"]

    print("El usuario", usuario, "jugó", partidas["total"], "partidas esta semana, \n ganando", partidas["ganadas"], "\n perdiendo", partidas["perdidas"], "\n y entablando", partidas["tablas"])    

usuarios = ['samu_cr', 'benjaminjimenezv', 'bruno_esteban', 'Kendall901', 'MatiasChaconAraya', 'jworozco', 'rafa_1011', 'joaquin_rosales_h', 'jairoaraya']

for usuario in usuarios:
    obtener_actividad(usuario)