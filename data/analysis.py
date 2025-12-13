import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sales.csv")
summary = df.groupby("product")["amount"].sum()

summary.plot(kind="bar")
plt.show()
