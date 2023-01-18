import json
import psycopg2


def get_product_by_id(config, id):
    """ Принимает словарь для подключения к базе данных и id продукта
        Возвращает json-строку, где есть следующая информация:
            - id продукта
            - наименование продукта
            - наименование категории продукта
            - цену продукта"""
    conn = psycopg2.connect(
        host=config.get('host'),
        database=config.get('database'),
        user=config.get('user'),
        password=config.get('password')
    )
    try:
        with conn:
            with conn.cursor() as cur:  # закрывает курсор
                cur.execute(
                    f"SELECT product_id, product_name, category_name, unit_price FROM products "
                    f"JOIN categories USING(category_id) WHERE product_id = {id}")
                row = cur.fetchone()
                return [{"product_id": row[0], "product_name": row[1], "category_name": row[2], "unit_price": row[3]}]

    finally:
        conn.close()


def get_category_by_id(config, id):
    """ Принимает словарь для подключения к базе данных и id категории продукта
        Возвращает json-строку, где есть следующая информация:
            - d категории
            - наименование категории
            - описание категории
            - список продуктов, относящихся к этой категории"""
    conn = psycopg2.connect(
        host=config.get('host'),
        database=config.get('database'),
        user=config.get('user'),
        password=config.get('password')
    )
    try:
        with conn:
            with conn.cursor() as cur:  # закрывает курсор
                req = f"SELECT category_id, category_name, description, product_name as list_product_name FROM products " \
                      f"INNER JOIN categories USING (category_id) " \
                      f"WHERE products.category_id = 7;"
                cur.execute(req)
                row = cur.fetchall()
                array_ = [i[3] for i in row]
                return [{"product_id": row[0][0], "product_name": row[0][1], "category_name": row[0][2],
                         "list_product_name": array_}]
    finally:
        conn.close()


config = {
    "host": "localhost",
    "database": "Northwind_Traders ",
    "user": "postgres",
    "password": "12345"
}

print(get_product_by_id(config, 5))
print(get_category_by_id(config, 7))
