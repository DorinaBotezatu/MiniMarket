from database import functions as db


def citeste_produse():
    minimarket = db.citeste_din_baza_de_date()
    produse = minimarket.get('produse')
    if len(produse) > 0:
        return produse


def citeste_produs(id):
    produs = db.citeste_produs(id)
    return produs
