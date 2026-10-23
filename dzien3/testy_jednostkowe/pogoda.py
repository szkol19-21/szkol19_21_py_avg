# Makieta (mock) zastepuje prawdziwy obiekt jego 'atrape'. gdybysmy nie chceili odpalaca 
# prawdziwej bazdy danych, sieci, wysylki maili. Uzywamy unittest.mock

import requests
# wymaga requests --> pip install requests

def aktualna_temperatura(miasto):
    odp = requests.get(f'https://api.pogoda.pl/{miasto}') # przykladowe api
    return odp.json()['temp']

    # [{},{},{},{}]


def aktualna_temp(miasto):
    try:
        odp = requests.get(f"https://api.pogoda.pl/{miasto}", timeout=5)
    except requests.Timeout:
        return None
    return odp.json()["temp"]