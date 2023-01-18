CREATE TABLE suppliers
(
	supplier_id serial PRIMARY KEY,
	company_name varchar(50),
	contact_name varchar(50),
	contact_title varchar(60),
	address varchar(100),
	city varchar(25),
	region varchar(25),
	postal_code varchar(25),
	country varchar(25),
	phone varchar(25),
	fax varchar(25),
	homepage text,
	products  varchar(50) array

);

-- СНАЧАЛА ВЫПОЛНЯЕМ ВОТ ДО СЮДА, А ПОТОМ (ПОСЛЕ ВЫПОЛНЕНИЯ ФАЙЛА 'fill_suppliers.py' ВСЁ ОСТАЛЬНОЕ)

ALTER TABLE products ADD COLUMN supplier_id int;  -- добавляем колонку supplier_id в таблицу products
-- строчкой ниже добавляем связь из таблицы product к таблицу suppliers
ALTER TABLE products ADD CONSTRAINT fk_products_suppliers  FOREIGN KEY(supplier_id) REFERENCES suppliers(supplier_id);

--aaaaaaaaaaaaaaaaaaaaaaaa. спустя три часа смог заполнить suppliers_id в products
UPDATE products set supplier_id = (
	SELECT supplier_id FROM suppliers
		WHERE products.product_name = ANY (products));