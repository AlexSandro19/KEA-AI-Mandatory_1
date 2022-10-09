import pandas as pd
import statistics

all_combined = pd.read_csv('./all_combined_clean.csv')


print(statistics.pvariance(all_combined['Total_food_supply_quantity, kg']))
print(statistics.pstdev(all_combined['Total_food_supply_quantity, kg']))