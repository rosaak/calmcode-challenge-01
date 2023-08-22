
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("data.csv")

fig, ax = plt.subplots(figsize=(10, 2))
for index, row in data.iterrows():
    ax.text(row['j'], row['i'], row['value'],
            ha='center', va='center', fontsize=8)
ax.set_ylim(max(data['i']) + 1, -1)
ax.set_xlim(-1, max(data['j']) + 1)
ax.axis('off')
plt.tight_layout()
plt.show()
