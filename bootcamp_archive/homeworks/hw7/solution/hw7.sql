INSERT INTO resturants (id, name, adress, city, cuisine_type, rating, status) VALUES
(1, 'Pizza Planet', '123 Star Ln', 'Metro City', 'Italian', 5, 1),
(2, 'Burger Barn', '456 Farm Rd', 'Metro City', 'American', 4, 1),
(3, 'Sushi Samurai', '789 Dojo St', 'Metro City', 'Japanese', 5, 1),
(4, 'The Ghost Kitchen', '000 Void Ave', 'Lost Town', 'Mystery', 1, 1);

INSERT INTO menu_items (item_id, name, description, category, price, resturant_id) VALUES
(1, 'Pepperoni Pizza', 'Classic cheese and pep', 'Main', 15, 1),
(2, 'Garlic Knots', 'Buttery goodness', 'Sides', 5, 1),
(3, 'Cheeseburger', 'Juicy beef patty', 'Main', 12, 2),
(4, 'French Fries', 'Crispy golden potatoes', 'Sides', 4, 2),
(5, 'Dragon Roll', 'Eel and avocado', 'Main', 18, 3),
(6, 'Miso Soup', 'Warm soybean broth', 'Sides', 3, 3);

INSERT INTO customers (id, name, email, phone_number, registration_date) VALUES
(1, 'Big Eater', 'hungry@email.com', '555-0101', '2025-01-10 10:00:00'),
(2, 'One-Time Olga', 'olga@email.com', '555-0102', '2025-02-15 11:30:00'),
(3, 'Silent Sam', 'sam@email.com', '555-0103', '2025-03-01 09:15:00');

INSERT INTO orders (id, date, status, delivery_address, resturant_id, customer_id) VALUES
(1, '2026-01-15 18:30:00', 'Delivered', '101 Apt A', 1, 1), -- Big Eater, Jan
(2, '2026-02-10 12:00:00', 'Delivered', '101 Apt A', 2, 1), -- Big Eater, Feb
(3, '2026-03-05 19:45:00', 'Delivered', '101 Apt A', 3, 1), -- Big Eater, March
(4, '2026-02-20 13:00:00', 'Cancelled', '202 South St', 1, 2), -- Olga, Cancelled
(5, '2026-03-08 20:00:00', 'Delivered', '303 North St', 2, 3); -- Silent Sam

INSERT INTO order_items (menu_item_id, quantity, order_id) VALUES
(1, 2, 1), -- 2 Pizzas for Order 1
(2, 1, 1), -- 1 Garlic Knot for Order 1
(3, 1, 2), -- 1 Burger for Order 2
(5, 1, 3), -- 1 Dragon Roll for Order 3
(1, 1, 4), -- 1 Pizza for Order 4 (Cancelled)
(4, 2, 5); -- 2 Fries for Order 5

INSERT INTO review (id, rating, comment, customer_id, order_id) VALUES
(1, 5, 'Best pizza ever!', 1, 1),
(2, 4, 'Good burger, a bit cold.', 1, 2),
(3, 1, 'My order never arrived!', 2, 4);

#1
SELECT * FROM resturants
ORDER BY resturants.name;

#2
SELECT * FROM menu_items
WHERE menu_items.price > 40
ORDER BY menu_items.price desc;

#3
SELECT * FROM resturants
where resturants.name LIKE '%burger%';

#4
SELECT * FROM orders
WHERE orders.status = ('Delivered' or 'Cancelled');

#5
SELECT * FROM menu_items
WHERE menu_items.category = 'Dessert'
ORDER BY menu_items.price;

#6
SELECT * FROM customers
WHERE YEAR(customers.registration_date) = 2024;

#7
SELECT * FROM resturants
WHERE rating >= 4 AND status = 1;

#8
SELECT orders.*, customers.name AS 'CUSTOMER NAME', resturants.name AS 'RESTURANT NAME' FROM orders
JOIN customers ON customers.id = orders.customer_id
JOIN resturants ON resturants.id = orders.resturant_id;

#9 
SELECT resturants.*, COUNT(menu_items.resturant_id) AS 'number of menu items'FROM resturants
JOIN menu_items ON menu_items.resturant_id = resturants.id
GROUP BY menu_items.resturant_id
ORDER BY COUNT(menu_items.resturant_id) DESC;

#10
SELECT review.*, customers.name AS 'CUSTOMER NAME', resturants.name AS 'RESTURANT NAME' FROM  review
JOIN customers ON customers.id =  review.customer_id
JOIN orders ON orders.id = review.order_id
JOIN resturants ON resturants.id =  orders.resturant_id;

#11
SELECT orders.id, SUM(order_items.quantity * menu_items.price) AS 'total price', 
resturants.name AS 'resturant',
customers.name AS 'customer'
FROM orders
JOIN order_items ON orders.id = order_items.order_id
JOIN menu_items ON menu_items.item_id = order_items.menu_item_id
JOIN resturants ON orders.resturant_id = resturants.id
JOIN customers ON orders.customer_id = customers.id
GROUP BY orders.id;

#12
SELECT menu_items.resturant_id, MAX(menu_items.price) FROM menu_items
GROUP BY menu_items.resturant_id;

#13
SELECT orders.status, COUNT(orders.status) FROM orders
GROUP BY orders.status;

#14
SELECT customers.id FROM customers
JOIN orders ON customers.id = orders.customer_id
WHERE customers.id != orders.customer_id;

#15
SELECT orders.resturant_id, AVG(rating) FROM review
JOIN orders ON orders.id = review.order_id
GROUP BY orders.resturant_id
HAVING COUNT(review.id)>3;

#16
SELECT orders.customer_id, SUM(order_items.quantity * menu_items.price) AS total_price, 
customers.name AS 'customer'
FROM orders
JOIN order_items ON orders.id = order_items.order_id
JOIN menu_items ON menu_items.item_id = order_items.menu_item_id
JOIN customers ON orders.customer_id = customers.id
GROUP BY orders.customer_id, customers.name
ORDER BY total_price DESC
LIMIT 3;

#17
SELECT customer_id FROM orders
GROUP BY customer_id
HAVING COUNT(orders.customer_id)>3;

#18
SELECT 
    (SELECT COUNT(*) FROM resturants WHERE status = 1) AS active_restaurants,
    (SELECT COUNT(*) FROM customers) AS total_customers,
    (SELECT COUNT(*) FROM orders WHERE date LIKE '2026-03%') AS monthly_orders,
    (SELECT SUM(oi.quantity * mi.price) FROM order_items oi 
     JOIN menu_items mi ON oi.menu_item_id = mi.item_id
     JOIN orders o ON oi.order_id = o.id
     WHERE o.date LIKE '2026-03%') AS monthly_revenue,
     (SELECT SUM(oi.quantity * mi.price) / COUNT(DISTINCT o.id)
     FROM orders o
     JOIN order_items oi ON o.id = oi.order_id
     JOIN menu_items mi ON oi.menu_item_id = mi.item_id
     WHERE o.date LIKE '2026-03%') AS avg_order_value,
     (SELECT r.cuisine_type
     FROM resturants r
     JOIN orders o ON r.id = o.resturant_id
     JOIN order_items oi ON o.id = oi.order_id
     JOIN menu_items mi ON oi.menu_item_id = mi.item_id
     WHERE o.date LIKE '2026-03%'
     GROUP BY r.cuisine_type
     ORDER BY SUM(oi.quantity * mi.price) DESC
     LIMIT 1) AS top_cuisine;
     


