We extract Google Search Trends data for 423 COVID-19 symptom related terms, and daily hospitalisation data between 01 Jan 2020 to XXXXXX aggregated by US State. The search trends dataset contains aggregated data for only 16 US States. Daily hospitalisation data was cleaned with the following criteria: (1) remove states where more than > 80% of dataset records no new daily hospitalisations, (2) remove data recording > 14 consecutive days of no new hospitalisations. From this, only 11 US States contain valid hospitalisation and search trend data.

We then merged the daily hospitalisation and weekly search trend datasets to produce a merged weekly dataset, retaining XX search trend features with more than XX% of the data for 11 US States available.

Contains
1. Raw Data under folder /Data/
2. 1_DataProcessing.ipynb where data cleaning was done    
3. Cleaned Data under folder /Clean/
  - USA_coviddata_clean.csv
  - USA_coviddata_clean_25.csv : retaining search trend features with > 25% of data available
  - USA_coviddata_clean_30.csv : retaining search trend features with > 30% of data available
  - USA_coviddata_clean_50.csv : retaining search trend features with > 50% of data available
