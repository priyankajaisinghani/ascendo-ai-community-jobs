# Ascendo AI Community Jobs

## Overview
Ascendo AI Community Jobs is a lightweight AI-powered job aggregation tool designed to help Field Service professionals discover relevant job opportunities in one place. The platform aggregates jobs from multiple sources and supports community-driven enrichment.

## Features
- Aggregates Field Service job listings
- Displays jobs in a simple searchable interface
- Simulated hourly refresh with timestamp
- Allows users to add new job sources
- Designed for content sharing and community growth

## Tech Stack
- Python
- Streamlit
- Pandas
- CSV-based storage

## How It Works
1. Job data is collected from sample datasets and public sources.
2. Listings are normalized into a single structure.
3. Jobs are refreshed via a simulated refresh mechanism.
4. Users can add new job sources for future refresh cycles.

## How to Run
```bash
pip install streamlit pandas
streamlit run app.py
