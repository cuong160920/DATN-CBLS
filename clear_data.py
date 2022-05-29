# import csv
#
# f = open('data.csv', 'w', encoding='utf-8', newline='')
# writer = csv.writer(f)
#
# data = list()
#
# data.append('av')
# data.append('avafddfadf')
# data.append('aafasdfdas')
# print(data)
# writer.writerows(data)

# import pandas as pd
# import csv
#
#
# df = pd.read_csv('data_result.csv', header=0)
#
# df = df.dropna()
#
# df.sort_values('address', inplace=True)
# df.drop_duplicates(subset='address', keep=False, inplace=True)
#
# f = open('data_result_clear.csv', 'w', encoding='utf-8-sig', newline='')
# writer = csv.writer(f)
#
#
# for index, row in df.iterrows():
#     # if 'hà nội' in str(df['address'][index]).lower():
#     data = list()
#     data.append(df['address'][index])
#     data.append(df['lat'][index])
#     data.append(df['long'][index])
#
#     writer.writerow(data)
#     f.flush()
# import pandas as pd
# import matplotlib.pyplot as plt
#
# df = pd.read_csv('data_result_clear.csv', header=0)
#
# plt.scatter(x=df['lat'], y=df['long'])
# plt.show()