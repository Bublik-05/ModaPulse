-- 1. Общий объём продаж по каналам
SELECT s.channel AS channel_name, SUM(s.total_amount) AS total_sales
FROM sales s
GROUP BY s.channel
ORDER BY total_sales DESC;

-- 2. Топ-5 самых популярных товаров
SELECT p.product_name, SUM(si.quantity) AS total_sold
FROM sales_items si
JOIN products p ON si.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC
LIMIT 5;

-- 3. Количество клиентов по странам
SELECT country, COUNT(*) AS num_customers
FROM customers
GROUP BY country
ORDER BY num_customers DESC;

-- 4. ROI кампаний: доход – "бюджет" (discount_value) ?????
SELECT c.campaign_name, c.discount_value AS budget, SUM(si.item_total) AS revenue,
       SUM(si.item_total) - c.discount_value AS roi
FROM campaigns c
LEFT JOIN sales_items si ON si.channel_campaigns = c.campaign_name
GROUP BY c.campaign_name, c.discount_value
ORDER BY roi DESC;

-- 5. Средний чек по каналам продаж
SELECT s.channel AS channel_name, AVG(s.total_amount) AS avg_order_value
FROM sales s
GROUP BY s.channel
ORDER BY avg_order_value DESC;

-- 6. Кол-во продаж по месяцам (год+месяц)
SELECT DATE_TRUNC('month', sale_date) AS month, COUNT(*) AS sales_count
FROM sales
GROUP BY DATE_TRUNC('month', sale_date)
ORDER BY month;

-- 7. Склад: товары с остатком меньше 10
SELECT p.product_name, st.stock_quantity
FROM stock st
JOIN products p ON st.product_id = p.product_id
WHERE st.stock_quantity < 10
ORDER BY st.stock_quantity;

-- 8. 10 самых прибыльных клиентов
SELECT s.customer_id, COUNT(*) AS num_orders, SUM(s.total_amount) AS total_spent
FROM sales s
GROUP BY s.customer_id
ORDER BY total_spent DESC
LIMIT 10;

-- 9. Топ-5 категорий с самой высокой средней цены продажи
SELECT p.category, AVG(si.unit_price) AS avg_unit_price
FROM sales_items si
JOIN products p ON si.product_id = p.product_id
GROUP BY p.category
ORDER BY avg_unit_price DESC
LIMIT 5;

-- 10. Продажи по категориям товаров 
SELECT p.category, SUM(si.quantity) AS total_units, SUM(si.unit_price*si.quantity) AS total_revenue
FROM sales_items si
JOIN products p ON si.product_id = p.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;
