import random


number_po = 27
min_postman_per_po = 5
max_postman_per_po = 20
min_parcel_per_postman = 40
max_parcel_per_postman = 177

min_parcel_per_po = min_postman_per_po * min_parcel_per_postman
max_parcel_per_po = max_postman_per_po * max_parcel_per_postman

for i in range(1, 50):
    f = open('po_list_data/po_list_%s.txt' % i, 'w')
    f.write(number_po)
    for j in range(number_po):
        f.write()



