##  Project Overview

This project is an **End-to-End Data Engineering & Analysis pipeline** designed to process and explore over **128,000+ records** of Amazon sales data in India. It demonstrates a professional workflow of transforming raw, inconsistent data into a structured SQLite database for high-performance querying and business intelligence.

##  Project Structure

The project follows a modular software engineering approach to ensure reusability and maintainability:

```text
ecommerce-analysis/
├── data/
│   ├── raw/                  # Original, unaltered CSV dataset
│   └── cleaned/              # Processed data ready for analysis
├── notebooks/
│   ├── 01_explore.ipynb      # Initial data discovery & profiling
│   ├── 02_clean.ipynb        # Interactive cleaning & logic testing
│   └── 03_analyze.ipynb      # Advanced SQL analysis & BI reporting
├── src/                      # Production-ready Python scripts
│   ├── clean.py              # Automated ETL & Transformation logic
│   └── db.py                 # Database connectivity layer (SQLAlchemy)
├── requirements.txt          # Project dependencies
└── README.md                 # Technical documentation

```

##  Tech Stack & Skills:

* **Core Language:** **Python 3.14**
 **Data Manipulation & ETL:**
* **Pandas:** The primary tool used for data loading, cleaning, and transformation logic.

**Database & Persistence:**
* **SQLAlchemy:** Used as the database toolkit to bridge Python with SQL.
* **SQLite:** The relational database engine used to store and query the processed records.

**Data Visualization:**
* **Matplotlib:** For creating static plots and figures.
* **Seaborn:** For advanced statistical visualizations and heatmaps.

**Environment & Automation:**
* **Jupyter Notebooks:** For interactive experimentation and EDA.
* **OS Module:** For managing file system paths and directory automation.



##  Data Engineering Highlights (The "How")

* **Automated ETL Pipeline:** Developed `clean.py` to automate the transformation of raw data into a standardized format.
* **Data Integrity Logic:** Implemented custom business rules, such as synchronizing `courier_status` with `order_status` to ensure logical consistency across 128k+ rows.
* **Advanced Mapping & Standardization:** Cleaned fragmented geographical data (e.g., mapping state codes like 'PB' to 'Punjab') to ensure accurate regional reporting.
* **Schema Optimization:** Migrated cleaned data to **SQLite** to leverage SQL indexing for faster retrieval compared to traditional CSV parsing.

##  Key Business Insights (The "What")

Through SQL-driven analysis in `03_analyze.ipynb`, the following insights were extracted:

* **Top Categories:** **'Set'** and **'Kurta'** are the primary revenue drivers.
* **Regional Demand:** **Bengaluru** and **Hyderabad** identified as the top-performing cities.
* **Risk Assessment:** Discovered a **14.59% cancellation rate** in the 'Set' category, highlighting a specific area for logistics optimization.
* **Fulfillment Trends:** Analysis shows a high reliance on **Expedited Shipping**, correlating with higher average order values.

##  How to Run

1. **Install Dependencies:**
```bash
pip install -r requirements.txt

```


2. **Run the Cleaning Pipeline:**
```bash
python src/clean.py

```


3. **Explore Analysis:** Open `notebooks/03_analyze.ipynb` to view the SQL queries and results.


