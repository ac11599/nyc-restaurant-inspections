# NYC Restaurant Inspections Analysis

An exploratory data analysis project for Urban Data Science examining restaurant inspection records in New York City, with an initial focus on Queens.

## Project Overview

This project analyzes NYC Department of Health restaurant inspection data to uncover patterns in food safety across the city. The analysis covers inspection scores and grades, health violations and critical flags, and cuisine type trends — starting with Queens and expanding to all five boroughs.

## Data Source

Data is pulled directly from NYC Open Data. No local data files are needed — the notebook fetches the latest data at runtime.

## Project Structure

```
nyc-restaurant-inspections/
├── NYC-restaurant-inspections.ipynb    # Main analysis notebook
├── streamlit_app.py                    # Interactive Streamlit dashboard
├── requirements.txt                    # Python dependencies
└── README.md
```

## Tools and Libraries

- Python, Jupyter Notebook
- `pandas` — data manipulation
- `matplotlib` / `seaborn` — data visualization
- `scikit-learn` — data analysis
- `requests` — API data fetching
- `streamlit` — interactive dashboard

