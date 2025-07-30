import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.ndimage import rotate
from scipy.stats import pearsonr , chi2_contingency


sns.set(style="whitegrid")

df =pd.read_csv("Resources/demographic_data.csv")


ct1=pd.crosstab(df["Education Level"],df["Marital Status"])
print(ct1)

chi2,p,dof,expected =chi2_contingency(ct1)
print(f"\n Chi-squre test;\n Chi2={chi2:.2f},p-value={p:.4g}")
