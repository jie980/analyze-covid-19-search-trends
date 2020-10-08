## Data Overview
We extract Google Search Trends data for 423 COVID-19 symptom related terms, and daily hospitalisation data between 01 Jan to 21 Sept 2020 aggregated by US State. The search trends dataset contains aggregated data for only 16 US States. Daily hospitalisation data was cleaned with the following criteria: (1) remove states where more than > 80% of dataset records no new daily hospitalisations, (2) remove data recording > 14 consecutive days of no new hospitalisations. From this, only 11 US States contain both valid hospitalisation and search trend data.

For these 11 states, we merged the daily hospitalisation and weekly search trend datasets to produce a weekly dataset, retaining XX search trend features with more than XX% of the total data points.

### Additional Notes:
- I chose not to remove search trend data in the dates where there is no corresponding hospitalisation data

## Folder Contents
Contains
1. Raw Data under folder /Data/
2. 1_DataProcessing.ipynb where data cleaning was done    
3. Cleaned Data under folder /Clean/
  - USA_coviddata_clean.csv
  - USA_coviddata_clean_25.csv : retaining search trend features with > 25% of data available
  - USA_coviddata_clean_30.csv : retaining search trend features with > 30% of data available
  - USA_coviddata_clean_50.csv : retaining search trend features with > 50% of data available
