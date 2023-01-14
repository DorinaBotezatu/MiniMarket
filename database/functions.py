import json
from utils import functii as f

from database import calea_catre_baza_de_date


def citeste_din_baza_de_date():
    with open(calea_catre_baza_de_date(), "r") as db:
        return json.load(db)


def citeste_produs(id):
    produse = citeste_din_baza_de_date()
    produs_gasit = None
    for p in produse["produse"]:
        if int(id) == p["id"]:
            produs_gasit = p
            break
    return produs_gasit


def adauga_produse(nume, cantitate_disponibila, descriere, pret, imagine, filename='minimarket.json'):
    with open(filename, 'r+') as file:
        y = {"id": f.genereaza_id("produse"),
             "nume": nume,
             "cantitate_disponibila": cantitate_disponibila,
             "descriere": descriere,
             "pret": pret,
             "img": imagine
             }
        file_data = json.load(file)
        file_data["produse"].append(y)
        file.seek(0)
        json.dump(file_data, file, indent=4)


if __name__ == "__main__":
    pass
