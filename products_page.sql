SELECT product_name, units_in_stock, contact_name, phone FROM products
JOIN suppliers USING(supplier_id)
JOIN categories USING(category_id)
WHERE discontinued != 1 AND units_in_stock <  20 AND category_name IN ('Beverages', 'Seafood')
ORDER BY units_in_stock DESC;