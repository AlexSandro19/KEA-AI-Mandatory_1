from turtle import color
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

all_combined = pd.read_csv('./all_combined_clean.csv')

fertilizers_use = all_combined.groupby(by=['Year'])['Total fertilizer use per area of cropland in kg per hectare'].mean().round(2)
fertilizers_use_df = fertilizers_use.to_frame(name="Average fertilizer use per area of cropland in kg per hectare").reset_index()
pesticides_use = all_combined.groupby(by=['Year'])['Pesticides used per area of cropland in kg per hectare'].mean().round(2)
pesticides_use_df = pesticides_use.to_frame(name="Average pesticides use per area of cropland in kg per hectare").reset_index()
deaths_from_digest = all_combined.groupby(by=['Year'])['Number of deaths from digestive diseases'].mean().div(100).round(2)
deaths_from_digest_df = deaths_from_digest.to_frame(name="Average number of deaths from digestive diseases").reset_index()
food_supply_quantity = all_combined.groupby(by=['Year'])['Total_food_supply_quantity, kg'].mean().round(2)
food_supply_quantity_df = food_supply_quantity.to_frame(name="Average food supply quantity, kg").reset_index()
food_supply_quality = all_combined.groupby(by=['Year'])['Total_food_supply_quality, kcal/capita/day'].mean().round(2)
food_supply_quality_df = food_supply_quality.to_frame(name="Average food supply quality, kcal/capita/day").reset_index()

years = list(range(1990, 2020))
statistical_data_df = pd.DataFrame(data=years, columns=['Year'])
statistical_data_df = statistical_data_df.merge(fertilizers_use_df, on='Year')
statistical_data_df = statistical_data_df.merge(pesticides_use_df, on='Year')
statistical_data_df = statistical_data_df.merge(deaths_from_digest_df, on='Year')
statistical_data_df = statistical_data_df.merge(food_supply_quantity_df, on='Year')
statistical_data_df = statistical_data_df.merge(food_supply_quality_df, on='Year')

# correlation_df = merged_df['Happiness_pct_change_2008-2018'].corr(merged_df['GDP_pct_change_2008-2018']);
# correlationStats = stats.pearsonr(merged_df['Happiness_pct_change_2008-2018'],merged_df['GDP_pct_change_2008-2018']);

# print("Correlation: ", correlation_df)

# print(statistical_data_df.head())
statistical_data_df.to_csv('./statistical_data.csv', index=False)

# plt.title("Scatter Plot")
# plt.xlabel('Year')
# plt.ylabel('Average number')
# plt.ylabel('Average fertilizer use per area of cropland in kg per hectare')
# plt.bar(statistical_data_df['Year']-0.3, statistical_data_df['Average fertilizer use per area of cropland in kg per hectare'], color='blue', width=0.25, label="fertilizers")
# plt.bar(statistical_data_df['Year'], statistical_data_df['Average food supply quantity, kg'],color='red', width=0.25, label="supply quantity")
# plt.bar(statistical_data_df['Year']+0.3, statistical_data_df['Average food supply quality, kcal/capita/day'],color='green', width=0.25, label="supply quality")
# for index, row in statistical_data_df.iterrows():
#     plt.text(int(row['GDP_pct_change_2008-2018']), int(row['Happiness_pct_change_2008-2018']), row['Entity'])
# plt.xlim([1989, 2020])
# plt.ylim([0, 200])

fig, axs = plt.subplots(5, 1, sharex=True)
# Remove vertical space between axes
fig.subplots_adjust(hspace=0.2)

# Plot each graph, and manually set the y tick values
axs[0].bar(statistical_data_df['Year'], statistical_data_df['Average fertilizer use per area of cropland in kg per hectare'],color='blue', label="fertilizers,kg/ha")
axs[1].bar(statistical_data_df['Year'], statistical_data_df['Average food supply quantity, kg'],color='red', label="average quantity,kg")
axs[2].bar(statistical_data_df['Year'], statistical_data_df['Average food supply quality, kcal/capita/day'],color='green', label='average quality,kcal/capita/day')
axs[3].bar(statistical_data_df['Year'], statistical_data_df["Average pesticides use per area of cropland in kg per hectare"],color='orange', label='pesticides,kg/ha')
axs[4].bar(statistical_data_df['Year'], statistical_data_df["Average number of deaths from digestive diseases"],color='black', label='deaths per 1000')
# axs[0].set_yticks(np.arange(-0.9, 1.0, 0.4))
# axs[0].set_ylim(-1, 1)

axs[0].legend(loc="lower right")
axs[1].legend(loc="lower right")
axs[2].legend(loc="lower right")
axs[3].legend(loc="lower right")
axs[4].legend(loc="lower right")
plt.show()