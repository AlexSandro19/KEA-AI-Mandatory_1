import pandas as pd
import matplotlib.pyplot as plt

all_combined = pd.read_csv('./all_combined.csv',delimiter=';')
print(type(all_combined))
food_fertilizers_top_10 = all_combined.groupby(
    by=['Year'])['Total fertilizer use per area of cropland in kg per hectare'].nlargest(100)

#food_fertilizers_top_10_df= food_fertilizers_top_10.to_frame(
#    name="Total fertilizer use per area of cropland in kg per hectare").reset_index()


#statistical_data_top_10_df = all_combined.merge(
#    food_fertilizers_top_10_df, on=['Year', 'Total fertilizer use per area of cropland in kg per hectare'])
#print(statistical_data_top_10_df)
#statistical_data_top_10_df.to_csv('./top_fertilizers.csv', index=False)
#statistical_data_top_10_df.to_excel('./top_fertilizers.xlsx', index=False)
