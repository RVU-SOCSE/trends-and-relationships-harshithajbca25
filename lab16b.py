import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r"prog16a.csv")
plt.scatter(df['YearsExperience'], df['Salary'])
plt.ylabel('Salary')
plt.xlabel('YearsExperience')
plt.legend()
plt.show()
sns.scatterplot(x = df['Salary'], y = df['YearsExperience'])
plt.show()
