import pandas as pd


ferlizers = pd.read_excel(
    './fertilizers-&-pesticides-&-deaths-in-raw-tables.xlsx', sheet_name='fertilizer-per-hectare')
pesticides = pd.read_excel('./fertilizers-&-pesticides-&-deaths-in-raw-tables.xlsx',
                           sheet_name='pesticide-use-per-hectare-of-cr')
deaths_from_digest_disease = pd.read_excel(
    './fertilizers-&-pesticides-&-deaths-in-raw-tables.xlsx', sheet_name='annual-number-of-deaths-by-caus')
# print("Content of the Fertilizers file:")
# print(ferlizers.columns.ravel())
# print("Content of the Pesticides file:")
# print(pesticides.columns.ravel())
# print()
ferlizers_cleaned = ferlizers.dropna(subset=['Code'])
# print(ferlizers_cleaned)
pesticides_cleaned = pesticides.dropna(subset=['Code'])
# print(pesticides_cleaned)
all_combined = ferlizers_cleaned.merge(pesticides_cleaned, on=["Code", "Year", "Entity"]).merge(
    deaths_from_digest_disease, on=["Code", "Year", "Entity"])
# print(updated_fertilizers)
# print("Content of the Combined file:")
# print(updated_fertilizers.columns.ravel())
# print(updated_fertilizers.head())
all_combined.to_csv('fertilizers_with_pesticides.csv', index=False)
print(len(all_combined.columns))

food_supply_quantity_before_2009 = pd.read_excel(
    './food_supply_quantity_-2009.xls', sheet_name='Sheet1')
food_supply_quantity_2010_onwards = pd.read_excel(
    './food_supply_quantity_2010-.xls', sheet_name='Sheet1')
food_supply_quantity_concat = pd.concat(
    [food_supply_quantity_before_2009, food_supply_quantity_2010_onwards], axis=0)
# print(len(food_supply_quantity_before_2009.index))
# print(len(food_supply_quantity_2010_onwards.index))
# print(len(food_supply_quantity_concat.index))
print(len(food_supply_quantity_before_2009.columns))
print(len(food_supply_quantity_2010_onwards.columns))
print(len(food_supply_quantity_concat.columns))
# food_supply_quantity_concat.to_csv('./food_supply_quantity_concat.csv', index=False)

# food_supply_quantity_2010_onwards[['Entity', 'Year', 'Total_Value']]  = food_supply_quantity_2010_onwards.groupby(by=['Entity', 'Year'], as_index= False)['Value'].sum()
total_food_supply_quantity_per_coutry_and_year = food_supply_quantity_concat.groupby(
    by=['Entity', 'Year'])['Value'].sum()
total_food_supply_quantity_per_coutry_and_year_dataframe = total_food_supply_quantity_per_coutry_and_year.to_frame(
    name="Total_food_supply_quantity, kg").reset_index()
food_supply_quantity_concat_with_total_food_supply_quantity = food_supply_quantity_concat.merge(
    total_food_supply_quantity_per_coutry_and_year_dataframe, on=['Entity', 'Year'])
# print(type(food_supply_quantity_concat_updated))
print(food_supply_quantity_concat_with_total_food_supply_quantity)
print(len(food_supply_quantity_concat_with_total_food_supply_quantity.columns))
# print(test.columns.ravel())
food_supply_quantity_concat_with_total_food_supply_quantity.to_csv(
    './food_supply_quantity_concat_with_total_food_supply_quantity.csv', index=False)

all_combined = all_combined.merge(
    total_food_supply_quantity_per_coutry_and_year_dataframe, on=['Entity', 'Year'])
print(len(all_combined.columns))
all_combined.to_csv(
    './fertilizers_with_pesticides_with_total_food_supply_quantity.csv', index=False)


food_supply_quality_before_2009 = pd.read_excel(
    './food_supply_quality_-2009.xls', sheet_name='Sheet1')
food_supply_quality_2010_onwards = pd.read_excel(
    './food_supply_quality_2010-.xls', sheet_name='Sheet1')
food_supply_quality_concat = pd.concat(
    [food_supply_quality_before_2009, food_supply_quality_2010_onwards], axis=0)
# print(len(food_supply_quantity_before_2009.index))
# print(len(food_supply_quantity_2010_onwards.index))
# print(len(food_supply_quantity_concat.index))
print(len(food_supply_quality_before_2009.columns))
print(len(food_supply_quality_2010_onwards.columns))
print(len(food_supply_quality_concat.columns))
# food_supply_quantity_concat.to_csv('./food_supply_quantity_concat.csv', index=False)

# food_supply_quantity_2010_onwards[['Entity', 'Year', 'Total_Value']]  = food_supply_quantity_2010_onwards.groupby(by=['Entity', 'Year'], as_index= False)['Value'].sum()
total_food_supply_quality_per_coutry_and_year = food_supply_quality_concat.groupby(
    by=['Entity', 'Year'])['Value'].sum()
total_food_supply_quality_per_coutry_and_year_dataframe = total_food_supply_quality_per_coutry_and_year.to_frame(
    name="Total_food_supply_quality, kcal/capita/day").reset_index()
food_supply_quality_concat_with_total_food_supply_quality = food_supply_quality_concat.merge(
    total_food_supply_quality_per_coutry_and_year_dataframe, on=['Entity', 'Year'])
# print(type(food_supply_quantity_concat_updated))
print(food_supply_quality_concat_with_total_food_supply_quality)
print(len(food_supply_quality_concat_with_total_food_supply_quality.columns))
# print(test.columns.ravel())
food_supply_quality_concat_with_total_food_supply_quality.to_csv(
    './food_supply_quality_concat_with_total_food_supply_quality.csv', index=False)

all_combined = all_combined.merge(
    total_food_supply_quality_per_coutry_and_year_dataframe, on=['Entity', 'Year'])
print(len(all_combined.columns))

all_combined.to_csv('./all_combined.csv', index=False)
