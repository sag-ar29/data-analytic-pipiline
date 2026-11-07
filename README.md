# Automated Data Ingestion & Analytics Pipeline

A Python data processing service utilizing **Pandas**, **NumPy**, and **SQLAlchemy** to clean, sanitize, aggregate, and persist structured datasets into relational databases.

## Architecture & Features
- **Data Ingestion & Hygiene:** Handles missing values, type coercions, and parses datetime timestamps.
- **Enrichment & Metrics:** Segments customer behaviors and calculates aggregation metrics (total spent, average order value, primary category).
- **Relational Persistence:** Automatically streams transformed tables into SQL storage.

## How to Run Locally

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Execute pipeline
python main.py
```
