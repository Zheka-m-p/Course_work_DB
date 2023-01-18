SELECT * FROM orders -- Выбрать все заказы, отсортировать по required_date (по убыванию) и отсортировать по дате отгрузке (по возрастанию)
ORDER BY required_date DESC, shipped_date; -- Если, конечно правильно понял условие, то второй столбец такой

SELECT AVG(shipped_date - order_date) as avg_delivery_date FROM orders -- Найти среднее значение дней уходящих на доставку с даты формирования заказа в USA
WHERE ship_country = 'USA';

-- Найти сумму, на которую имеется товаров (количество * цену) причём таких, которые не сняты с продажи (см. на поле discontinued)
SELECT SUM(unit_price * units_in_stock) as total_sum FROM products
WHERE discontinued != 1;