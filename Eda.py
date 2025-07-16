import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("education_resources.csv")

print(df.info())
print(df.describe())

df['Subject'].value_counts().plot(kind='bar', title="Resources per Subject")
plt.xlabel("Subject")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
