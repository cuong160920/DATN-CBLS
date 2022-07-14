import pandas as pd
import matplotlib.pyplot as plt


for i in range(1, 51):
    df = pd.read_csv('result/result_csv_%i.csv' % i, header=None)

    x = df[0]
    y = df[1]

    plt.subplot()
    plt.plot(x, y)
plt.show()