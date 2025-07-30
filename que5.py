import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.ndimage import rotate
from scipy.stats import pearsonr , chi2_contingency


sns.set(style="whitegrid")

df =pd.read_csv("/home/vedant/Downloads/demographic_data.csv")

plt.figure(figsize=(10,6))
sns.histplot(data=df,x="Age",y="Education Level",multiple="dodge",palette="Set2",bins=10,legend=False,hue="Education Level")
plt.savefig("Age_distribution_by_EDUlevel.png")
