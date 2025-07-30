import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr , chi2_contingency


sns.set(style="whitegrid")

df =pd.read_csv("/home/vedant/Downloads/demographic_data.csv")



#Scatter plot
plt.figure(figsize=(8,6))
sns.scatterplot(data=df,x="Age",y="Income",hue="Gender",style="Gender")
plt.savefig("Age_vs_Income_Correlation.png")
corr ,pval=pearsonr(df["Age"],df["Income"])
print(f"Correlation : {corr:.2f},p-value:{pval:.4g}")