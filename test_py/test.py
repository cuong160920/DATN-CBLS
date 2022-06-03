import math

import pandas as pd


# df = pd.read_csv('post_office_address/all_post_office.csv', delimiter='|', header=0)
#
# print(df.to_string())
# import pandas as pd
# import random
#
# df = pd.read_csv('post_office_address/all_post_office.csv', header=0, delimiter='|')
#
# df.sort_values('Địa chỉ', inplace=True)
# df.drop_duplicates(subset='Địa chỉ', keep=False, inplace=True)
#
# len_df = len(df['Địa chỉ'])
#
# buu_ta = [random.randint(5, 20) for i in range(len_df)]
#
# df['Bưu tá'] = buu_ta
#
# df.to_csv('post_office_address/all_post_office_drop_duplicate.csv', index=False)

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))


df_1 = pd.read_csv('../csv_folder/added_district_data.csv', header=0)

df_order_address = df_1[['lat', 'long', 'district']]

df_2 = pd.read_csv('../post_office_address/all_post_office_drop_duplicate.csv', header=0)

df_post_office_address = df_2[['Mã bưu cục', 'lat', 'long', 'Quận', 'Bưu tá']]

post_office_group = {
    'ba đình': df_post_office_address.query('Quận == "ba đình"'),
    'bắc từ liêm': df_post_office_address.query('Quận == "bắc từ liêm"'),
    'cầu giấy': df_post_office_address.query('Quận == "cầu giấy"'),
    'đống đa': df_post_office_address.query('Quận == "đống đa"'),
    'hà đông': df_post_office_address.query('Quận == "hà đông"'),
    'hai bà trưng': df_post_office_address.query('Quận == "hai bà trưng"'),
    'hoàn kiếm': df_post_office_address.query('Quận == "hoàn kiếm"'),
    'hoàng mai': df_post_office_address.query('Quận == "hoàng mai"'),
    'long biên': df_post_office_address.query('Quận == "long biên"'),
    'nam từ liêm': df_post_office_address.query('Quận == "nam từ liêm"'),
    'tây hồ': df_post_office_address.query('Quận == "tây hồ"'),
    'thanh xuân': df_post_office_address.query('Quận == "thanh xuân"')
}

min_distances = list()
po_codes = list()

len_df_order_address = len(df_order_address['lat'])

for index in range(len_df_order_address):
    district = df_order_address['district'][index]

    lat = float(df_order_address['lat'][index])
    long = float(df_order_address['long'][index])

    try:
        df_po = post_office_group[district]

        distance_min = 99999
        po_code = '000000'

        for index_1, rows_1 in df_po.iterrows():
            lat_1 = float(df_po['lat'][index_1])
            long_1 = float(df_po['long'][index_1])

            distance = calculate_distance(lat, long, lat_1, long_1)

            if distance < distance_min:
                distance_min = distance
                po_code = df_po['Mã bưu cục'][index_1]

        min_distances.append(distance_min)
        po_codes.append(po_code)
    except:
        min_distances.append('')
        po_codes.append('')

df_order_address['min_distances'] = min_distances
df_order_address['po_code'] = po_codes

df_order_address.to_csv('order_address.csv', index=False)

dic_count = dict()

for po_code in po_codes:
    if po_code in dic_count:
        dic_count[po_code] += 1
    else:
        dic_count[po_code] = 1

list_count = list()
avg_1 = list()
avg_2 = list()

len_df_2 = len(df_2['lat'])

for i in range(len_df_2):
    try:
        c = dic_count[df_2['Mã bưu cục'][i]]
        list_count.append(c)
        avg_1.append(c / df_2['Bưu tá'][i])
        if c != 0:
            avg_2.append(df_2['Bưu tá'][i] / c)
        else:
            avg_2.append(-1)
    except:
        list_count.append(0)
        avg_1.append(0)
        avg_2.append(-1)

df_2['number_of_order'] = list_count
df_2['average_1'] = avg_1
df_2['average_2'] = avg_2

df_2.to_csv('avg.csv', index=False)
