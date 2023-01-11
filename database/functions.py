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

def sterge_produs(nume):
    with open(calea_catre_baza_de_date(), "a") as db:
         produse = json.load(db)
    for n, obj in enumerate(produse):
        if obj["nume"] == nume:
            produse.pop(n)





if __name__ == "__main__":
    """adauga_produse("Oua,10 bucati",12,"Tip Produs\nOua de gaina,Greutate\n0.7,Termen de valabilitate\nA se consuma inainte de data inscriptionata pe ambalaj.",18.90,"https://auchan.vtexassets.com/arquivos/ids/218874-1600-1600?v=1759796408&width=1600&height=1600&aspect=true")
    adauga_produse("Lapte semidegresat UHT Auchan, 1.5% grasime, 1 l", 12,"Tip Produs\nLapte UHT\nConditii de pastrare\
A se pastra la o temperatura de maxim 25°C\
Tara de origine\
Romania\
Greutate\
1\
Termen de valabilitat\
A se consuma inainte de data inscriptionata pe ambalaj.", 5.70,"https://auchan.vtexassets.com/arquivos/ids/219008-1600-1600?v=1759784963&width=1600&height=1600&aspect=true")
    adauga_produse("Salam de Sibiu Agricola, feliat, 150 g", 5,"Cel mai pretios salam crud-uscat din Romania, Salamul de Sibiu de la Agricola inseamna pentru cunoscatori rasfatul suprem.\ "
                                                               "Preparat din carne aleasa cu cea mai mare grija, condimentat cu un amestec unic de mirodenii si desavarsit de savoarea mucegaiului nobil, "
                                                               "Salamul de Sibiu de la Agricola iti aduce pe masa deliciul si rafinamentul perfect. Salamul de Sibiu de la Agricola- perfect, rafinat, inconfundabil.", 17.30,
                   "https://auchan.vtexassets.com/arquivos/ids/163819-1200-1200?v=1759782137&width=1200&height=1200&aspect=true")
    adauga_produse("Cascaval clasic Hochland, 250 g", 5,"Cascaval clasic Hochland, 250 g. Cascaval laptos, cremos si gustos. Informatii alergeni:",13.90,"https://auchan.vtexassets.com/arquivos/ids/218237-1600-1600?v=1759785032&width=1600&height=1600&aspect=true")
    adauga_produse("Rosii rotunde, 500 g",10,"Rosii rotunde ecologice, pentru diverse preparate culinare", 7.79, "https://auchan.vtexassets.com/arquivos/ids/166388-1200-1200?v=1759792422&width=1200&height=1200&aspect=true")
    adauga_produse("Cartofi albi, 1Kg",30,"Tip Produs\
Cartofi\
Conditii de pastrare\
A se pastra la loc uscat si racoros, ferit de razele soarelui.\
Tara de origine\
Romania\
Greutate\
1",2.79,"https://auchan.vtexassets.com/arquivos/ids/215711-1200-1200?v=638046225344500000&width=1200&height=1200&aspect=true")
    adauga_produse("Apa plata de izvor Auchan, 2 l", 50,"Cantitate\
2\
Tip Produs\
Apa plata\
Greutate\
2.083\
Termen de valabilitate\
A se consuma inainte de data inscriptionata pe ambalaj.",1.15,"https://auchan.vtexassets.com/arquivos/ids/164848-1200-1200?v=1759791128&width=1200&height=1200&aspect=true")
    adauga_produse("Vin rosu sec de Purcari, Pinot Noir 0.75 l",10,"Cantitate\
0.75\
Tip Produs\
Vin rosu",33.99,"https://auchan.vtexassets.com/arquivos/ids/195497-1600-1600?v=1759778271&width=1600&height=1600&aspect=true")"""


