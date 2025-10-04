# ModaPulse
Modapulsa Analytics is the analytics department of a large fashion retail chain. We study sales, product assortment, and customer behavior to improve product assortment, forecast demand, and optimize store operations.

The goal is to perform a comprehensive analysis of fashion retail data to identify patterns and trends in product sales, customer segments, and regional performance.

## ERD Diagram
<img width="637" height="942" alt="Снимок экрана (163)" src="https://github.com/user-attachments/assets/6c57e77e-cd17-4ed0-a1b5-8f49008b57a1" />



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
- `data.sql` — SQL script for importing CSV data into PostgreSQL  
- `queries.sql` — 10 analytical SQL queries (with short comments)  
- `main.py` — Python script to connect to the database and execute basic queries (Assignment 1)  
- `analytics.py` — main analytical module with SQL execution, data visualization, and export to Excel (Assignment 2)  
- `config.py` — database connection configuration (user, password, host, port, dbname)  
- `requirements.txt` — Python dependencies (`pandas`, `matplotlib`, `openpyxl`, `psycopg2`, etc.)  
- `archive/` — CSV files from the Kaggle dataset (may be stored as ZIP archive)  
- `charts/` — generated graphs and plots (e.g., revenue trends, top categories)  
- `exports/` — Excel reports with formatting and filters  
- `README.md` — project documentation with setup and analysis instructions  
  
## Quick setup & run instructions

### 1. Prerequisites

* macOS / Linux / Windows
* PostgreSQL 14+ installed and running
* Python 3.10+
* Git (optional: GitHub CLI `gh`)
* VS Code / PyCharm (any code editor)

### 2. Clone the repository

```bash
git clone git@github.com:Bublik-05/ModaPulse.git
cd ModaPuls
pip install -r requirements.txt
```

### 3. Create Python virtual environment and install dependencies

```bash
python -m venv venv          # create virtual environment
# macOS / Linux:
source venv/bin/activate     
# Windows PowerShell:
.\venv\Scripts\Activate.ps1  
pip install -r requirements.txt
```

### 4. Create PostgreSQL database

```sql
-- open psql shell
CREATE DATABASE fashion_store;
\c fashion_store
```

### 5. Import database schema

```bash
psql -U <username> -d fashion_store -f schema.sql
```

### 6. Load CSV data into tables

```bash
psql -U <username> -d fashion_store -f data.sql
```

> ⚠ Make sure the CSV files are in `archive/` folder and paths in `data.sql` match your local folder structure.

### 7. Run Python script to execute queries

```bash
python main.py
```

> The script will connect to your PostgreSQL database, execute the queries from `queries.sql`, and display the results using `pandas`.

### 8. Optional tools

* Use **VS Code / PyCharm** to explore and edit the project.
* Optionally, connect **Apache Superset** or other BI tools to visualize the data.


---

## Analytical Module (Assignment 2)

After the database setup and data import (Assignment 1), this stage focuses on **data analysis, visualization, and exporting analytical reports**.

### Goals of the Analysis

In this stage, we explore the following key business questions:

- Which **categories and brands** generate the most revenue?  
- How do **sales vary by region and sales channel** (online/offline)?  
- What is the **impact of marketing campaigns** on sales volume?  
- Who are the **main customer segments** (by gender, age, purchase frequency)?  
- How does **demand change over time**?

---

### How to Run the Analysis

Make sure your PostgreSQL database is active and filled with data from the first assignment.  
Then, run the script:

```bash
python analytics.py
```
### Results and Output Structure

After running analytics.py, new results will appear inside these folders:

#### 1. charts/

Stores visualization images generated using matplotlib or seaborn:

* top_categories.png — revenue by category

* sales_trend.png — sales trend over time

* campaign_effect.png — comparison of sales during campaigns

#### 2. exports/

Contains formatted Excel reports, e.g.:
```bash
exports/
└── fashion_report.xlsx
```

Each Excel sheet corresponds to a different analysis topic, such as:

* Top Categories

* Sales by Channel

* Customers Overview

The report includes:

* Frozen headers (freeze_panes)

* Filters on all columns

* Conditional color formatting (min/max values)

* Gradient fills for numerical columns


## Tools & resources

* PostgreSQL 14 (server)

* Python 3.10+, pip

* psycopg2-binary, pandas, sqlalchemy

* VS Code for editing


## Project author: Pernebek Abylay
