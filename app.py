import os
import json
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# ==============================================================================
# Page Configuration
# ==============================================================================
st.set_page_config(
    page_title="Ekurhuleni Women-Safety Intelligence — Y.Y. Zulu (22339104)",
    page_icon="▲",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================================================================
# Vercel-Inspired Design System CSS Injection
# ==============================================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400&display=swap');

:root {
    --primary: #171717;
    --on-primary: #ffffff;
    --ink: #171717;
    --body: #4d4d4d;
    --mute: #888888;
    --hairline: #ebebeb;
    --hairline-strong: #a1a1a1;
    --canvas: #ffffff;
    --canvas-soft: #fafafa;
    --canvas-soft-2: #f5f5f5;
    --link: #0070f3;
    --link-deep: #0761d1;
    --link-bg-soft: #d3e5ff;
    --error: #ee0000;
    --error-soft: #f7d4d6;
    --error-deep: #c50000;
    --warning: #f5a623;
    --warning-soft: #ffefcf;
    --warning-deep: #ab570a;
    --violet: #7928ca;
    --violet-soft: #d8ccf1;
    --violet-deep: #4c2889;
    --cyan: #50e3c2;
    --cyan-soft: #aaffec;
    --cyan-deep: #29bc9b;
    --highlight-pink: #ff0080;
    --highlight-magenta: #eb367f;
    --font-sans: 'Geist', 'Inter', system-ui, -apple-system, sans-serif;
    --font-mono: 'Geist Mono', 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, monospace;
}

/* Global Canvas & Typography */
html, body, [class*="css"], .stApp {
    font-family: var(--font-sans) !important;
    background-color: var(--canvas-soft) !important;
    color: var(--ink) !important;
    font-feature-settings: "ss01", "ss02";
    -webkit-font-smoothing: antialiased;
}

::selection {
    background-color: var(--primary);
    color: #f2f2f2;
}

/* Enforce weight ceiling 600 & negative tracking on all headings */
h1, h2, h3, h4, h5, h6 {
    font-family: var(--font-sans) !important;
    font-weight: 600 !important;
    color: var(--ink) !important;
    letter-spacing: -0.96px !important;
}

.block-container {
    max-width: 1400px !important;
    padding-top: 2rem !important;
    padding-bottom: 4rem !important;
}

/* Sidebar App-Shell Styling */
section[data-testid="stSidebar"] {
    background-color: var(--canvas) !important;
    border-right: 1px solid var(--hairline) !important;
}

section[data-testid="stSidebar"] .stMarkdown p {
    font-size: 14px !important;
    line-height: 20px !important;
    letter-spacing: -0.28px !important;
    color: var(--body) !important;
}

/* Hero Band with Full-Bleed Multi-Stop Mesh Gradient Backdrop */
.v-hero-band {
    position: relative;
    overflow: hidden;
    background-color: var(--canvas);
    border-radius: 12px;
    padding: 48px 36px 40px 36px;
    margin-bottom: 28px;
    box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.08), 0px 2px 2px rgba(0, 0, 0, 0.04), 0px 8px 16px -4px rgba(0, 0, 0, 0.04);
}

.v-hero-mesh {
    position: absolute;
    top: -35%;
    left: -10%;
    right: -10%;
    height: 230px;
    background:
        radial-gradient(circle at 16% 30%, rgba(0, 124, 240, 0.20) 0%, rgba(0, 223, 216, 0.14) 28%, transparent 58%),
        radial-gradient(circle at 52% 20%, rgba(121, 40, 202, 0.18) 0%, rgba(255, 0, 128, 0.15) 32%, transparent 62%),
        radial-gradient(circle at 86% 35%, rgba(255, 77, 77, 0.18) 0%, rgba(249, 203, 40, 0.16) 32%, transparent 60%);
    filter: blur(28px);
    pointer-events: none;
    z-index: 0;
}

.v-hero-content {
    position: relative;
    z-index: 1;
    max-width: 960px;
}

.v-banner-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background-color: var(--canvas-soft);
    color: var(--body);
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    line-height: 16px;
    padding: 6px 12px;
    border-radius: 9999px;
    box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.08);
    margin-bottom: 16px;
}

.v-banner-dot {
    width: 7px;
    height: 7px;
    border-radius: 9999px;
    background: linear-gradient(135deg, #007cf0, #ff0080);
    display: inline-block;
}

.v-display-xl {
    font-family: var(--font-sans);
    font-size: 44px;
    font-weight: 600;
    line-height: 48px;
    letter-spacing: -2.2px;
    color: var(--ink);
    margin: 0 0 12px 0;
}

.v-display-lg {
    font-family: var(--font-sans);
    font-size: 32px;
    font-weight: 600;
    line-height: 40px;
    letter-spacing: -1.28px;
    color: var(--ink);
    margin: 0 0 8px 0;
}

.v-display-md {
    font-family: var(--font-sans);
    font-size: 24px;
    font-weight: 600;
    line-height: 32px;
    letter-spacing: -0.96px;
    color: var(--ink);
    margin: 0 0 6px 0;
}

.v-body-lg {
    font-family: var(--font-sans);
    font-size: 18px;
    font-weight: 400;
    line-height: 28px;
    letter-spacing: 0px;
    color: var(--body);
    margin: 0 0 24px 0;
}

.v-caption-mono {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    line-height: 16px;
    color: var(--mute);
    text-transform: uppercase;
    letter-spacing: 0px;
    margin-bottom: 6px;
}

/* Marketing Pill CTA Row (100px pill radius) */
.v-cta-row {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    align-items: center;
}

.v-btn-primary {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    height: 40px;
    padding: 0 18px;
    background-color: var(--primary);
    color: var(--on-primary) !important;
    font-family: var(--font-sans);
    font-size: 14px;
    font-weight: 500;
    line-height: 20px;
    border-radius: 100px;
    text-decoration: none !important;
    transition: opacity 0.15s ease;
}

.v-btn-primary:hover {
    opacity: 0.88;
}

.v-btn-secondary {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    height: 40px;
    padding: 0 18px;
    background-color: var(--canvas);
    color: var(--ink) !important;
    font-family: var(--font-sans);
    font-size: 14px;
    font-weight: 500;
    line-height: 20px;
    border-radius: 100px;
    box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.12), 0px 1px 2px rgba(0, 0, 0, 0.04);
    text-decoration: none !important;
}

.v-btn-secondary:hover {
    background-color: var(--canvas-soft);
}

/* Cards & Elevation (Stacked Shadows + Inset 1px Hairline) */
.v-card {
    background-color: var(--canvas);
    color: var(--ink);
    border-radius: 8px;
    padding: 20px 22px;
    box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.08), 0px 2px 2px rgba(0, 0, 0, 0.04), 0px 8px 8px -8px rgba(0, 0, 0, 0.04);
    margin-bottom: 16px;
}

.v-card-featured {
    background-color: var(--primary);
    color: var(--on-primary);
    border-radius: 8px;
    padding: 20px 22px;
    box-shadow: 0 0 0 1px rgba(255, 255, 255, 0.12), 0px 2px 2px rgba(0, 0, 0, 0.08), 0px 8px 16px -4px rgba(0, 0, 0, 0.12);
    margin-bottom: 16px;
}

.v-card-soft {
    background-color: var(--canvas-soft);
    color: var(--ink);
    border-radius: 8px;
    padding: 18px 22px;
    box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.08);
    margin-bottom: 16px;
}

.v-kpi-value {
    font-family: var(--font-sans);
    font-size: 28px;
    font-weight: 600;
    line-height: 34px;
    letter-spacing: -1.1px;
    margin: 4px 0 6px 0;
}

.v-badge {
    display: inline-block;
    font-family: var(--font-mono);
    font-size: 11px;
    font-weight: 400;
    line-height: 16px;
    padding: 2px 8px;
    border-radius: 9999px;
    background-color: var(--canvas-soft-2);
    color: var(--body);
    box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.06);
}

.v-badge-blue {
    background-color: var(--link-bg-soft);
    color: var(--link-deep);
}

.v-badge-red {
    background-color: var(--error-soft);
    color: var(--error-deep);
}

.v-badge-amber {
    background-color: var(--warning-soft);
    color: var(--warning-deep);
}

.v-badge-violet {
    background-color: var(--violet-soft);
    color: var(--violet-deep);
}

.v-badge-dark {
    background-color: rgba(255, 255, 255, 0.14);
    color: #ffffff;
}

/* 3-Up Pricing/Precinct Tier Cards */
.v-tier-card {
    background-color: var(--canvas);
    color: var(--ink);
    border-radius: 12px;
    padding: 28px 24px;
    box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.08), 0px 2px 2px rgba(0, 0, 0, 0.04), 0px 8px 16px -4px rgba(0, 0, 0, 0.04);
    height: 100%;
}

.v-tier-card-featured {
    background-color: var(--primary);
    color: var(--on-primary);
    border-radius: 12px;
    padding: 28px 24px;
    box-shadow: 0 0 0 1px rgba(255, 255, 255, 0.15), 0px 8px 24px -4px rgba(0, 0, 0, 0.18);
    height: 100%;
}

.v-tier-row {
    display: flex;
    justify-content: space-between;
    padding: 8px 0;
    border-bottom: 1px solid var(--hairline);
    font-size: 14px;
    line-height: 20px;
    letter-spacing: -0.28px;
}

.v-tier-row-dark {
    display: flex;
    justify-content: space-between;
    padding: 8px 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.14);
    font-size: 14px;
    line-height: 20px;
    letter-spacing: -0.28px;
    color: #e5e5e5;
}

/* Polarity-Flipped Dark Showcase Band & Code Mockup */
.v-showcase-dark {
    background-color: var(--primary);
    color: var(--on-primary);
    border-radius: 12px;
    padding: 36px 32px;
    margin-top: 20px;
    margin-bottom: 20px;
}

.v-code-mockup {
    background-color: #0a0a0a;
    color: #f2f2f2;
    font-family: var(--font-mono);
    font-size: 13px;
    line-height: 20px;
    border-radius: 8px;
    padding: 20px 24px;
    box-shadow: 0 0 0 1px rgba(255, 255, 255, 0.14);
    overflow-x: auto;
    margin-top: 14px;
}

/* Tab-Ghost Pill Styling (64px pill radius) */
div[data-testid="stTabs"] button[data-baseweb="tab"] {
    font-family: var(--font-sans) !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    letter-spacing: -0.28px !important;
    border-radius: 64px !important;
    padding: 6px 16px !important;
    margin-right: 8px !important;
    background-color: var(--canvas) !important;
    color: var(--body) !important;
    border: 1px solid var(--hairline) !important;
    transition: all 0.15s ease !important;
}

div[data-testid="stTabs"] button[data-baseweb="tab"][aria-selected="true"] {
    background-color: var(--primary) !important;
    color: var(--on-primary) !important;
    border-color: var(--primary) !important;
}

div[data-testid="stTabs"] div[data-baseweb="tab-highlight"] {
    display: none !important;
}

div[data-testid="stTabs"] div[data-baseweb="tab-border"] {
    background-color: var(--hairline) !important;
}

/* Plotly Chart Container Card Chrome */
div[data-testid="stPlotlyChart"] {
    background-color: var(--canvas);
    border-radius: 8px;
    padding: 8px;
    box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.08), 0px 2px 2px rgba(0, 0, 0, 0.04);
}
</style>
""", unsafe_allow_html=True)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@st.cache_data
def load_all_data():
    panel_path = os.path.join(BASE_DIR, "ekurhuleni_panel_data.csv")
    station_path = os.path.join(BASE_DIR, "ekurhuleni_station_summary.csv")
    geojson_path = os.path.join(BASE_DIR, "ekurhuleni_boundaries.geojson")
    metrics_path = os.path.join(BASE_DIR, "model_metrics.json")

    panel_df = pd.read_csv(panel_path)
    station_df = pd.read_csv(station_path)
    with open(geojson_path, "r", encoding="utf-8") as f:
        geojson_data = json.load(f)
    with open(metrics_path, "r", encoding="utf-8") as f:
        metrics_data = json.load(f)

    return panel_df, station_df, geojson_data, metrics_data

panel_df, station_df, geojson_data, metrics_data = load_all_data()

# Unified Vercel Plotly Chart Styling Helper
VERCEL_PALETTE = ["#171717", "#0070f3", "#7928ca", "#ff0080", "#29bc9b", "#f5a623", "#ee0000"]
CLUSTER_COLOR_MAP = {
    "Tier 1 (Critical Density)": "#ee0000",
    "Tier 2 (Elevated Commercial/Transit)": "#7928ca",
    "Tier 3 (Low Density Peri-Urban)": "#0070f3"
}

def style_vercel_fig(fig, title_text, height=430):
    if title_text and not title_text.endswith("."):
        title_text = title_text + "."
    fig.update_layout(
        title=dict(
            text=title_text,
            font=dict(family="Geist, Inter, system-ui, sans-serif", size=17, color="#171717"),
            x=0.01,
            y=0.96
        ),
        font=dict(family="Geist, Inter, system-ui, sans-serif", size=12, color="#4d4d4d"),
        paper_bgcolor="#ffffff",
        plot_bgcolor="#ffffff",
        height=height,
        margin=dict(l=16, r=16, t=52, b=20),
        legend=dict(
            bgcolor="rgba(250,250,250,0.85)",
            bordercolor="#ebebeb",
            borderwidth=1,
            font=dict(size=11, color="#171717")
        )
    )
    fig.update_xaxes(
        gridcolor="#ebebeb",
        linecolor="#ebebeb",
        tickfont=dict(family="Geist Mono, JetBrains Mono, monospace", size=11, color="#888888"),
        title_font=dict(family="Geist, Inter, sans-serif", size=12, color="#4d4d4d")
    )
    fig.update_yaxes(
        gridcolor="#ebebeb",
        linecolor="#ebebeb",
        tickfont=dict(family="Geist Mono, JetBrains Mono, monospace", size=11, color="#888888"),
        title_font=dict(family="Geist, Inter, sans-serif", size=12, color="#4d4d4d")
    )
    return fig

# ==============================================================================
# Sidebar: App-Shell Controls & Provenance
# ==============================================================================
with st.sidebar:
    st.markdown("""
    <div style="padding: 8px 0 16px 0; border-bottom: 1px solid #ebebeb; margin-bottom: 16px;">
        <div class="v-caption-mono">CANDIDATE · TLPR200 / TPRO200</div>
        <div style="font-size: 18px; font-weight: 600; letter-spacing: -0.6px; color: #171717;">Y.Y. Zulu · 22339104</div>
        <div style="font-size: 13px; color: #888888; margin-top: 2px;">Supplementary Examination 2026</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="v-caption-mono">01 / OFFENCE CATEGORIES</div>', unsafe_allow_html=True)
    all_categories = sorted(panel_df["Crime Category"].unique().tolist())
    selected_categories = st.multiselect(
        "Crime categories",
        options=all_categories,
        default=all_categories,
        label_visibility="collapsed"
    )
    if not selected_categories:
        selected_categories = all_categories

    st.markdown('<div class="v-caption-mono" style="margin-top:12px;">02 / TEMPORAL WINDOW (21 QUARTERS)</div>', unsafe_allow_html=True)
    ordered_periods = (
        panel_df[["Time_Index", "Year_Quarter"]]
        .drop_duplicates()
        .sort_values("Time_Index")["Year_Quarter"]
        .tolist()
    )
    period_range = st.select_slider(
        "Quarter range",
        options=ordered_periods,
        value=(ordered_periods[0], ordered_periods[-1]),
        label_visibility="collapsed"
    )
    start_idx = ordered_periods.index(period_range[0])
    end_idx = ordered_periods.index(period_range[1])
    active_periods = ordered_periods[start_idx : end_idx + 1]

    st.markdown('<div class="v-caption-mono" style="margin-top:12px;">03 / SEASONAL QUARTER</div>', unsafe_allow_html=True)
    all_quarters = ["Q1", "Q2", "Q3", "Q4"]
    selected_quarters = st.multiselect(
        "Seasonal quarters",
        options=all_quarters,
        default=all_quarters,
        label_visibility="collapsed"
    )
    if not selected_quarters:
        selected_quarters = all_quarters

    st.markdown('<div class="v-caption-mono" style="margin-top:12px;">04 / K-MEANS RISK CLUSTER TIER</div>', unsafe_allow_html=True)
    cluster_options = sorted(station_df["Risk_Cluster_Short"].unique().tolist())
    selected_clusters = st.multiselect(
        "Risk clusters",
        options=cluster_options,
        default=cluster_options,
        label_visibility="collapsed"
    )
    if not selected_clusters:
        selected_clusters = cluster_options

    st.markdown('<div class="v-caption-mono" style="margin-top:12px;">05 / POLICE PRECINCT FILTER</div>', unsafe_allow_html=True)
    eligible_stations = sorted(
        station_df[station_df["Risk_Cluster_Short"].isin(selected_clusters)]["Station Name"].unique().tolist()
    )
    selected_stations = st.multiselect(
        "Police precincts (empty = all)",
        options=eligible_stations,
        default=[],
        placeholder="All 39 Ekurhuleni precincts...",
        label_visibility="collapsed"
    )
    active_stations = selected_stations if selected_stations else eligible_stations

    st.markdown("""
    <div style="margin-top: 24px; padding-top: 16px; border-top: 1px solid #ebebeb;">
        <div class="v-caption-mono">VERIFIED OPEN DATA PROVENANCE</div>
        <div style="font-size: 13px; line-height: 20px; margin-top: 6px;">
            <a href="https://www.saps.gov.za/services/crimestats.php" target="_blank" style="color: #0070f3; text-decoration: underline;">saps.gov.za/services/crimestats.php</a><br>
            <a href="https://www.saps.gov.za/services/boundary.php" target="_blank" style="color: #0070f3; text-decoration: underline;">saps.gov.za/services/boundary.php</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Filter panel dataframe
filtered_df = panel_df[
    (panel_df["Crime Category"].isin(selected_categories)) &
    (panel_df["Year_Quarter"].isin(active_periods)) &
    (panel_df["Quarter"].isin(selected_quarters)) &
    (panel_df["Station Name"].isin(active_stations))
].copy()

# ==============================================================================
# Hero Band (`hero-band` with Mesh Gradient Backdrop)
# ==============================================================================
st.markdown("""
<div class="v-hero-band">
    <div class="v-hero-mesh"></div>
    <div class="v-hero-content">
        <div class="v-banner-pill">
            <span class="v-banner-dot"></span>
            <span>EKURHULENI METROPOLITAN SAFETY ANALYTICS · 39 PRECINCTS · 2021 Q1 – 2026 Q1</span>
        </div>
        <h1 class="v-display-xl">Women-safety hotspots and spatial intelligence for Ekurhuleni.</h1>
        <p class="v-body-lg">
            Transforming 21 consecutive quarters of official South African Police Service records and UTM Zone 35S precinct geometry into leakage-free hotspot predictions, unsupervised risk clusters, and targeted prevention planning.
        </p>
        <div class="v-cta-row">
            <a class="v-btn-primary" href="https://www.saps.gov.za/services/crimestats.php" target="_blank">Verify SAPS Crime Statistics ↗</a>
            <a class="v-btn-secondary" href="https://www.saps.gov.za/services/boundary.php" target="_blank">Inspect GIS Precinct Boundaries ↗</a>
            <span class="v-badge">EPSG:32735 METRIC CRS</span>
            <span class="v-badge v-badge-blue">ROC-AUC 0.9762</span>
            <span class="v-badge v-badge-violet">4,914 PANEL OBSERVATIONS</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ==============================================================================
# Top KPI Summary Strip (with Featured Polarity-Flipped Card)
# ==============================================================================
total_incidents = int(filtered_df["Count"].sum())
mean_density = float(filtered_df["Spatial_Density"].mean()) if len(filtered_df) else 0.0
hotspot_count = int(filtered_df["Hotspot"].sum())
hotspot_rate = float(filtered_df["Hotspot"].mean() * 100) if len(filtered_df) else 0.0
anomaly_count = int(filtered_df["Is_Temporal_Anomaly"].sum())

if len(filtered_df) > 0:
    top_station_row = (
        filtered_df.groupby("Station Name")["Spatial_Density"]
        .mean()
        .sort_values(ascending=False)
    )
    top_station_name = top_station_row.index[0]
    top_station_val = top_station_row.iloc[0]
else:
    top_station_name = "N/A"
    top_station_val = 0.0

k1, k2, k3, k4, k5 = st.columns(5)
with k1:
    st.markdown(f"""
    <div class="v-card">
        <div class="v-caption-mono">RECORDED INCIDENTS</div>
        <div class="v-kpi-value">{total_incidents:,}</div>
        <span class="v-badge">{len(active_stations)} PRECINCTS · {len(active_periods)} QTRS</span>
    </div>
    """, unsafe_allow_html=True)
with k2:
    st.markdown(f"""
    <div class="v-card">
        <div class="v-caption-mono">SPATIAL DENSITY</div>
        <div class="v-kpi-value">{mean_density:.2f}<span style="font-size:15px;font-weight:400;color:#888888;"> /km²</span></div>
        <span class="v-badge v-badge-blue">AREA-NORMALISED RATE</span>
    </div>
    """, unsafe_allow_html=True)
with k3:
    # Featured Polarity-Flipped Ink Card
    st.markdown(f"""
    <div class="v-card-featured">
        <div class="v-caption-mono" style="color:#a1a1a1;">ACTIVE HOTSPOTS (≥ P80)</div>
        <div class="v-kpi-value" style="color:#ffffff;">{hotspot_count:,} <span style="font-size:15px;font-weight:400;color:#a1a1a1;">({hotspot_rate:.1f}%)</span></div>
        <span class="v-badge v-badge-dark">TOP 20% COHORT THRESHOLD</span>
    </div>
    """, unsafe_allow_html=True)
with k4:
    st.markdown(f"""
    <div class="v-card">
        <div class="v-caption-mono">PEAK DENSITY PRECINCT</div>
        <div class="v-kpi-value" style="font-size:22px;">{top_station_name}</div>
        <span class="v-badge v-badge-red">{top_station_val:.2f} CRIMES / KM²</span>
    </div>
    """, unsafe_allow_html=True)
with k5:
    st.markdown(f"""
    <div class="v-card">
        <div class="v-caption-mono">TEMPORAL ANOMALIES</div>
        <div class="v-kpi-value">{anomaly_count:,}</div>
        <span class="v-badge v-badge-amber">Z-SCORE ≥ +1.5 SD</span>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# 5-Up Tab Pill Row (`tab-ghost`)
# ==============================================================================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "01 · Spatial Map & EDA",
    "02 · Hotspot Classification",
    "03 · Pattern Discovery",
    "04 · Three-Hotspot Comparison",
    "05 · Governance & Complexity"
])

# ------------------------------------------------------------------------------
# TAB 1: Spatial Map & EDA Explorer
# ------------------------------------------------------------------------------
with tab1:
    st.markdown("""
    <div style="margin: 12px 0 20px 0;">
        <div class="v-caption-mono">SECTION 01 · SPATIAL CONCENTRATION & EXPLORATORY ANALYTICS</div>
        <h2 class="v-display-lg">Geographic exposure and seasonal crime trajectories.</h2>
        <p style="font-size:16px; color:#4d4d4d; max-width:880px; margin:0;">
            Precinct land areas across Ekurhuleni span from <code>8.95 km²</code> (Primrose) and <code>14.32 km²</code> (Tembisa) to <code>393.01 km²</code> (Devon). Evaluating spatial crime density per square kilometre exposes concentrated urban risk that raw incident counts conceal.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col_map, col_rank = st.columns([1.22, 1.0])

    with col_map:
        map_metric_choice = st.selectbox(
            "Spatial layer metric",
            options=[
                "Spatial_Density (Mean Crimes / km²)",
                "Count (Total Recorded Incidents)",
                "Hotspot_Frequency (% Quarters in Top 20% Hotspot)",
                "Predicted_Hotspot_Prob (Mean ML Hotspot Probability)"
            ],
            index=0
        )

        map_agg = (
            filtered_df.groupby("Station Name")
            .agg(
                Mean_Density=("Spatial_Density", "mean"),
                Total_Count=("Count", "sum"),
                Hotspot_Freq=("Hotspot", lambda s: s.mean() * 100.0),
                Mean_Prob=("Predicted_Hotspot_Prob", "mean"),
                Area_Sq_Km=("Area_Sq_Km", "first"),
                Risk_Cluster=("Risk_Cluster_Short", "first")
            )
            .reset_index()
        )

        metric_col_map = {
            "Spatial_Density (Mean Crimes / km²)": ("Mean_Density", "Crimes / km²"),
            "Count (Total Recorded Incidents)": ("Total_Count", "Total Incidents"),
            "Hotspot_Frequency (% Quarters in Top 20% Hotspot)": ("Hotspot_Freq", "Hotspot %"),
            "Predicted_Hotspot_Prob (Mean ML Hotspot Probability)": ("Mean_Prob", "ML Probability")
        }
        plot_col, plot_label = metric_col_map[map_metric_choice]

        custom_scale = [[0.0, "#fafafa"], [0.25, "#d3e5ff"], [0.55, "#7928ca"], [0.8, "#ff0080"], [1.0, "#ee0000"]]

        if hasattr(px, "choropleth_map"):
            fig_map = px.choropleth_map(
                map_agg,
                geojson=geojson_data,
                locations="Station Name",
                featureidkey="properties.Station Name",
                color=plot_col,
                color_continuous_scale=custom_scale,
                map_style="carto-positron",
                zoom=9.1,
                center={"lat": -26.21, "lon": 28.30},
                opacity=0.82,
                hover_name="Station Name",
                hover_data={
                    "Risk_Cluster": True,
                    "Area_Sq_Km": ":.2f",
                    "Total_Count": ":,",
                    "Mean_Density": ":.2f",
                    "Hotspot_Freq": ":.1f",
                    "Mean_Prob": ":.3f"
                },
                labels={plot_col: plot_label}
            )
        else:
            fig_map = px.choropleth_mapbox(
                map_agg,
                geojson=geojson_data,
                locations="Station Name",
                featureidkey="properties.Station Name",
                color=plot_col,
                color_continuous_scale=custom_scale,
                mapbox_style="carto-positron",
                zoom=9.1,
                center={"lat": -26.21, "lon": 28.30},
                opacity=0.82,
                hover_name="Station Name",
                hover_data={
                    "Risk_Cluster": True,
                    "Area_Sq_Km": ":.2f",
                    "Total_Count": ":,",
                    "Mean_Density": ":.2f",
                    "Hotspot_Freq": ":.1f",
                    "Mean_Prob": ":.3f"
                },
                labels={plot_col: plot_label}
            )
        style_vercel_fig(fig_map, f"Ekurhuleni precinct choropleth — {plot_label}", height=475)
        st.plotly_chart(fig_map, width="stretch")

    with col_rank:
        top_n = st.slider("Top precincts displayed", min_value=5, max_value=39, value=15)
        rank_df = map_agg.sort_values(plot_col, ascending=False).head(top_n).sort_values(plot_col, ascending=True)
        fig_bar = px.bar(
            rank_df,
            x=plot_col,
            y="Station Name",
            color="Risk_Cluster",
            orientation="h",
            text=rank_df[plot_col].apply(lambda x: f"{x:,.2f}"),
            color_discrete_map=CLUSTER_COLOR_MAP
        )
        style_vercel_fig(fig_bar, f"Top {top_n} precincts ranked by {plot_label}", height=475)
        fig_bar.update_layout(xaxis_title=plot_label, yaxis_title="")
        st.plotly_chart(fig_bar, width="stretch")

    col_t1, col_t2 = st.columns(2)
    with col_t1:
        trend_cat_df = (
            filtered_df.groupby(["Time_Index", "Year_Quarter", "Crime Category"])["Count"]
            .sum()
            .reset_index()
            .sort_values("Time_Index")
        )
        fig_trend = px.line(
            trend_cat_df,
            x="Year_Quarter",
            y="Count",
            color="Crime Category",
            markers=True,
            color_discrete_sequence=VERCEL_PALETTE
        )
        style_vercel_fig(fig_trend, "21-quarter trajectory by offence category", height=410)
        fig_trend.update_layout(xaxis_title="Financial Year & Quarter", yaxis_title="Recorded Incidents", xaxis_tickangle=-45)
        st.plotly_chart(fig_trend, width="stretch")

    with col_t2:
        fig_scatter = px.scatter(
            map_agg,
            x="Total_Count",
            y="Mean_Density",
            size="Area_Sq_Km",
            color="Risk_Cluster",
            hover_name="Station Name",
            text="Station Name",
            color_discrete_map=CLUSTER_COLOR_MAP
        )
        fig_scatter.update_traces(textposition="top center")
        style_vercel_fig(fig_scatter, "Raw incident count vs. spatial density (bubble = area km²)", height=410)
        fig_scatter.update_layout(
            xaxis_title="Total Recorded Incidents (Raw Count)",
            yaxis_title="Mean Spatial Density (Crimes / km²)"
        )
        st.plotly_chart(fig_scatter, width="stretch")

# ------------------------------------------------------------------------------
# TAB 2: Hotspot Classification & Metrics
# ------------------------------------------------------------------------------
with tab2:
    st.markdown("""
    <div style="margin: 12px 0 20px 0;">
        <div class="v-caption-mono">SECTION 02 · SUPERVISED MACHINE LEARNING & VALIDATION</div>
        <h2 class="v-display-lg">Leakage-free hotspot classification on unseen quarters.</h2>
        <p style="font-size:16px; color:#4d4d4d; max-width:920px; margin:0;">
            A precinct-quarter-category unit is designated a <b>Hotspot (1)</b> when its spatial density reaches the <b>top 20% (≥ 80th percentile)</b> within its <code>(Year, Quarter, Crime Category)</code> cohort. Models are trained strictly on lagged historical features from <code>2021–2025</code> (3,510 rows) and tested on 5 unseen quarters from <code>2025 Q1 – 2026 Q1</code> (1,170 rows).
        </p>
    </div>
    """, unsafe_allow_html=True)

    selected_model_name = st.radio(
        "Select classification architecture",
        options=["HistGradientBoostingClassifier", "RandomForestClassifier", "LogisticRegression"],
        horizontal=True
    )
    m_obj = metrics_data["models"][selected_model_name]
    rep = m_obj["report"]

    mc1, mc2, mc3, mc4, mc5 = st.columns(5)
    with mc1:
        st.markdown(f"""
        <div class="v-card">
            <div class="v-caption-mono">TEST ACCURACY</div>
            <div class="v-kpi-value">{m_obj['accuracy']*100:.2f}%</div>
            <span class="v-badge">1,170 UNSEEN ROWS</span>
        </div>
        """, unsafe_allow_html=True)
    with mc2:
        st.markdown(f"""
        <div class="v-card-featured">
            <div class="v-caption-mono" style="color:#a1a1a1;">ROC-AUC SCORE</div>
            <div class="v-kpi-value" style="color:#ffffff;">{m_obj['roc_auc']:.4f}</div>
            <span class="v-badge v-badge-dark">DISCRIMINATIVE POWER</span>
        </div>
        """, unsafe_allow_html=True)
    with mc3:
        st.markdown(f"""
        <div class="v-card">
            <div class="v-caption-mono">PR-AUC SCORE</div>
            <div class="v-kpi-value">{m_obj['pr_auc']:.4f}</div>
            <span class="v-badge v-badge-blue">PRECISION-RECALL AREA</span>
        </div>
        """, unsafe_allow_html=True)
    with mc4:
        st.markdown(f"""
        <div class="v-card">
            <div class="v-caption-mono">HOTSPOT PRECISION</div>
            <div class="v-kpi-value">{rep['1']['precision']:.4f}</div>
            <span class="v-badge v-badge-violet">CLASS 1 POSITIVE PURITY</span>
        </div>
        """, unsafe_allow_html=True)
    with mc5:
        st.markdown(f"""
        <div class="v-card">
            <div class="v-caption-mono">HOTSPOT RECALL / F1</div>
            <div class="v-kpi-value">{rep['1']['recall']:.2f} <span style="font-size:16px;color:#888888;">/ {rep['1']['f1-score']:.2f}</span></div>
            <span class="v-badge v-badge-amber">SENSITIVITY & HARMONIC MEAN</span>
        </div>
        """, unsafe_allow_html=True)

    cm_col, roc_col, fi_col = st.columns([1.0, 1.15, 1.15])

    with cm_col:
        cm_arr = np.array(m_obj["confusion_matrix"])
        cm_labels = ["Non-Hotspot (0)", "Hotspot (1)"]
        fig_cm = px.imshow(
            cm_arr,
            x=cm_labels,
            y=cm_labels,
            text_auto=True,
            color_continuous_scale=[[0.0, "#fafafa"], [0.5, "#d3e5ff"], [1.0, "#0070f3"]],
            labels=dict(x="Predicted Designation", y="Actual Designation", color="Observations")
        )
        style_vercel_fig(fig_cm, f"Confusion matrix ({selected_model_name})", height=400)
        fig_cm.update_layout(coloraxis_showscale=False)
        st.plotly_chart(fig_cm, width="stretch")

    with roc_col:
        fig_roc = go.Figure()
        for m_name, color in [
            ("HistGradientBoostingClassifier", "#171717"),
            ("RandomForestClassifier", "#0070f3"),
            ("LogisticRegression", "#ff0080")
        ]:
            mo = metrics_data["models"][m_name]
            fig_roc.add_trace(go.Scatter(
                x=mo["fpr"], y=mo["tpr"], mode="lines",
                name=f"{m_name} ({mo['roc_auc']:.4f})",
                line=dict(color=color, width=3.0 if m_name == selected_model_name else 1.6)
            ))
        fig_roc.add_trace(go.Scatter(
            x=[0, 1], y=[0, 1], mode="lines", name="Random Baseline (0.5000)",
            line=dict(color="#a1a1a1", dash="dash")
        ))
        style_vercel_fig(fig_roc, "ROC curve comparison across unseen quarters", height=400)
        fig_roc.update_layout(
            xaxis_title="False Positive Rate (1 - Specificity)",
            yaxis_title="True Positive Rate (Recall)",
            legend=dict(yanchor="bottom", y=0.04, xanchor="right", x=0.96)
        )
        st.plotly_chart(fig_roc, width="stretch")

    with fi_col:
        fi_df = pd.DataFrame(metrics_data["feature_importance"]).sort_values("Importance_Mean", ascending=True)
        fig_fi = px.bar(
            fi_df,
            x="Importance_Mean",
            y="Feature",
            error_x="Importance_Std",
            orientation="h",
            color_discrete_sequence=["#171717"]
        )
        style_vercel_fig(fig_fi, "Permutation feature importance (ROC-AUC drop)", height=400)
        fig_fi.update_layout(xaxis_title="Mean ROC-AUC Decrease on Unseen Test Set", yaxis_title="")
        st.plotly_chart(fig_fi, width="stretch")

    st.markdown('<div class="v-caption-mono" style="margin-top:8px;">CLASSIFICATION REPORT TABLE · UNSEEN TEST COHORT (2025 Q1 – 2026 Q1)</div>', unsafe_allow_html=True)
    rep_table = pd.DataFrame({
        "Class / Metric": ["Non-Hotspot (0)", "Hotspot (1)", "Macro Average", "Weighted Average"],
        "Precision": [rep["0"]["precision"], rep["1"]["precision"], rep["macro avg"]["precision"], rep["weighted avg"]["precision"]],
        "Recall": [rep["0"]["recall"], rep["1"]["recall"], rep["macro avg"]["recall"], rep["weighted avg"]["recall"]],
        "F1-Score": [rep["0"]["f1-score"], rep["1"]["f1-score"], rep["macro avg"]["f1-score"], rep["weighted avg"]["f1-score"]],
        "Support (Rows)": [int(rep["0"]["support"]), int(rep["1"]["support"]), int(rep["macro avg"]["support"]), int(rep["weighted avg"]["support"])]
    })
    st.dataframe(rep_table.style.format({"Precision": "{:.4f}", "Recall": "{:.4f}", "F1-Score": "{:.4f}"}), width="stretch")

# ------------------------------------------------------------------------------
# TAB 3: Pattern Discovery & Anomalies
# ------------------------------------------------------------------------------
with tab3:
    st.markdown("""
    <div style="margin: 12px 0 20px 0;">
        <div class="v-caption-mono">SECTION 03 · UNSUPERVISED CLUSTERING, CO-OCCURRENCE & ANOMALIES</div>
        <h2 class="v-display-lg">Structural risk tiers and quarterly anomaly surges.</h2>
        <p style="font-size:16px; color:#4d4d4d; max-width:900px; margin:0;">
            K-Means clustering ($k=3$) partitions the 39 Ekurhuleni precincts into distinct operational tiers based on standardised category densities and surface area, while Z-score anomaly detection isolates quarterly spikes exceeding $\\mu + 1.5\\sigma$.
        </p>
    </div>
    """, unsafe_allow_html=True)

    p_col1, p_col2 = st.columns([1.15, 1.0])

    with p_col1:
        fig_clust = px.scatter(
            station_df,
            x="Sexual Offences",
            y="Assault GBH",
            size="Women_Safety_Priority_Density",
            color="Risk_Cluster_Short",
            hover_name="Station Name",
            text="Station Name",
            hover_data=["Area_Sq_Km", "Common Assault", "Aggravated Robbery", "Kidnapping"],
            color_discrete_map=CLUSTER_COLOR_MAP
        )
        fig_clust.update_traces(textposition="top center")
        style_vercel_fig(fig_clust, "K-Means precinct clusters: Sexual Offences/km² vs. Assault GBH/km²", height=440)
        fig_clust.update_layout(
            xaxis_title="Mean Sexual Offences Density (Crimes / km²)",
            yaxis_title="Mean Assault GBH Density (Crimes / km²)"
        )
        st.plotly_chart(fig_clust, width="stretch")

    with p_col2:
        pivot_corr = (
            filtered_df.pivot_table(
                index=["Station Name", "Year_Quarter"],
                columns="Crime Category",
                values="Spatial_Density"
            )
            .corr()
            .round(2)
        )
        fig_corr = px.imshow(
            pivot_corr,
            text_auto=True,
            color_continuous_scale=[[0.0, "#fafafa"], [0.45, "#d3e5ff"], [0.75, "#7928ca"], [1.0, "#171717"]],
            zmin=0,
            zmax=1
        )
        style_vercel_fig(fig_corr, "Inter-category spatial-temporal correlation matrix", height=440)
        st.plotly_chart(fig_corr, width="stretch")

    st.markdown('<div class="v-caption-mono" style="margin-top:12px;">TEMPORAL ANOMALY LOG · SURGES EXCEEDING STATION BASELINE BY ≥ +1.5 SD</div>', unsafe_allow_html=True)
    anom_df = (
        filtered_df[filtered_df["Is_Temporal_Anomaly"] == 1][
            ["Station Name", "Risk_Cluster_Short", "Year_Quarter", "Crime Category", "Count", "Spatial_Density", "Density_Z_Score", "Predicted_Hotspot_Prob"]
        ]
        .sort_values("Density_Z_Score", ascending=False)
    )
    st.dataframe(
        anom_df.head(30).style.format({
            "Spatial_Density": "{:.3f}",
            "Density_Z_Score": "{:.2f}",
            "Predicted_Hotspot_Prob": "{:.3f}"
        }),
        width="stretch"
    )

# ------------------------------------------------------------------------------
# TAB 4: Three-Hotspot Deep-Dive Comparison (3-Up Pricing Rhythm with Middle Polarity Flip)
# ------------------------------------------------------------------------------
with tab4:
    st.markdown("""
    <div style="margin: 12px 0 20px 0;">
        <div class="v-caption-mono">SECTION 04 · THREE-PRECINCT DEEP-DIVE COMPARISON</div>
        <h2 class="v-display-lg">Comparing Kempton Park, Tembisa, and Germiston.</h2>
        <p style="font-size:16px; color:#4d4d4d; max-width:920px; margin:0;">
            Side-by-side structural comparison of Ekurhuleni's major aviation/commercial transit hub (<b>Kempton Park</b>), its most concentrated residential township precinct (<b>Tembisa</b>, polarity-flipped centre card), and its primary rail/industrial interchange (<b>Germiston</b>).
        </p>
    </div>
    """, unsafe_allow_html=True)

    all_station_list = sorted(station_df["Station Name"].unique().tolist())
    default_three = [s for s in ["KEMPTON PARK", "TEMBISA", "GERMISTON"] if s in all_station_list]
    compare_stations = st.multiselect(
        "Customise three precincts for comparison",
        options=all_station_list,
        default=default_three,
        max_selections=3
    )
    if not compare_stations:
        compare_stations = default_three

    comp_panel = panel_df[panel_df["Station Name"].isin(compare_stations)].copy()
    comp_station_meta = station_df[station_df["Station Name"].isin(compare_stations)].copy()

    # 3-Up Vercel Pricing-Card Rhythm (Middle Card Polarity-Flipped to Primary Ink #171717)
    card_cols = st.columns(len(compare_stations))
    for idx, st_name in enumerate(compare_stations):
        row_m = comp_station_meta[comp_station_meta["Station Name"] == st_name].iloc[0]
        st_sub = comp_panel[comp_panel["Station Name"] == st_name]
        so_mean = st_sub[st_sub["Crime Category"] == "Sexual Offences"]["Count"].mean()
        gbh_mean = st_sub[st_sub["Crime Category"] == "Assault GBH"]["Count"].mean()
        rob_mean = st_sub[st_sub["Crime Category"] == "Aggravated Robbery"]["Count"].mean()
        kid_mean = st_sub[st_sub["Crime Category"] == "Kidnapping"]["Count"].mean()

        is_featured = (idx == 1)  # Middle card gets `pricing-card-featured` polarity flip
        with card_cols[idx]:
            if is_featured:
                st.markdown(f"""
                <div class="v-tier-card-featured">
                    <div class="v-caption-mono" style="color:#50e3c2;">FEATURED FOCUS HOTSPOT · {row_m['Risk_Cluster_Short'].upper()}</div>
                    <div class="v-display-md" style="color:#ffffff;">{st_name}.</div>
                    <div style="font-size:36px; font-weight:600; letter-spacing:-1.8px; color:#ffffff; margin:10px 0 4px 0;">
                        {row_m['Women_Safety_Priority_Density']:.2f} <span style="font-size:14px; font-weight:400; color:#a1a1a1;">priority crimes/km²</span>
                    </div>
                    <div style="font-size:13px; color:#a1a1a1; margin-bottom:16px;">Precinct Footprint: {row_m['Area_Sq_Km']:.2f} km² · {int(row_m['Adjacent_Precincts'])} Adjacent Precincts</div>
                    <div class="v-tier-row-dark"><span>Sexual Offences / Qtr</span><span><b>{so_mean:.1f}</b> ({row_m['Sexual Offences']:.2f}/km²)</span></div>
                    <div class="v-tier-row-dark"><span>Assault GBH / Qtr</span><span><b>{gbh_mean:.1f}</b> ({row_m['Assault GBH']:.2f}/km²)</span></div>
                    <div class="v-tier-row-dark"><span>Aggravated Robbery / Qtr</span><span><b>{rob_mean:.1f}</b> ({row_m['Aggravated Robbery']:.2f}/km²)</span></div>
                    <div class="v-tier-row-dark" style="border-bottom:none;"><span>Kidnapping / Qtr</span><span><b>{kid_mean:.1f}</b> ({row_m['Kidnapping']:.2f}/km²)</span></div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="v-tier-card">
                    <div class="v-caption-mono">{row_m['Risk_Cluster_Short'].upper()}</div>
                    <div class="v-display-md">{st_name}.</div>
                    <div style="font-size:36px; font-weight:600; letter-spacing:-1.8px; color:#171717; margin:10px 0 4px 0;">
                        {row_m['Women_Safety_Priority_Density']:.2f} <span style="font-size:14px; font-weight:400; color:#888888;">priority crimes/km²</span>
                    </div>
                    <div style="font-size:13px; color:#888888; margin-bottom:16px;">Precinct Footprint: {row_m['Area_Sq_Km']:.2f} km² · {int(row_m['Adjacent_Precincts'])} Adjacent Precincts</div>
                    <div class="v-tier-row"><span>Sexual Offences / Qtr</span><span><b>{so_mean:.1f}</b> ({row_m['Sexual Offences']:.2f}/km²)</span></div>
                    <div class="v-tier-row"><span>Assault GBH / Qtr</span><span><b>{gbh_mean:.1f}</b> ({row_m['Assault GBH']:.2f}/km²)</span></div>
                    <div class="v-tier-row"><span>Aggravated Robbery / Qtr</span><span><b>{rob_mean:.1f}</b> ({row_m['Aggravated Robbery']:.2f}/km²)</span></div>
                    <div class="v-tier-row" style="border-bottom:none;"><span>Kidnapping / Qtr</span><span><b>{kid_mean:.1f}</b> ({row_m['Kidnapping']:.2f}/km²)</span></div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
    c_left, c_right = st.columns(2)

    with c_left:
        cat_comp = (
            comp_panel.groupby(["Station Name", "Crime Category"])["Spatial_Density"]
            .mean()
            .reset_index()
        )
        fig_comp_bar = px.bar(
            cat_comp,
            x="Crime Category",
            y="Spatial_Density",
            color="Station Name",
            barmode="group",
            color_discrete_sequence=["#0070f3", "#171717", "#ff0080", "#7928ca"]
        )
        style_vercel_fig(fig_comp_bar, "Mean spatial crime density by category across selected precincts", height=420)
        fig_comp_bar.update_layout(yaxis_title="Mean Quarterly Crimes / km²", xaxis_title="")
        st.plotly_chart(fig_comp_bar, width="stretch")

    with c_right:
        comp_focus_cat = st.selectbox(
            "Timeline offence category",
            options=["All Women-Safety Priority Offences (Combined)"] + all_categories,
            index=0
        )
        if comp_focus_cat == "All Women-Safety Priority Offences (Combined)":
            tl_sub = comp_panel[comp_panel["Crime Category"].isin(["Sexual Offences", "Assault GBH", "Common Assault", "Kidnapping"])]
        else:
            tl_sub = comp_panel[comp_panel["Crime Category"] == comp_focus_cat]

        tl_agg = (
            tl_sub.groupby(["Time_Index", "Year_Quarter", "Station Name"])["Spatial_Density"]
            .sum()
            .reset_index()
            .sort_values("Time_Index")
        )
        fig_comp_tl = px.line(
            tl_agg,
            x="Year_Quarter",
            y="Spatial_Density",
            color="Station Name",
            markers=True,
            color_discrete_sequence=["#0070f3", "#171717", "#ff0080", "#7928ca"]
        )
        style_vercel_fig(fig_comp_tl, f"21-quarter density trajectory — {comp_focus_cat}", height=420)
        fig_comp_tl.update_layout(xaxis_title="Financial Year & Quarter", yaxis_title="Crimes / km²", xaxis_tickangle=-45)
        st.plotly_chart(fig_comp_tl, width="stretch")

# ------------------------------------------------------------------------------
# TAB 5: Governance, Prevention & Complexity (`showcase-band-dark` + `code-editor-mockup`)
# ------------------------------------------------------------------------------
with tab5:
    st.markdown("""
    <div style="margin: 12px 0 20px 0;">
        <div class="v-caption-mono">SECTION 05 · PREVENTION ARCHITECTURE, ETHICS & ALGORITHMIC COMPLEXITY</div>
        <h2 class="v-display-lg">Evidence-led prevention planning and methodological governance.</h2>
    </div>
    """, unsafe_allow_html=True)

    g1, g2, g3 = st.columns(3)
    with g1:
        st.markdown("""
        <div class="v-card">
            <div class="v-caption-mono">01 / TRANSIT & CBD HUBS (KEMPTON PARK, GERMISTON)</div>
            <div class="v-display-md">Environmental CPTED.</div>
            <p style="font-size:14px; line-height:20px; color:#4d4d4d; letter-spacing:-0.28px;">
                High volumes of Aggravated Robbery (<code>139.0/qtr</code> in Kempton Park; <code>146.1/qtr</code> in Germiston), Common Assault, and Kidnapping cluster along multimodal transport corridors. Prevention requires clearing and securing derelict CBD buildings, high-mast pedestrian lighting between taxi ranks and PRASA/Gautrain rail nodes, and shift-aligned visible policing.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with g2:
        st.markdown("""
        <div class="v-card">
            <div class="v-caption-mono">02 / RESIDENTIAL HOTSPOTS (TEMBISA, IVORY PARK)</div>
            <div class="v-display-md">GBV trauma & patrol scale.</div>
            <p style="font-size:14px; line-height:20px; color:#4d4d4d; letter-spacing:-0.28px;">
                Compact residential precincts exhibit extreme per-km² concentration of Sexual Offences (<code>4.93/km²</code> in Tembisa) and Assault GBH (<code>14.70/km²</code>), peaking sharply every <b>Q3 (October–December)</b>. Interventions must pre-deploy mobile Victim Friendly Rooms (VFRs), weekend evening patrols, and liquor-outlet compliance before Q3 begins.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with g3:
        st.markdown("""
        <div class="v-card">
            <div class="v-caption-mono">03 / CAUSAL RIGOUR & ETHICS</div>
            <div class="v-display-md">Association ≠ causation.</div>
            <p style="font-size:14px; line-height:20px; color:#4d4d4d; letter-spacing:-0.28px;">
                Elevated crime density near transport nodes or high-density townships reflects an <b>empirical association</b> driven by ambient commuter footfall and environmental opportunity structures—not proof that a community is inherently dangerous. SAPS rows are never falsely relabeled as "crimes against women" where sex disaggregation is absent.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Polarity-Flipped Dark Showcase Band (`showcase-band-dark`) with `code-editor-mockup`
    st.markdown("""
    <div class="v-showcase-dark">
        <div class="v-caption-mono" style="color:#50e3c2;">ALGORITHMIC COMPLEXITY & PIPELINE SPECIFICATION</div>
        <h3 class="v-display-lg" style="color:#ffffff; margin-bottom:8px;">A reproducible compute pipeline for all 39 precincts.</h3>
        <p style="font-size:16px; color:#a1a1a1; max-width:820px; margin-bottom:16px;">
            Formal Big-O time and space bounds across multi-workbook ingestion, UTM Zone 35S polygon projection, leakage-free lag engineering, K-Means risk profiling, and histogram-binned gradient boosting.
        </p>
        <div class="v-code-mockup">
<span style="color:#888888;">// Let F=5 workbooks, R_raw≈35,000 rows/file, S=39 precincts (V vertices), T=21 quarters, C=6 categories (N=4,914 rows)</span><br>
<span style="color:#50e3c2;">01. Multi-Workbook SAPS Ingestion & Deduplication</span>   Time: O(F · R_raw + N log N)         Space: O(F · R_raw)<br>
<span style="color:#0070f3;">02. UTM Zone 35S (EPSG:32735) Projection & Adjacency</span> Time: O(S_nat · V + S² · V)          Space: O(S_nat · V)<br>
<span style="color:#f5a623;">03. Chronological Lag & Rolling Window Engineering</span>  Time: O(N log N)                     Space: O(N)<br>
<span style="color:#ff0080;">04. Unsupervised K-Means Risk Profiling (k=3, I iter)</span> Time: O(I · k · S · d_clust)         Space: O((S + k) · d_clust)<br>
<span style="color:#50e3c2;">05. HistGradientBoosting (M=150 trees, D=5, B=255)</span>  Time: O(N · d + M · 2^D · d · B)     Space: O(N · d + M · 2^D)
        </div>
    </div>
    """, unsafe_allow_html=True)
