import pandas as pd


all_combined = pd.read_csv('./all_combined.csv')
all_combined = all_combined.round(2)

all_combined.to_csv('./all_combined_clean.csv', index=False)