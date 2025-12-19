# Sri Lanka Agricultural Insights

This repository provides an **exploratory data analysis (EDA) and business insights** on agricultural production and export data in Sri Lanka. The project includes data cleaning, visualization, trend analysis, and a **Streamlit dashboard** for interactive exploration.

---


---

## **Project Overview**

The main goals of this project are to:

1. **Explore agricultural production and export data**  
   - Inspect raw datasets for missing values, duplicates, and inconsistent column names  
   - Reshape wide tables (years as columns) to long format (year, value rows)  

2. **Perform data cleaning**  
   - Standardize column names  
   - Remove duplicates and empty rows  
   - Combine production and export datasets into a single clean CSV  

3. **Conduct exploratory data analysis (EDA)**  
   - Overall trends in total agricultural production  
   - Crop-wise comparison and variability  
   - Outlier detection and distribution analysis  
   - Correlations between production, export volume, and export value  

4. **Generate business insights**  
   - Identify **reliable crops** (low volatility, high production)  
   - Identify **risky crops** (high volatility)  
   - Recommend actions for planning, subsidies, and export strategies  

5. **Provide an interactive dashboard using Streamlit**  
   - Filter by metric, year range, and crop  
   - Display trend lines, top crop comparisons, distributions, scatter plots  
   - Visualize all static report figures  
   - Access business insights directly in the app  
   - (Optional) Download a PDF report including insights and figures  

---

## **Project Summary & Screenshots**

The dashboard contains three main sections:

1. **Interactive Charts** – dynamic plots with sidebar filters for metrics, year range, and crops.  
2. **Report Figures** – static plots generated from EDA, automatically loaded from `reports/figures/`.  
3. **Business Insights** – key recommendations for policy, exports, and crop planning.  

**Example Screenshots:**

Interactive Charts Tab:  
![Interactive Charts](assets/interactive_charts.png)

Report Figures Tab:  
![Report Figures](assets/report_figures.png)

Business Insights Tab:  
![Business Insights](assets/business_insights.png)

> Replace the `assets/` images with your actual screenshots.

---

## **Getting Started**

### 1. Clone the repository

```bash
git clone https://github.com/chithira67/SriLanka-Agricultural-Insights.git
cd SriLanka-Agricultural-Insights

###  2.Create a virtual environment 
python -m venv venv
source venv/bin/activate 
venv\Scripts\activate     

3. Install dependencies
pip install -r requirements.txt


Dependencies include: pandas, numpy, matplotlib, seaborn, streamlit, markdown2, pdfkit

4. Run the Streamlit dashboard
streamlit run app/app.py

Using the Dashboard

Sidebar Controls:

Select metric (Production, Export Volume, Export Value USD mn)

Choose year range

Filter by crops

Toggle 3-year rolling average for trends

Tabs:

Interactive Charts – view dynamic trends and distributions

Report Figures – see static PNG plots from your analysis

Business Insights – key takeaways and recommendations

PDF Report Download (optional)

Generates a PDF with business insights and figures (requires wkhtmltopdf + pdfkit)

Data Sources

production_of_major_agricultural_crops.csv – national crop production data

volume_and_value_of_export_agriculture_crops.csv – export volumes and values

All data is from official Sri Lankan agricultural statistics sources.

Notebooks

01_data_overview.ipynb – Initial inspection of raw CSVs, missing values, duplicates

02_data_cleaning.ipynb – Standardizing columns, removing duplicates, reshaping datasets

03_exploratory_data_analysis.ipynb – Visual exploration of trends, distributions, and correlations

04_business_insights.ipynb – Translating EDA results into actionable recommendations

## Contributing

Contributions are welcome! You can:

Add more crops or years of data

Enhance visualizations or dashboard interactivity

Integrate additional analysis like climate impact or price trends

License

This project is released under the MIT License.

