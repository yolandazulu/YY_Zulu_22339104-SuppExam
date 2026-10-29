# Ekurhuleni Women-Safety Analytics & Hotspot Classification
**TPRO200**

- **Candidate:** Y.Y. Zulu
- **Student Number:** `22339104`
- **Study Area:** City of Ekurhuleni Metropolitan Municipality (39 Official SAPS Police Precincts, Gauteng, South Africa)

---

## 1. Project Overview
This repository contains an end-to-end machine learning, spatial analysis, and interactive visualisation solution for identifying women-safety and violent crime hotspots and patterns across the 39 police precincts of Ekurhuleni over **21 consecutive quarters (`2021-2022 Q1` to `2026-2027 Q1`)**.

### Official Open Data Sources
1. **SAPS Quarterly Crime Statistics (2021/22 Q1 – 2026/27 Q1):** [https://www.saps.gov.za/services/crimestats.php](https://www.saps.gov.za/services/crimestats.php)
2. **SAPS GIS Police Station Boundaries & Coordinates:** [https://www.saps.gov.za/services/boundary.php](https://www.saps.gov.za/services/boundary.php)

---

## 2. Repository Structure
- `YY_Zulu_22339104.ipynb` / `YY_Zulu_22339104 (1).ipynb` — Complete, step-by-step executed Jupyter Notebook with plain-English explanations, data quality checks, spatial feature engineering (`EPSG:32735`), EDA, leakage-free hotspot classification, K-Means risk clustering, Z-score anomaly detection, 3-hotspot deep-dive comparison (`Kempton Park`, `Tembisa`, `Germiston`), algorithmic complexity analysis, and AI prompts log.
- `app.py` — Interactive Streamlit dashboard for exploring spatial hotspots, seasonal patterns, model performance metrics, and prevention insights.
- `ekurhuleni_panel_data.csv` — Cleaned 4,914-row station-quarter-category panel dataset with spatial densities, lagged features, hotspot flags, anomaly Z-scores, and model predictions.
- `ekurhuleni_station_summary.csv` — Station-level summary table with surface area ($\text{km}^2$), K-Means risk cluster tiers, and mean category densities.
- `ekurhuleni_boundaries.geojson` — Ekurhuleni police precinct polygons for interactive choropleth mapping.
- `model_metrics.json` — Saved evaluation metrics (Confusion Matrices, Classification Reports, ROC curves, Permutation Feature Importances).
- `requirements.txt` — Open-source Python dependencies.

---

## 3. Running the Streamlit Dashboard Locally
```bash
pip install -r requirements.txt
python -m streamlit run app.py
```
Then open **http://localhost:8501** in your web browser.
