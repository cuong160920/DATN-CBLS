import pandas as pd


def check_district(string):
    district_list = ['hoàng mai', 'hai bà trưng', 'ba đình', 'hoàn kiếm', 'thanh xuân', 'hà đông',
                     'đống đa', 'cầu giấy', 'nam từ liêm', 'bắc từ liêm', 'long biên', 'tây hồ']

    for district in district_list:
        if district in string:
            return True

    return False


def clear_district(district):
    return district.replace('quận', '').replace('huyện', '').replace('thị xã', '').strip()


df = pd.read_csv('csv_folder/data_result_clear.csv', header=0)

addresses = df['address']

df_district = list()

for address in addresses:
    try:
        arr = address.lower().split(',')

        district_1 = arr[-4]
        district_2 = arr[-3]

        if check_district(district_1):
            df_district.append(clear_district(district_1))
        elif check_district(district_2):
            df_district.append(clear_district(district_2))
        else:
            df_district.append('')

    except:
        df_district.append('')

df['district'] = df_district

df.to_csv('added_district_data.csv', encoding='utf-8-sig', index=False)