## Data Overview
We obtained publicly available Google Weekly Search Trends and Daily Hospitalisation data between 01 Jan to 21 Sept 2020 aggregated by US State (Source: Google Research's Open COVID-19 Data project). The search trends dataset contains weekly anonymised data for 423 COVID-19 symptom search terms across 16 US states, recording the relative popularity of symptoms searched across all symptoms in each region from a scale of 0-100.

The data was cleaned with the following procedure. For daily hospitalisation data we (1) remove states where more than > 80% of dataset records no new daily hospitalisations, (2) remove data recording > 14 consecutive days of no new hospitalisations. From this we are left with 11 US States containing both hospitalisation and search trend data. We merged the datasets by sampling available daily hospitalisation data onto weekly search trend timestamps. From this merged weekly dataset, we retained XX search trend features with more than XX% of the total data points.

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
