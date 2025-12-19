import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="Sri Lanka Agricultural Insights",
    layout="wide"
)

sns.set_style("whitegrid")

# --------------------------------------------------
# Paths
# --------------------------------------------------
DATA_PATH = Path("data/processed/cleaned_agriculture_data.csv")
FIGURES_PATH = Path("reports/figures")

# --------------------------------------------------
# Load data
# --------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    return df

df = load_data()

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
st.sidebar.title("Dashboard Controls")

metric_map = {
    "Production": "production",
    "Export Volume": "volume",
    "Export Value (USD mn)": "value_usd_mn"
}

metric_label = st.sidebar.selectbox(
    "Metric",
    list(metric_map.keys())
)
metric = metric_map[metric_label]

years = df["year"].dropna().astype(int)
year_range = st.sidebar.slider(
    "Year Range",
    int(years.min()),
    int(years.max()),
    (int(years.min()), int(years.max()))
)

all_crops = sorted(df["crop"].dropna().unique())
selected_crops = st.sidebar.multiselect(
    "Crops",
    all_crops,
    default=all_crops[:6]
)

show_rolling = st.sidebar.checkbox("Show 3-year rolling average")

# Filter data for interactive plots
filtered = df[
    (df["metric"] == metric) &
    (df["year"].between(year_range[0], year_range[1])) &
    (df["crop"].isin(selected_crops))
]

# --------------------------------------------------
# Tabs for layout
# --------------------------------------------------
tab1, tab2, tab3 = st.tabs(["📈 Visualizations", "📊 Report Figures", "💡 Business Insights"])

# -------------------
# TAB 1: Visualizations
# -------------------
with tab1:
    st.header("Visualizations")
    st.markdown(f"**Metric:** {metric_label} &nbsp;&nbsp;|&nbsp;&nbsp; **Years:** {year_range[0]}–{year_range[1]}")

    # KPI row
    k1, k2, k3 = st.columns(3)
    total_value = filtered["value"].sum()
    avg_yearly = filtered.groupby("year")["value"].sum().mean()
    top_crop = (
        filtered.groupby("crop")["value"].sum()
        .sort_values(ascending=False)
        .index[0]
        if not filtered.empty else "N/A"
    )

    k1.metric("Total", f"{total_value:,.0f}")
    k2.metric("Average per Year", f"{avg_yearly:,.0f}")
    k3.metric("Top Crop", top_crop)

    # Trend over time
    st.subheader("Trend Over Time")
    trend = filtered.groupby("year", as_index=False)["value"].sum()
    fig, ax = plt.subplots()
    sns.lineplot(data=trend, x="year", y="value", marker="o", ax=ax, label="Raw")
    if show_rolling:
        trend["rolling_3yr"] = trend["value"].rolling(3, min_periods=1).mean()
        sns.lineplot(
            data=trend,
            x="year",
            y="rolling_3yr",
            marker="o",
            ax=ax,
            label="3-year rolling avg"
        )
    ax.set_xlabel("Year")
    ax.set_ylabel(metric_label)
    ax.legend()
    st.pyplot(fig)

    # Top crops comparison
    st.subheader("Top Crops Comparison")
    top_crops = (
        filtered.groupby("crop")["value"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )
    fig, ax = plt.subplots()
    sns.barplot(x=top_crops.values, y=top_crops.index, ax=ax)
    ax.set_xlabel(metric_label)
    ax.set_ylabel("Crop")
    st.pyplot(fig)

    # Distribution by crop
    st.subheader("Distribution by Crop")
    fig, ax = plt.subplots(figsize=(10, 4))
    sns.boxplot(data=filtered, x="crop", y="value", ax=ax)
    plt.xticks(rotation=45)
    ax.set_xlabel("Crop")
    ax.set_ylabel(metric_label)
    st.pyplot(fig)

    # Production vs export scatter
    st.subheader("Production vs Export Value")
    wide = df.pivot_table(index=["crop", "year"], columns="metric", values="value").reset_index()
    if "production" in wide.columns and "value_usd_mn" in wide.columns:
        scatter = wide.dropna()
        fig, ax = plt.subplots()
        sns.scatterplot(
            data=scatter,
            x="production",
            y="value_usd_mn",
            hue="crop",
            ax=ax
        )
        ax.set_xlabel("Production")
        ax.set_ylabel("Export Value (USD mn)")
        st.pyplot(fig)
    else:
        st.info("Production and export value not available together.")

# -------------------
# TAB 2: Report Figures
# -------------------
with tab2:
    st.header("Key Figures from Report")
    if FIGURES_PATH.exists():
        images = sorted(FIGURES_PATH.glob("*.png"))
        if images:
            cols = st.columns(2)
            for i, img in enumerate(images):
                with cols[i % 2]:
                    st.image(img, caption=img.stem.replace("_", " ").title())
        else:
            st.info("No figures found in reports/figures/")
    else:
        st.warning("reports/figures folder not found.")

# -------------------
# TAB 3: Business Insights
# -------------------
with tab3:
    st.header("Business Insights")
    st.markdown("""
**Reliable crops**: Paddy, Coffee, and Coconut are identified as reliable crops based on low volatility and strong recent production.  
**Risky crops**: Pepper, Clove, Nutmeg & Mace, Cinnamon, Cashew, Cocoa, and Rubber are flagged as high-volatility crops.  
**Observing growth patterns**: Positive YoY growth in some years (2007, 2010, 2012), sharp drop in 2011. Single-year spikes/dips require crop-level follow-up.  
**Recommended actions**:  
- Prioritize reliable crops for logistics, storage, and exports.  
- Design conditional subsidies or insurance for risky crops.  
- Route risky crops toward processing/value-added chains when export volatility is high.  
- Pilot interventions (irrigation, improved seeds, post-harvest) for risky crops with long-term potential.
""")
