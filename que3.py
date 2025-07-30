import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.ndimage import rotate
from scipy.stats import pearsonr , chi2_contingency


sns.set(style="whitegrid")

df =pd.read_csv("/home/vedant/Downloads/demographic_data.csv")


plt.figure(figsize=(10,8))
sns.boxplot(data=df,x="Education Level",y="Income")
plt.xticks(rotation=45)
plt.title("Income Distribution by Education Level")
plt.savefig("Income_by_Education.png")
