import pandas as pd
import math


pd.options.mode.chained_assignment = None
df = pd.read_csv('csv_folder/avg.csv', header=0)

df1 = df

buu_ta_list = df1['Bưu tá'].values.tolist()
order_list = df1['number_of_order'].values.tolist()
avg_1_list = df1['average_1'].values.tolist()
avg_2_list = df1['average_2'].values.tolist()

sum_order = df1['number_of_order'].sum()
sum_buuta = df1['Bưu tá'].sum()
avg_1 = sum_order / sum_buuta
avg_2 = sum_buuta / sum_order

print('Tổng đơn hàng:', sum_order)
print('Tổng bưu tá:', sum_buuta)
print('Trung bình đơn hàng trên bưu tá:', avg_1)
print('Trung bình bưu tá trên đơn hàng:', avg_2, '\n')


len_order = len(order_list)

df_2 = df1.query('average_1 <= @avg_1')

df_3 = df1.query('average_1 > @avg_1')
print(df_3.to_string())

total_remaining_order = 0

for index, row in df_3.iterrows():
    new_number_of_order = math.ceil(df_3['Bưu tá'][index] * avg_1)
    total_remaining_order += df_3['number_of_order'][index] - new_number_of_order

    df_3['number_of_order'][index] = new_number_of_order
    df_3['average_1'][index] = df_3['number_of_order'][index] / df_3['Bưu tá'][index]
    df_3['average_2'][index] = df_3['Bưu tá'][index] / df_3['number_of_order'][index]

print('\n', df_3.to_string())
print('\nTổng số đơn hàng cần chuyển sang các bưu cục có tỉ lệ đơn hàng / đầu người thấp hơn:', total_remaining_order)

print('\n', df_2.to_string())

for index, row in df_2.iterrows():
    new_number_of_order = math.ceil(df_2['Bưu tá'][index] * avg_1)
    remain_order = new_number_of_order - df_2['number_of_order'][index]

    if remain_order > total_remaining_order:
        df_2['number_of_order'][index] += total_remaining_order
        df_2['average_1'][index] = df_2['number_of_order'][index] / df_2['Bưu tá'][index]
        df_2['average_2'][index] = df_2['Bưu tá'][index] / df_2['number_of_order'][index]
        break
    else:
        total_remaining_order -= remain_order
        df_2['number_of_order'][index] = new_number_of_order
        df_2['average_1'][index] = df_2['number_of_order'][index] / df_2['Bưu tá'][index]
        df_2['average_2'][index] = df_2['Bưu tá'][index] / df_2['number_of_order'][index]

print('\n', df_2.to_string())

print('Tổng đơn hàng sau khi update:', df_2['number_of_order'].sum() + df_3['number_of_order'].sum())


# len_order = len(order_list)
#
# df_2 = df1.query('average_2 <= @avg_2')
#
# df_3 = df1.query('average_2 > @avg_2')
# print(df_3.to_string())
#
# total_remaining_postman = 0
#
# for index, row in df_3.iterrows():
#     new_number_of_postman = math.ceil(df_3['number_of_order'][index] * avg_2)
#     total_remaining_postman += df_3['Bưu tá'][index] - new_number_of_postman
#
#     df_3['Bưu tá'][index] = new_number_of_postman
#     df_3['average_1'][index] = df_3['number_of_order'][index] / df_3['Bưu tá'][index]
#     df_3['average_2'][index] = df_3['Bưu tá'][index] / df_3['number_of_order'][index]
#
# print('\n', df_3.to_string())
# print('\nTổng số bưu tá cần chuyển sang các bưu cục có tỉ lệ bưu tá / đơn hàng thấp hơn:', total_remaining_postman)
#
# print('\n', df_2.to_string())
#
# for index, row in df_2.iterrows():
#     new_number_of_postman = math.ceil(df_2['number_of_order'][index] * avg_2)
#     remain_postman = new_number_of_postman - df_2['Bưu tá'][index]
#
#     if remain_postman > total_remaining_postman:
#         df_2['Bưu tá'][index] += total_remaining_postman
#         df_2['average_1'][index] = df_2['number_of_order'][index] / df_2['Bưu tá'][index]
#         df_2['average_2'][index] = df_2['Bưu tá'][index] / df_2['number_of_order'][index]
#         break
#     else:
#         total_remaining_postman -= remain_postman
#         df_2['Bưu tá'][index] = new_number_of_postman
#
#         if df_2['Bưu tá'][index] != 0:
#             df_2['average_1'][index] = df_2['number_of_order'][index] / df_2['Bưu tá'][index]
#         else:
#             df_2['average_1'][index] = -1
#
#         if df_2['number_of_order'][index] != 0:
#             df_2['average_2'][index] = df_2['Bưu tá'][index] / df_2['number_of_order'][index]
#         else:
#             df_2['average_2'][index] = -1
#
# print('\n', df_2.to_string())
#
# print('Tổng bưu tá sau khi update:', df_2['Bưu tá'].sum() + df_3['Bưu tá'].sum())