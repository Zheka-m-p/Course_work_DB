import json
import psycopg2


def verification_of_the_uniqueness_of_the_goods_of_suppliers():
    """ Функция порверят уникальны ли товары у каждого постовщика
        Возвращает True, если уникальны, иначе - False """
    with open('suppliers.json') as f:
        data = json.load(f)
        len_all_products = 0  # количество товаров всего
        set_products = set()
        for sample in data:
            products = (sample['products'])
            len_all_products += len(products)  # суммируем общее количество товаров
            set_products.update(set(products))  # добавляем во множество товары из каждого поставщика
    return len_all_products == len(set_products)  # убеждаемся, что число товаров совпало


assert verification_of_the_uniqueness_of_the_goods_of_suppliers() == True

# with open('suppliers.json') as f:
#     data = json.load(f)
#     print(type(data))

many_s = ('%s ,' * 13)[:-2]
print(many_s)
print(f"INSERT INTO suppliers VALUES({many_s})")

conn = psycopg2.connect(host='localhost', database='Northwind_Traders ', user='postgres', password='12345')
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaa. В название базы когда копировал в конце поставился пробела, диииииичччь, ахахах)))
try:
    with conn:
        with conn.cursor() as cur:  # закрывает курсор
            many_s = ('%s ,' * 13)[:-2]  # перееменная, чтобы не писать 13 раз %s
            cur.execute("SELECT * FROM products")
            rows = cur.fetchall()
            for row in rows:
                print(row)

finally:
    conn.close()

