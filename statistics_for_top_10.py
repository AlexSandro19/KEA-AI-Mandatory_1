import pandas as pd
import matplotlib.pyplot as plt

all_combined = pd.read_csv('./all_combined_clean.csv')

food_fertilizers_top_10 = all_combined.groupby(
    by=['Year'])['Total fertilizer use per area of cropland in kg per hectare'].nlargest(100)

food_fertilizers_top_10_df= food_fertilizers_top_10.to_frame(
    name="Total fertilizer use per area of cropland in kg per hectare").reset_index()


statistical_data_top_10_df = food_fertilizers_top_10_df.merge(
    all_combined, on=['Year', 'Total fertilizer use per area of cropland in kg per hectare'])

country_list = statistical_data_top_10_df['Entity']

statistical_data_top_10_df.to_csv('./statistical_top_10_data.csv', index=False)



food_supply_quantity_top_10_average = statistical_data_top_10_df.groupby(
    by=['Year'])['Total_food_supply_quantity, kg'].mean().round(2)
food_supply_quantity_top_10_average_df = food_supply_quantity_top_10_average.to_frame(
    name="Average food supply quantity, kg").reset_index()

food_supply_quality_top_10_average = statistical_data_top_10_df.groupby(
    by=['Year'])['Total_food_supply_quality, kcal/capita/day'].mean().round(2)
food_supply_quality_top_10_average_df = food_supply_quality_top_10_average.to_frame(
    name="Average food supply quality, kcal/capita/day").reset_index()
final_merged_table_top100_average = food_supply_quantity_top_10_average_df.merge(food_supply_quality_top_10_average_df, on=['Year'])

fertilizers_top_10_average = statistical_data_top_10_df.groupby(by=['Year'])[
    'Total fertilizer use per area of cropland in kg per hectare'].mean().round(2)
fertilizers_top_10_average_df = fertilizers_top_10_average.to_frame(
    name="Average fertilizer use per area of cropland in kg per hectare").reset_index()
final_merged_table_top100_average = final_merged_table_top100_average.merge(fertilizers_top_10_average_df,on=['Year'])
pesticides_top_10_average = statistical_data_top_10_df.groupby(
    by=['Year'])['Pesticides used per area of cropland in kg per hectare'].mean().round(2)
pesticides_top_10_average_df = pesticides_top_10_average.to_frame(
    name="Average Pesticides used per area of cropland in kg per hectare").reset_index()
final_merged_table_top100_average =final_merged_table_top100_average.merge(pesticides_top_10_average_df,on=['Year'])
deaths_top_10_average = statistical_data_top_10_df.groupby(
    by=['Year'])['Number of deaths from digestive diseases'].mean().round(2)
deaths_top_10_average_df = deaths_top_10_average.to_frame(
    name="Average Number of deaths from digestive diseases").reset_index()
final_merged_table_top100_average =final_merged_table_top100_average.merge(deaths_top_10_average_df,on=['Year'])
#deaths_top_10_sum = statistical_data_top_10_df.groupby(
#    by=['Year'])['Number of deaths from digestive diseases'].sum()
#deaths_top_10_sum_df = deaths_top_10_sum.to_frame(
#    name="Sum Number of deaths from digestive diseases").reset_index()

final_merged_table_top100_average.to_csv('./final_merged_table_top100_average.csv',index=False)


fig, axs = plt.subplots(5, 1, sharex=True)
fig.subplots_adjust(hspace=0)
axs[0].bar(food_supply_quantity_top_10_average_df['Year'], food_supply_quantity_top_10_average_df['Average food supply quantity, kg'],color='red', label="average quantity")
axs[1].bar(food_supply_quality_top_10_average_df['Year'], food_supply_quality_top_10_average_df['Average food supply quality, kcal/capita/day'],color='red', label="average quantity")
axs[2].bar(fertilizers_top_10_average_df['Year'], fertilizers_top_10_average_df['Average fertilizer use per area of cropland in kg per hectare'],color='red', label="fertilizers")
axs[3].bar(pesticides_top_10_average_df['Year'], pesticides_top_10_average_df['Average Pesticides used per area of cropland in kg per hectare'],color='red', label="pesticides")
axs[4].bar(deaths_top_10_average_df['Year'], deaths_top_10_average_df['Average Number of deaths from digestive diseases'],color='red', label="deaths")
axs[0].legend(loc="lower right")
axs[1].legend(loc="lower right")
axs[2].legend(loc="lower right")
axs[3].legend(loc="lower right")
axs[4].legend(loc="lower right")


plt.show()
