import json
from database import calea_catre_baza_de_date

def citeste_din_baza_de_date():
    with open(calea_catre_baza_de_date(), "r") as db:
        return json.load(db)

def scrie_in_baza_de_date():
    with open(calea_catre_baza_de_date(), "w") as db:
        return json.load(db)
