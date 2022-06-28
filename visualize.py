import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv('result_csv_3.csv', header=0)

X = list(map(str, list(dict.fromkeys(df['test'].values.tolist()))))

number_po = list(map(str, list(dict.fromkeys(df['max_po'].values.tolist()))))

X_l = list()
for i in number_po:
    tmp = df.query('max_po == %s' % i)['objV'].values.tolist()
    X_l.append(tmp)


X_axis = np.arange(len(X))

width = 0.1

for i in range(len(number_po)):
    plt.bar(X_axis + width * i, X_l[i], width, label = 'Max PO ' + str(i + 1))

plt.xticks(X_axis, X)
plt.xlabel("Tests")
plt.ylabel("Objective Value")
plt.legend()
plt.show()



# X_axis = np.arange(len(X))
#
# print(X_axis - 0.2)
# print(X_axis + 0.2)
#
# plt.bar(X_axis - 0.2, Ygirls, 0.4, label='Girls')
# plt.bar(X_axis + 0.2, Zboys, 0.4, label='Boys')
#
# plt.xticks(X_axis, X)
# plt.xlabel("Groups")
# plt.ylabel("Number of Students")
# plt.title("Number of Students in each group")
# plt.legend()
# plt.show()