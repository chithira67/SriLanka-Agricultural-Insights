# Data Cleaning

This document explains the cleaning and transformation steps applied to the raw datasets.

## Cleaning Steps

1. **Normalize column names**
   - Remove spaces, special characters
   - Convert to lowercase
   - Replace currency symbols (e.g., $ → dollar)

2. **Drop duplicates**
   - Checked each dataset and removed duplicate rows

3. **Drop empty rows**
   - Rows with all values missing were removed

4. **Reshape datasets**
   - Melt wide format (year columns) into long format (`year` and `value` columns)
   - Add `metric` column to distinguish production, volume, and export value

5. **Combine datasets**
   - Production and export datasets merged into a single cleaned file: `cleaned_agriculture_data.csv`

## Output

- `production_long.csv` → long format production
- `export_long.csv` → long format export data
- `cleaned_agriculture_data.csv` → combined cleaned dataset
