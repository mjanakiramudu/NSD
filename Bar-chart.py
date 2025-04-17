import numpy as np
import matplotlib.pyplot as plt
months=["jan",'feb','march','april','may','june']
np.random.seed(42)
sales=np.random.randint(40,100,6)
colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan']
bars=plt.bar(months,sales,color=colors,edgecolor='black')
plt.title("Bar chart - Sales Data")
plt.xlabel("Months")
plt.ylabel("Sales in 1000")
legend_labels = [f"{months[i]} ({colors[i]})" for i in range(len(months))]
plt.legend(bars, legend_labels, title="Month Colors", bbox_to_anchor=(1.05, 1), loc='upper left')
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
             str(bar.get_height()), ha='center', fontsize=12, fontweight='bold')