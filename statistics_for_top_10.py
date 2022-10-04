import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

all_combined = pd.read_csv('./all_combined.csv')

food_supply_quantity_top_10 = all_combined.groupby(
    by=['Year'])['Total_food_supply_quantity, kg'].nlargest(10)
food_supply_quantity_top_10_df = food_supply_quantity_top_10.to_frame(
    name="Total_food_supply_quantity, kg").reset_index()
# print(food_supply_quantity_top_10_df.head(50))
statistical_data_top_10_df = food_supply_quantity_top_10_df.merge(
    all_combined, on=['Year', 'Total_food_supply_quantity, kg'])
# print(statistical_data_top_10_df.head(50))

# statistical_data_top_10_df.to_csv('./statistical_top_10_data.csv', index=False)

years = list(range(1990, 2020))
statistical_data_top_10_average_df = pd.DataFrame(data=years, columns=['Year'])

food_supply_quantity_top_10_average = statistical_data_top_10_df.groupby(
    by=['Year'])['Total_food_supply_quantity, kg'].mean().round(2)
food_supply_quantity_top_10_average_df = food_supply_quantity_top_10_average.to_frame(
    name="Average food supply quantity, kg").reset_index()
# print(food_supply_quantity_top_10_average_df)
food_supply_quality_top_10_average = statistical_data_top_10_df.groupby(
    by=['Year'])['Total_food_supply_quality, kcal/capita/day'].mean().round(2)
food_supply_quality_top_10_average_df = food_supply_quality_top_10_average.to_frame(
    name="Average food supply quality, kcal/capita/day").reset_index()
# print(food_supply_quality_top_10_average_df)
fertilizers_top_10_average = statistical_data_top_10_df.groupby(by=['Year'])[
    'Total fertilizer use per area of cropland in kg per hectare'].mean().round(2)
fertilizers_top_10_average_df = fertilizers_top_10_average.to_frame(
    name="Average fertilizer use per area of cropland in kg per hectare").reset_index()
# print(fertilizers_top_10_average_df)
pesticides_top_10_average = statistical_data_top_10_df.groupby(
    by=['Year'])['Pesticides used per area of cropland in kg per hectare'].mean().round(2)
pesticides_top_10_average_df = pesticides_top_10_average.to_frame(
    name="Average Pesticides used per area of cropland in kg per hectare").reset_index()
# print(pesticides_top_10_average_df)
deaths_top_10_average = statistical_data_top_10_df.groupby(
    by=['Year'])['Number of deaths from digestive diseases'].mean().round(2)
deaths_top_10_average_df = deaths_top_10_average.to_frame(
    name="Average Number of deaths from digestive diseases").reset_index()
# print(deaths_top_10_average_df)
deaths_top_10_sum = statistical_data_top_10_df.groupby(
    by=['Year'])['Number of deaths from digestive diseases'].sum()
deaths_top_10_sum_df = deaths_top_10_sum.to_frame(
    name="Sum Number of deaths from digestive diseases").reset_index()
# print(deaths_top_10_sum_df)


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

# Shows the total and average number of deaths for top 10 countries
# plt.bar(deaths_top_10_average_df['Year']-0.1,
#         deaths_top_10_average_df['Average Number of deaths from digestive diseases'], color='red', width=0.25, label="deaths average")
# plt.bar(deaths_top_10_sum_df['Year']+0.1,
#         deaths_top_10_sum_df['Sum Number of deaths from digestive diseases'], color='blue', width=0.25, label="deaths sum")
# plt.legend(loc="lower right")
# plt.show()






# statistical_data_top_10_df = statistical_data_top_10_df.merge(food_supply_quantity_top_10_average_df, on='Year')
# food_supply_quantity_top_10_average = statistical_data_top_10_df.groupby(by=['Year'])['Total_food_supply_quantity, kg'].nlargest(10).groupby(by=['Year']).mean().round(2)
# food_supply_quantity_top_10_average_df = food_supply_quantity_top_10_average.to_frame(name="Average food supply quantity, kg").reset_index()
# food_supply_quantity_head = all_combined.groupby(by=['Year'])['Total_food_supply_quantity, kg'].nlargest(10).head(50)
# food_supply_quantity_df = food_supply_quantity.to_frame(name="Average fertilizer use per area of cropland in kg per hectare").reset_index()
# print(food_supply_quantity_head)

# years = list(range(1990, 2020))
# statistical_data_top_10_df = pd.DataFrame(data=years, columns=['Year'])
# statistical_data_top_10_df = statistical_data_top_10_df.merge(food_supply_quantity_df, on='Year')

# statistical_data_top_10_df.to_csv('./statistical_top_10_data.csv', index=False)
# print(food_supply_quantity_df)
# merged_table= statistical_data_top_10_df.merge(all_combined, on='Year')
# merged_table.to_csv('./merged_table.csv', index=False)
# fig, axs = plt.subplots(5, 1, sharex=True)
# fig.subplots_adjust(hspace=0)
# axs[0].bar(statistical_data_top_10_df['Year'], statistical_data_top_10_df['Average food supply quantity, kg'],color='red', label="average quantity")
# axs[0].legend(loc="lower right")
# axs[1].bar(merged_table['Year'], merged_table['Total_food_supply_quality, kcal/capita/day'],color='green', label="food quality")
# axs[1].legend(loc="lower right")
# axs[2].bar(merged_table['Year'], merged_table['Number of deaths from digestive diseases'],color='blue', label="numbers of deaths")
# axs[2].legend(loc="lower right")
# axs[3].bar(merged_table['Year'], merged_table['Total fertilizer use per area of cropland in kg per hectare'],color='orange', label="numbers of deaths")
# axs[3].legend(loc="lower right")
# #plt.bar(statistical_data_top_10_df['Year'], statistical_data_top_10_df['Average food supply quantity, kg'],color='red', width=0.25, label="supply quantity")
# plt.show()
