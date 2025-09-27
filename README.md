# ModaPulse
Modapulsa Analytics is the analytics department of a large fashion retail chain. We study sales, product assortment, and customer behavior to improve product assortment, forecast demand, and optimize store operations.

The goal is to perform a comprehensive analysis of fashion retail data to identify patterns and trends in product sales, customer segments, and regional performance.

## ERD Diagram
![Uploading image.png…]()



## Data Structure
<a href='https://www.kaggle.com/datasets/joycemara/european-fashion-store-multitable-dataset'>The dataset is composed of 7 relational tables, clean, consistent and interconnected. Below is a description of each one:</a>

customers: basic customer information  

sales: overall sale transactions

sales_items: detailed items within each sale

products: product catalog with attributes

stock: inventory levels of each product by store/channel

campaigns: marketing campaigns and promotions

channels: available sales channels

## Dataset  

Files (CSV) used in the project (stored in `archive/`):  

- **dataset_fashion_store_campaigns.csv** — marketing campaigns (discounts, start/end dates)  
- **dataset_fashion_store_channels.csv** — sales channels (online, offline, etc.)  
- **dataset_fashion_store_customers.csv** — customer demographics and registration  
- **dataset_fashion_store_products.csv** — product catalog (categories, brands, prices)  
- **dataset_fashion_store_sales.csv** — sales transactions (who, when, where)  
- **dataset_fashion_store_salesitems.csv** — items per sale (products, quantities, prices)  
- **dataset_fashion_store_stock.csv** — current stock levels by product and store  


## Contents of the repository

- `schema.sql` — CREATE TABLE statements for all tables  
- `queries.sql` — 10 analytical SQL queries (with short comments)  
- `main.py` — Python script to connect to the DB and run sample queries  
- `requirements.txt` — Python dependencies  
- `archive/` — CSV files (not included in repo if large)  
- `images/` — ER diagram  
- `data.sql` — importing CSV files
  
## Quick setup & run instructions

1. **Prerequisites**  
   - macOS / Linux / Windows  
   - PostgreSQL 14 (or compatible) installed and running  
   - Python 3.10+  
   - Git and optionally the GitHub CLI (gh)  
   - VS Code / PyCharm (или любой редактор кода)  

2. **Create virtual environment and install dependencies**  

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # macOS / Linux
   # Windows PowerShell:
   .\venv\Scripts\Activate.ps1
   pip install -r requirements.txt

3. **Create PostgreSQL database**



## Tools & resources

* PostgreSQL 14 (server)

* Python 3.10+, pip

* psycopg2-binary, pandas, sqlalchemy

* Apache Superset (optional dashboard)

* VS Code for editing


## Project author: Pernebek Abylay
