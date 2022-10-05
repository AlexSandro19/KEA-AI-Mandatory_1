import pandas as pd
import matplotlib.pyplot as plt
import scipy
top_fertilizers = pd.read_csv('./top_fertilizers.csv')
print()
results = scipy.stats.pearsonr(top_fertilizers['Total fertilizer use per area of cropland in kg per hectare'],top_fertilizers['Number of deaths from digestive diseases'])
print(results)
