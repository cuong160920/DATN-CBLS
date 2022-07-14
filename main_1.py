import statistics
import math
import random
import time
import csv


def readInput(filepath):
    """
    Read data from file po_list.txt

    :return:
        parcel_list: list of parcels of post offices
        po_of_postman_list: list of post offices of each postman can work in it
        number_postman: number of postmans
        number_po: number of post offices
        po_per_postman: number of post offices that each postman can work in it
    """

    f = open(filepath, 'r')

    data = f.readlines()

    # Number of post offices
    number_po = int(data[0])

    # Parcel number list of post offices, starting from index 1
    parcel_list = [0] * (number_po + 1)

    for i in range(1, number_po + 1):
        parcel_list[i] = int(data[i].replace('\n', ''))

    # Number of postman
    number_postman = int(data[number_po + 1])

    # Number of post offices that each postman can do
    po_per_postman = int(data[number_po + 2])

    # Post office list of each postman, starting from index 1
    po_of_postman_list = [[0] * po_per_postman] * (number_postman + 1)

    min_index_pm = number_po + 3

    for i in range(min_index_pm, min_index_pm + number_postman):
        po_of_postman_list[i - min_index_pm + 1] = [int(j) for j in data[i].replace('\n', '').split(' ')]


    return parcel_list, po_of_postman_list, number_postman, number_po, po_per_postman


def generate_average_parcel_list(number_postman_in_po_list, parcel_list):
    """
    Calculate average number of parcels per postman in post offices

    :param number_postman_in_po_list: list of number of postmans in post offices
    :param parcel_list: list of parcels of post offices
    :return: list of average of parcels per postman in post offices
    """

    l = len(parcel_list)
    average_parcel_list = [0] * l

    for i in range(1, l):
        average_parcel_list[i] += parcel_list[i] / number_postman_in_po_list[i]

    return average_parcel_list


def calculateNumberPostmanInPoList(number_po, number_postman, x):
    """
    Calculate number of postmans in each post office

    :param number_po: number of post offices
    :param number_postman: number of postmans
    :param x: solution
    :return: list of number of postmans in each post office
    """

    number_postman_in_po_list = [0 for i in range(number_po + 1)]

    for i in range(1, number_postman + 1):
        number_postman_in_po_list[x[i]] += 1

    return number_postman_in_po_list


def calculateObjValue(average_parcel_list):
    """
    Calculate objective value

    :param average_parcel_list: list of average of parcels per postman in post offices
    :return: objective value
    """
    tmp_list = list()   # list of substraction beetween average of parcels

    len_pa = len(average_parcel_list)

    for i in range(1, len_pa):
        for j in range(i + 1, len_pa):
            tmp_list.append(math.fabs(average_parcel_list[i] - average_parcel_list[j]))

    # tmp_list.sort()

    # median = statistics.median(tmp_list)

    mean = statistics.mean(tmp_list)

    # max_min_sub = tmp_list[-1] - tmp_list[0]

    # Return average of substraction beetween mean, median and max_min_sub
    # return (math.fabs(median - mean) + math.fabs(mean - max_min_sub) + math.fabs(max_min_sub - median)) / 3
    return mean


def generateRandomSolution(number_postman, number_po, check_x):
    """
    Generate a random solution

    :param number_postman: number of postmans
    :param number_po: number of post offices
    :param check_x: marked list of possible post offices of each postman
    :return: random solution
    """

    # x[i] = j means postman i work at post office j
    x = [0 for i in range(number_postman + 1)]

    check = True

    # While loop of generate random solution must satisfy for all of post offices have postman
    while check:
        for i in range(1, number_postman + 1):
            while True:
                random_post_office = random.randint(1, number_po)
                check_po = check_x[i][random_post_office]

                if check_po == 1:
                    x[i] = random_post_office
                    break

        number_postman_in_po_list = calculateNumberPostmanInPoList(number_po, number_postman, x)

        # Check all of post offices must have postman
        for i in range(1, number_po + 1):
            if number_postman_in_po_list[i] == 0:
                break
            else:
                if i == number_po:
                    check = False

    return x, number_postman_in_po_list


def hillClimbing(x, check_x, number_postman, number_po, parcel_list, number_postman_in_po_list):
    """
    Find the best solution starting from a initial solution

    :param x: initial solution
    :param check_x: marked list of possible post offices of each postman
    :param number_postman: number of postmans
    :param number_po: number of post offices
    :param parcel_list: list of parcels of each post office
    :param number_postman_in_po_list: list of number of postmans in post offices
    :return: the best solution and the best value
    """

    # Initial point
    solution = x
    number_postman_in_po_list_sol = number_postman_in_po_list.copy()

    average_parcel_list = generate_average_parcel_list(number_postman_in_po_list_sol, parcel_list)

    sol_value = calculateObjValue(average_parcel_list)

    for postman in range(1, number_postman + 1):
        tmp_check = [0] * (number_po + 1)
        tmp_check[solution[postman]] = 1

        for post_office in range(1, number_po + 1):
            if check_x[postman][post_office] == 1 and tmp_check[post_office] == 0:
                tmp_check[post_office] = 1
                solution_tmp = solution.copy()
                number_postman_in_po_list_tmp = number_postman_in_po_list_sol.copy()

                if number_postman_in_po_list_tmp[solution_tmp[postman]] > 1:
                    number_postman_in_po_list_tmp[post_office] += 1
                    number_postman_in_po_list_tmp[solution_tmp[postman]] -= 1

                    solution_tmp[postman] = post_office

                    average_parcel_list_tmp = generate_average_parcel_list(number_postman_in_po_list_tmp, parcel_list)

                    sol_value_tmp = calculateObjValue(average_parcel_list_tmp)

                    if  sol_value_tmp <= sol_value:
                        sol_value = sol_value_tmp
                        solution = solution_tmp.copy()
                        number_postman_in_po_list_sol = number_postman_in_po_list_tmp.copy()
                        average_parcel_list = average_parcel_list_tmp.copy()


    return solution, sol_value


def ILS(i, n_restarts, check_x, number_po, number_postman, parcel_list):
    """
    Iterated Local Search

    :param n_restarts: random restarts
    :param check_x: marked list of possible post offices of each postman
    :param number_po: number of post offices
    :param number_postman: number of postmans
    :param parcel_list: list of parcels of post offices
    :return: the best solution and the best value after n restarts hillClimbing
    """

    best_solution, number_postman_in_po_list = generateRandomSolution(number_postman, number_po, check_x)

    average_parcel_list = generate_average_parcel_list(number_postman_in_po_list, parcel_list)

    best_value = calculateObjValue(average_parcel_list)

    f0 = open('result/result_csv_%s.csv' % i, 'w', newline='')

    writer = csv.writer(f0)

    writer.writerow([-1, best_value])

    for n in range(n_restarts):
        initial_x, initial_number_postman_in_po_list = generateRandomSolution(number_postman, number_po, check_x)

        tmp_solution, tmp_value = hillClimbing(initial_x, check_x, number_postman, number_po, parcel_list, initial_number_postman_in_po_list)

        if tmp_value <= best_value:
            best_value = tmp_value
            best_solution = tmp_solution.copy()

            writer.writerow([n, tmp_value])

    f0.close()

    return best_solution, best_value


def main():
    # f = open('result_1.txt', 'w'

    for j in range(1, 51):
        filepath = 'input_1/po_list_%s.txt' % (j)
        print(filepath)
        parcel_list, po_of_postman_list, number_postman, number_po, po_per_postman = readInput(filepath)

        # print('parcel_list:', parcel_list)
        # print('po_of_postman_list:', po_of_postman_list)
        # print('number_postman:', number_postman)
        # print('po_per_postman:', po_per_postman)

        # Checked list of post offices that each postman can do.
        # If postman i can do at post office j, check_x[i][j] = 1.
        check_x = [[0 for i in range(number_po + 1)] for i in range(number_postman + 1)]

        for i in range(1, number_postman + 1):
            for p in po_of_postman_list[i]:
                check_x[i][p] = 1

        # x_ij - postman i works in post office j
        # And postman number of post office

        n_restarts = 100

        best_solution, best_value = ILS(j, n_restarts, check_x, number_po, number_postman, parcel_list)

        number_postman_in_po_list = calculateNumberPostmanInPoList(number_po, number_postman, best_solution)

        average_parcel_list = generate_average_parcel_list(number_postman_in_po_list, parcel_list)

        string_best_solution = [str(int) for int in best_solution]
        string_average_parcel_list = [str(int) for int in average_parcel_list]

        # tmp = list()
        #
        # tmp.append(k)
        # tmp.append(j)
        # tmp.append(best_value)
        #
        # writer.writerow(tmp)
        # f.writelines(str(j) + ' ' + str(k) + '\n')
        # f.writelines('Best solution:' +  ' '.join(string_best_solution) + '\n')
        # f.writelines('Best value:' + str(best_value) + '\n')
        # f.writelines('Number postman in po:' + str(number_postman_in_po_list) + '\n')
        # f.writelines('Average:' +  ' '.join(string_average_parcel_list) + '\n\n')

    # f.close()
    # f0.close()


main()
