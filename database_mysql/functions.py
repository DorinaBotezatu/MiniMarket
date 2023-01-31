import mysql.connector as db_connector

HOST_NAME = "localhost"
PORT = 3306
user = "root"
password = "26863207"
DATABASE_NAME = "Minimarket"


def create_db_connection():
    try:
        db = db_connector.connect(
            host=HOST_NAME,
            port=PORT,
            password=password,
            user=user,
            database = DATABASE_NAME)
        return db
    except Exception as e:
        print(e)


def create_database(name):
    db = create_db_connection()
    cursor = db.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {name}")
    db.close()


def get_all_products():
    db_connection = create_db_connection()
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    db_connection.close()
    return products


def get_product_by_id(product_id):
    db_connection = create_db_connection()
    cursor = db_connection.cursor()
    cursor.execute(f"SELECT * FROM products WHERE id = '{product_id}'")
    product = cursor.fetchall()
    db_connection.close()
    return product


if __name__ == "__main__":
    create_database(DATABASE_NAME)
    pass
