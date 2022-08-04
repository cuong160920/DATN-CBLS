import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


sns.set_theme(style="darkgrid")

df = pd.read_csv('nrestart_result/result_csv_5.csv', header=None)

sns.lineplot(df[0], df[1])

plt.show()