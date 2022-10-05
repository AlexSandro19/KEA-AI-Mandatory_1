import pandas as pd
import matplotlib.pyplot as plt
import scipy
statistical_data_df = pd.read_csv('./all_combined.csv')
statistical_data_df_cleaned = statistical_data_df.dropna()
print()
results1 = scipy.stats.pearsonr(statistical_data_df_cleaned['Total fertilizer use per area of cropland in kg per hectare'],statistical_data_df_cleaned['Number of deaths from digestive diseases'])
print("Fertilizers and death", results1)
results2 = scipy.stats.pearsonr(statistical_data_df_cleaned['Pesticides used per area of cropland in kg per hectare'],statistical_data_df_cleaned['Number of deaths from digestive diseases'])
print("Pesticides and death", results2)
results3 = scipy.stats.pearsonr(statistical_data_df_cleaned['Total fertilizer use per area of cropland in kg per hectare'],statistical_data_df_cleaned['Total_food_supply_quantity, kg'])
print("Fertilizers and quantity", results3)
results4 = scipy.stats.pearsonr(statistical_data_df_cleaned['Total fertilizer use per area of cropland in kg per hectare'],statistical_data_df_cleaned['Total_food_supply_quality, kcal/capita/day'])
print("Fertilizers and quality", results4)

correlation_df = statistical_data_df_cleaned['Total fertilizer use per area of cropland in kg per hectare'].corr(statistical_data_df_cleaned['Number of deaths from digestive diseases']);
print("Correlation: ", correlation_df)
