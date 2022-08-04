import pandas as pd
import matplotlib.pyplot as plt


for i in range(6, 11):
    df = pd.read_csv('nrestart_result/result_csv_%i.csv' % i, header=None)

    x = df[0]
    m = df[1].min()
    y = df[1].apply(lambda x: float(x) - m)
    # y = df[1]
    plt.subplot()
    plt.scatter(x, y)
plt.xlabel("Time")
plt.ylabel("Objective Value")
plt.show()