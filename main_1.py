import statistics
import math
import random


def readInput():
    f = open('po_list.txt', 'r')

    data = f.readlines()

    # Number of post offices
    number_po = int(data[0])

    # Parcel number list of post offices, starting from index 1
    list_parcel = [0] * (number_po + 1)

    for i in range(1, number_po + 1):
        list_parcel[i] = int(data[i].replace('\n', ''))

    # Number of postman
    number_postman = int(data[number_po + 1])

    # Number of post offices that each postman can do
    po_per_postman = int(data[number_po + 2])

    # Post office list of each postman, starting from index 1
    list_po_of_postman = [[0] * po_per_postman] * (number_postman + 1)

    min_index_pm = number_po + 3

    for i in range(min_index_pm, min_index_pm + number_postman):
        list_po_of_postman[i - min_index_pm + 1] = [int(j) for j in data[i].replace('\n', '').split(' ')]


    return list_parcel, list_po_of_postman, number_postman, number_po, po_per_postman


def calculateObjValue(list_parcel_average):
    tmp_list = list()   # list of substraction beetween average of parcels

    len_pa = len(list_parcel_average)

    for i in range(1, len_pa):
        for j in range(i + 1, len_pa):
            tmp_list.append(math.fabs(list_parcel_average[i] - list_parcel_average[j]))

    tmp_list.sort()

    median = statistics.median(tmp_list)

    mean = statistics.mean(tmp_list)

    max_min_sub = tmp_list[-1] - tmp_list[0]

    # Return average of substraction beetween mean, median and max_min_sub
    return (math.fabs(median - mean) + math.fabs(mean - max_min_sub) + math.fabs(max_min_sub - median)) / 3


def generateRandomSolution(number_postman, number_po, po_per_postman, list_po_of_postman):

    # x[i] = j means postman i work at post office j
    x = [0 for i in range(number_postman + 1)]

    number_postman_in_po_list = [0 for i in range(number_po + 1)]

    check = True
    j = 1
    # While loop of generate random solution must satisfy for all of post offices have postman
    while check:
        print(j)
        number_postman_in_po_list = [0 for i in range(number_po + 1)]

        for i in range(1, number_postman + 1):
            while True:
                random_post_office = random.randint(1, number_po)
                check_x = list_po_of_postman[i][random_post_office]

                if  check_x == 1:
                    number_postman_in_po_list[random_post_office] += 1
                    x[i] = random_post_office
                    break

        print('x:', x)
        print('number_postman:', number_postman_in_po_list)
        # Check all of post offices must have postman
        for i in range(1, number_po + 1):
            if number_postman_in_po_list[i] == 0:
                break
            else:
                if i == number_po:
                    check = False
        j += 1

    return x, number_postman_in_po_list

def main():

    list_parcel, list_po_of_postman, number_postman, number_po, po_per_postman = readInput()

    '''
        Variables
    '''

    obj = 0
    objS = 999999


    x = [0 for i in range(number_postman + 1)]


    number_postman_in_po_list = [0 for i in range(number_po + 1)]

    # Checked list of post offices that each postman can do.
    # If postman i can do at post office j, check_x[i][j] = 1.
    check_x = [[0 for i in range(number_po + 1)] for i in range(number_postman + 1)]

    for i in range(1, number_postman + 1):
        for j in list_po_of_postman[i]:
            check_x[i][j] = 1

    # x_ij - postman i works in post office j
    # And postman number of post office
    x, number_postman_in_po_list = generateRandomSolution(number_postman, number_po, po_per_postman, check_x)

    print(x)
    print(number_postman_in_po_list)


main()