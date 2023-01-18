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


def data_for_write_in_table(file_name):
    ''' Функция для подгтовки данных, которые мы потом будем загружать в таблицу. Возвращает список кортежей. '''
    with open(file_name) as f:
        ans, count = [], 1
        data = json.load(f)
        for elem in data:
            split_adress = elem['address'].split(';')[::-1]  # разобьём адресс для нормализации таблицы
            split_adress = [i.strip() for i in split_adress]  # удаляем крайние пробелы и табуляцию(если есть)
            split_adress[2], split_adress[3] = split_adress[3], split_adress[2]  # меняем на правильный порядок
            tmp = []  # массив, который мы заполним, а потом преобразуем в кортеж
            tmp.extend([elem['company_name'], *elem['contact'].split(','), *split_adress, elem['phone'], elem['fax'],
                        elem['homepage'], elem['products']])  # подготавливаем данные
            tmp = tuple([count] + tmp)
            count += 1
            ans.append(tmp)
    return ans


assert verification_of_the_uniqueness_of_the_goods_of_suppliers() == True
conn = psycopg2.connect(host='localhost', database='Northwind_Traders ', user='postgres', password='12345')
try:
    with conn:
        with conn.cursor() as cur:  # закрывает курсор
            many_s = ('%s ,' * 13)[:-2]  # перееменная, чтобы не писать 13 раз %s
            cur.executemany(f"INSERT INTO suppliers VALUES({many_s})", data_for_write_in_table('suppliers.json'))

finally:
    conn.close()
