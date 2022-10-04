import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

deaths_from_digest_disease = pd.read_excel(
    './fertilizers-&-pesticides-&-deaths-in-raw-tables.xlsx', sheet_name='annual-number-of-deaths-by-caus')

print(deaths_from_digest_disease)

deaths_top_10_average = deaths_from_digest_disease.groupby(
    by=['Year'])['Number of deaths from digestive diseases'].sum()
deaths_top_10_average_df = deaths_top_10_average.to_frame(
    name="Average Number of deaths from digestive diseases").reset_index()
print(deaths_top_10_average_df)
