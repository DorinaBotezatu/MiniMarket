from database import functions as db


def genereaza_id(sectiune):
    minimarket = db.citeste_din_baza_de_date()
    produse = minimarket.get(sectiune)
    id_uri = [produs['id'] for produs in produse]
    max_id = max(id_uri) + 1
    return max_id
