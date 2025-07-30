import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr , chi2_contingency

sns.set(style="whitegrid")

df =pd.read_csv("Resources/demographic_data.csv")


#Box plot Income by gender
plt.figure(figsize=(8,6))
sns.boxplot(data=df,x="Gender" , y="Income" , palette="Set2", hue="Gender" , legend=False)
plt.title("Income Distribution by gender")
plt.savefig("Income_by_gender_boxplot.png")


