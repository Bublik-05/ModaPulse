-- 1. Top-selling products by total quantity sold
SELECT 
    p.product_name,
    p.category,
    SUM(si.quantity) AS total_sold
FROM sales_items si
JOIN products p ON si.product_id = p.product_id
GROUP BY p.product_name, p.category
ORDER BY total_sold DESC
LIMIT 10;

-- 2. Total sales revenue per country
SELECT 
    s.country,
    ROUND(SUM(s.total_amount), 2) AS total_revenue
FROM sales s
GROUP BY s.country
ORDER BY total_revenue DESC;

-- 3. Average order value per customer by country
SELECT
    s.country,
    ROUND(AVG(s.total_amount), 2) AS avg_order_value
FROM sales s
WHERE s.total_amount > 0
GROUP BY s.country
ORDER BY avg_order_value DESC
LIMIT 10;


-- 4. Stock levels by category (average stock per product)
SELECT 
    p.category,
    ROUND(AVG(st.stock_quantity), 2) AS avg_stock
FROM stock st
JOIN products p ON st.product_id = p.product_id
GROUP BY p.category
ORDER BY avg_stock DESC;

-- 5. Revenue by sales channel
SELECT 
    s.channel,
    ROUND(SUM(s.total_amount), 2) AS revenue
FROM sales s
GROUP BY s.channel
ORDER BY revenue DESC;

-- 6. Product profitability (catalog price - cost price)
SELECT 
    p.category,
    ROUND(AVG(p.catalog_price - p.cost_price), 2) AS avg_profit_margin
FROM products p
GROUP BY p.category
ORDER BY avg_profit_margin DESC
LIMIT 10;

-- 7. Изменение продаж по категориям со временем
SELECT
    p.category,
    DATE_TRUNC('month', si.sale_date) AS month,
    SUM(si.item_total) AS total_sales
FROM sales_items si
JOIN products p ON si.product_id = p.product_id
WHERE si.sale_date IS NOT NULL
GROUP BY p.category, month
ORDER BY month, total_sales DESC;
