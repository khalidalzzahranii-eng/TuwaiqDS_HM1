import pandas as pd
import matplotlib.pyplot as plt

# Read data
df = pd.read_csv("data.csv")
print(df)

# Plot line chart with markers
fig, ax = plt.subplots(figsize=(10,6), dpi=150)

ax.plot(df['region'], df['temp'], marker='o', color='#0378A6', linestyle='-', linewidth=2, markersize=8)

ax.set_title('Average Temperatures in Saudi Arabia Regions')
ax.set_xlabel('Region')
ax.set_ylabel('Temperature (°C)')
ax.grid(True, linestyle='--', alpha=0.7)

plt.xticks(rotation=45)  # تدوير أسماء المناطق لسهولة القراءة
fig.tight_layout()
fig.savefig("Figure.png", bbox_inches="tight")
plt.show()
plt.close('all')
