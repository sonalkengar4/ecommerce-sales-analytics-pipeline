# 🛒 Zero-Cost E-Commerce Sales Analytics Pipeline

## 📌 Project Overview

This project demonstrates a zero-cost end-to-end data analytics pipeline for an e-commerce dataset using:

- Python
- SQLite (lightweight database)
- Pandas
- AWS S3 (for cloud storage)

The objective is to simulate a real-world data pipeline without using paid database services.

---

## 🏗 Architecture

Raw CSV → SQLite → SQL Queries → Pandas Transformations → Processed CSV → AWS S3

---

## ⚙️ Tech Stack

- Python 3.10+
- Pandas
- NumPy
- SQLite (built-in with Python)
- Boto3 (AWS SDK)

---

## 📂 Project Structure
ecommerce-sales-analytics-pipeline/
│
├── data/
│ ├── raw/
│ └── processed/
│
├── src/
│ ├── sqlite_loading.py
│ ├── sql_queries.py
│ └── data_transformation.py
│
├── requirements.txt
└── README.md

---

## 🚀 How to Run This Project

### 1️⃣ Clone Repository

```bash
git clone https://github.com/sonalkengar4/ecommerce-sales-analytics-pipeline.git
cd ecommerce-sales-analytics-pipeline

**Install Dependencies**

pip install -r requirements.txt

**Run Scripts**

python src/sqlite_loading.py
python src/sql_queries.py
python src/data_transformation.py

**Processed file will be generated inside:**

data/processed/

-----

📊 Key Features

Zero-cost local database setup using SQLite

SQL-based data extraction

Pandas-based transformation

Clean project structure

Cloud storage integration with AWS S3

🎯 Learning Outcomes

Data pipeline structuring

SQL + Pandas integration

Environment dependency management

GitHub project organization

Basic cloud integration (AWS S3)

---

👤 Author

Sonalkengar
Aspiring Data Engineer
