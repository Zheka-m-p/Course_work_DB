SELECT COUNT(*) FROM customers; -- Посчитать количество заказчиков

SELECT DISTINCT (city, country) from customers;  --Выбрать все уникальные сочетания городов и стран, в которых "зарегестрированы" заказчики

-- Найти заказчиков и обслуживающих их заказы сотрудников, таких, что и заказчики и сотрудники из города London,
--а доставка идёт компанией Speedy Express. Вывести компанию заказчика и ФИО сотрудника
SELECT customers.company_name, CONCAT(first_name, ' ', last_name) FROM orders  --
JOIN customers USING(customer_id)
JOIN employees USING(employee_id)
JOIN shippers ON (orders.ship_via = shippers.shipper_id)
WHERE employees.city = 'London' AND customers.city = 'London' AND shippers.company_name = 'Speedy Express';

SELECT  contact_name, order_id  FROM orders -- Найти заказчиков, не сделавших ни одного заказа. Вывести имя заказчика и order_id.
RIGHT JOIN customers USING(customer_id)
WHERE  customer_id not in (SELECT DISTINCT customer_id FROM orders
					ORDER BY customer_id)
ORDER BY contact_name;