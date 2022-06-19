import random


number_po_per_postman = 4
number_po = 27
min_postman_per_po = 5
max_postman_per_po = 20
min_parcel_per_postman = 40
max_parcel_per_postman = 177

min_parcel_per_po = min_postman_per_po * min_parcel_per_postman * 2
max_parcel_per_po = max_postman_per_po * max_parcel_per_postman

for i in range(1, 10):
    f = open('first_po_list_data/po_list_%s.txt' % i, 'w')
    f.writelines(str(number_po) + '\n')

    for j in range(number_po):
        f.writelines(str(random.randint(min_parcel_per_po, max_parcel_per_po)) + '\n')

    number_postman = 0
    for j in range(number_po):
        number_postman += random.randint(min_postman_per_po, max_postman_per_po)

    f.writelines(str(number_postman) + '\n')