COPY campaigns(campaign_id, campaign_name, start_date, end_date, channel, discount_type, discount_value)
FROM 'C:/Users/ASUS/Documents/3 курс/1 тримак/Data Visualization/archive/dataset_fashion_store_campaigns.csv'
DELIMITER ','
CSV HEADER;

COPY channels(channel, description)
FROM 'C:/Users/ASUS/Documents/3 курс/1 тримак/Data Visualization/archive/dataset_fashion_store_channels.csv'
DELIMITER ','
CSV HEADER;

COPY customers(customer_id, country, age_range, signup_date)
FROM 'C:/Users/ASUS/Documents/3 курс/1 тримак/Data Visualization/archive/dataset_fashion_store_customers.csv'
DELIMITER ','
CSV HEADER;

COPY products(product_id, product_name, category, brand, color, size, catalog_price, cost_price, gender)
FROM 'C:/Users/ASUS/Documents/3 курс/1 тримак/Data Visualization/archive/dataset_fashion_store_products.csv'
DELIMITER ','
CSV HEADER;

COPY stock(country, product_id, stock_quantity)
FROM 'C:/Users/ASUS/Documents/3 курс/1 тримак/Data Visualization/archive/dataset_fashion_store_stock.csv'
DELIMITER ','
CSV HEADER;

COPY sales(sale_id, channel, discounted, total_amount, sale_date, customer_id, country)
FROM 'C:/Users/ASUS/Documents/3 курс/1 тримак/Data Visualization/archive/dataset_fashion_store_sales.csv'
DELIMITER ','
CSV HEADER;

COPY sales_items(item_id, sale_id, product_id, quantity, original_price, unit_price, discount_applied, discount_percent, discounted, item_total, sale_date, channel, channel_campaigns)
FROM 'C:/Users/ASUS/Documents/3 курс/1 тримак/Data Visualization/archive/dataset_fashion_store_salesitems.csv'
DELIMITER ','
CSV HEADER;
