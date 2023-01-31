from database import functions as db
from database_mysql import functions as my_sql_db

# citire din json
def citeste_produse():
    minimarket = db.citeste_din_baza_de_date()
    produse = minimarket.get('produse')
    if len(produse) > 0:
        return produse

# citire din json
def citeste_produs(id):
    produs = db.citeste_produs(id)
    return produs

# citire din mysql db
def citeste_produse_mysql():
    produse = []
    produse_db = my_sql_db.get_all_products()
    if len(produse_db) > 0:
        for p in range(len(produse_db)):
            produs = {}
            produs["id"] = produse_db[p][0]
            produs["nume"] = produse_db[p][1]
            produs["descriere"] = produse_db[p][3]
            produs["pret"] = produse_db[p][4]
            produs["img"] = produse_db[p][5]
            produse.append(produs)
    return produse

# citire din mysql db
def citeste_produs_mysql(id_produs):
    produs_db = my_sql_db.get_product_by_id(id_produs)
    produs = {}

    produs["id"] = produs_db[0][0]
    produs["nume"] = produs_db[0][1]
    produs["cantitate_disponibila"] = produs_db[0][2]
    produs["descriere"] = produs_db[0][3]
    produs["pret"] = produs_db[0][4]
    produs["img"] = produs_db[0][5]

    return produs
