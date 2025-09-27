-- Создание схемы базы данных для Fashion Store
DROP TABLE IF EXISTS sales_items;
DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS stock;
DROP TABLE IF EXISTS campaigns;
DROP TABLE IF EXISTS channels;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS products;


CREATE TABLE campaigns (
    campaign_id INT,
    campaign_name VARCHAR(255),
    start_date DATE,
    end_date DATE,
    channel VARCHAR(255),
    discount_type VARCHAR(50),
    discount_value NUMERIC
);

CREATE TABLE channels (
    channel VARCHAR(255),
    description TEXT
);

CREATE TABLE customers (
    customer_id INT,
    country VARCHAR(100),
    age_range VARCHAR(50),
    signup_date DATE
);

CREATE TABLE products (
    product_id INT,
    product_name VARCHAR(255),
    category VARCHAR(100),
    brand VARCHAR(100),
    color VARCHAR(50),
    size VARCHAR(20),
    catalog_price NUMERIC,
    cost_price NUMERIC,
    gender VARCHAR(10)
);

CREATE TABLE stock (
    country VARCHAR(100),
    product_id INT,
    stock_quantity INT
);

CREATE TABLE sales (
    sale_id INT,
    channel VARCHAR(255),
    discounted BOOLEAN,
    total_amount NUMERIC,
    sale_date DATE,
    customer_id INT,
    country VARCHAR(100)
);

CREATE TABLE sales_items (
    item_id INT,
    sale_id INT,
    product_id INT,
    quantity INT,
    original_price NUMERIC,
    unit_price NUMERIC,
    discount_applied BOOLEAN,
    discount_percent NUMERIC,
    discounted BOOLEAN,
    item_total NUMERIC,
    sale_date DATE,
    channel VARCHAR(255),
    channel_campaigns VARCHAR(255)
);