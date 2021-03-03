from datetime import datetime, timedelta
import requests

usuario = 'marioemorac'
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
        partidas["total"] += intervalo["games"]["blitz"]["win"] + intervalo["games"]["blitz"]["loss"] + intervalo["games"]["blitz"]["draw"]      
        partidas["ganadas"] += intervalo["games"]["blitz"]["win"]
        partidas["perdidas"] += intervalo["games"]["blitz"]["loss"]
        partidas["tablas"] += intervalo["games"]["blitz"]["draw"]

print("El usuario", usuario, "jugó", partidas["total"], "partidas esta semana, \n ganando", partidas["ganadas"], "perdiendo", partidas["perdidas"], "y entablando", partidas["tablas"])    
