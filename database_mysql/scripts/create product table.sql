CREATE TABLE IF NOT EXISTS products(
    id int NOT NULL AUTO_INCREMENT,
    nume varchar(150) NOT NULL,
    cantitate_disponibila int NOT NULL,
    descriere varchar(500) NOT NULL,
    pret float(6,2) NOT NULL,
    img varchar(300),
    PRIMARY KEY (id)
)

