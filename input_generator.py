import random


number_po = 27
min_postman_per_po = 5
max_postman_per_po = 20
min_parcel_per_postman = 40
max_parcel_per_postman = 177

min_parcel_per_po = min_postman_per_po * min_parcel_per_postman * 2
max_parcel_per_po = max_postman_per_po * max_parcel_per_postman

for i in range(1, 51):
    f0 = open('first_po_list_data/po_list_%s.txt' % i, 'r')
    data = f0.readlines()

    f = open('input_1/po_list_%s.txt' % i, 'w')
    f.writelines(data)
    # f.writelines(str(number_po) + '\n')
    #
    # for j in range(number_po):
    #     f.writelines(str(random.randint(min_parcel_per_po, max_parcel_per_po)) + '\n')
    #
    number_postman = int(data[-1])

    f.writelines(str(4) + '\n')

    for p in range(number_postman):
        s = ''

        for k in range(4):
            s += str(random.randint(1, number_po)) + ' '

        if p == number_postman - 1:
            s = s[:-1]
        else:
            s = s[:-1] + '\n'

        f.writelines(s)

    f.close()
    f0.close()

