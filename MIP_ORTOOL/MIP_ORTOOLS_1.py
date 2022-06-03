from ortools.linear_solver import pywraplp
import time
from datetime import datetime
import pandas as pd
import math


# def main():
#     # Create the mip solver with the SCIP backend.
#     solver = pywraplp.Solver.CreateSolver('SCIP')
#
#     infinity = solver.infinity()
#     # x and y are integer non-negative variables.
#     x = solver.IntVar(0.0, infinity, 'x')
#     y = solver.IntVar(0.0, infinity, 'y')
#
#     print('Number of variables =', solver.NumVariables())
#
#     # x + 7 * y <= 17.5.
#     solver.Add(x + 7 * y <= 17.5)
#
#     # x <= 3.5.
#     solver.Add(x <= 3.5)
#
#     print('Number of constraints =', solver.NumConstraints())
#
#     # Maximize x + 10 * y.
#     solver.Maximize(x + 10 * y)
#
#     status = solver.Solve()
#
#     if status == pywraplp.Solver.OPTIMAL:
#         print('Solution:')
#         print('Objective value =', solver.Objective().Value())
#         print('x =', x.solution_value())
#         print('y =', y.solution_value())
#     else:
#         print('The problem does not have an optimal solution.')
#
#     print('\nAdvanced usage:')
#     print('Problem solved in %f milliseconds' % solver.wall_time())
#     print('Problem solved in %d iterations' % solver.iterations())
#     print('Problem solved in %d branch-and-bound nodes' % solver.nodes())
#
#
# if __name__ == '__main__':
#     main()


def read_data():
    df_parcel = pd.read_csv('../aaa.csv', header=0)
    df_post_office = pd.read_csv('../po_address_7_district.csv', header=0)

    '''
        List of distances of parcel in hoan kiem district
    '''

    hoan_kiem_list = list()

    # lat, long of hoan kiem post office
    df_po_hk = df_post_office.query('district == "hoàn kiếm"')
    lat_po = 0
    long_po = 0

    for index, row in df_po_hk.iterrows():
        lat_po = df_po_hk['lat'][index]
        long_po = df_po_hk['long'][index]

    df_parcel_hoan_kiem = df_parcel.query('district == "hoàn kiếm"')

    for index, row in df_parcel_hoan_kiem.iterrows():
        lat = int(df_parcel_hoan_kiem['lat'][index] * 1000)
        long = int(df_parcel_hoan_kiem['long'][index] * 1000)

        # Calculate distance between parcel and post office
        distance = int(math.sqrt((lat - lat_po) * (lat - lat_po) + (long - long_po) * (long - long_po)) * 100)

        hoan_kiem_list.append(distance)

    '''
        List of distances of parcel in ba dinh district
    '''

    ba_dinh_list = list()

    # lat, long of ba dinh post office
    df_po_bd = df_post_office.query('district == "ba đình"')
    lat_po = 0
    long_po = 0

    for index, row in df_po_bd.iterrows():
        lat_po = df_po_bd['lat'][index]
        long_po = df_po_bd['long'][index]

    df_parcel_ba_dinh = df_parcel.query('district == "ba đình"')

    for index, row in df_parcel_ba_dinh.iterrows():
        lat = int(df_parcel_ba_dinh['lat'][index] * 1000)
        long = int(df_parcel_ba_dinh['long'][index] * 1000)

        # Calculate distance between parcel and post office
        distance = int(math.sqrt((lat - lat_po) * (lat - lat_po) + (long - long_po) * (long - long_po)) * 100)

        ba_dinh_list.append(distance)

    '''
        List of distances of parcel in cau giay district
    '''

    cau_giay_list = list()

    # lat, long of cau giay post office
    df_po_cg = df_post_office.query('district == "cầu giấy"')
    lat_po = 0
    long_po = 0

    for index, row in df_po_cg.iterrows():
        lat_po = df_po_cg['lat'][index]
        long_po = df_po_cg['long'][index]

    df_parcel_cau_giay = df_parcel.query('district == "cầu giấy"')

    for index, row in df_parcel_cau_giay.iterrows():
        lat = int(df_parcel_cau_giay['lat'][index] * 1000)
        long = int(df_parcel_cau_giay['long'][index] * 1000)

        # Calculate distance between parcel and post office
        distance = int(math.sqrt((lat - lat_po) * (lat - lat_po) + (long - long_po) * (long - long_po)) * 100)

        cau_giay_list.append(distance)

    '''
        List of distances of parcel in hai ba trung district
    '''

    hai_ba_trung_list = list()

    # lat, long of hai ba trung post office
    df_po_hbt = df_post_office.query('district == "hai bà trưng"')
    lat_po = 0
    long_po = 0

    for index, row in df_po_hbt.iterrows():
        lat_po = df_po_hbt['lat'][index]
        long_po = df_po_hbt['long'][index]

    df_parcel_hai_ba_trung = df_parcel.query('district == "hai bà trưng"')

    for index, row in df_parcel_hai_ba_trung.iterrows():
        lat = int(df_parcel_hai_ba_trung['lat'][index] * 1000)
        long = int(df_parcel_hai_ba_trung['long'][index] * 1000)

        # Calculate distance between parcel and post office
        distance = int(math.sqrt((lat - lat_po) * (lat - lat_po) + (long - long_po) * (long - long_po)) * 100)

        hai_ba_trung_list.append(distance)

    '''
        List of distances of parcel in nam tu liem district
    '''

    nam_tu_liem_list = list()

    # lat, long of nam_tu_liem post office
    df_po_ntl = df_post_office.query('district == "nam từ liêm"')
    lat_po = 0
    long_po = 0

    for index, row in df_po_ntl.iterrows():
        lat_po = df_po_ntl['lat'][index]
        long_po = df_po_ntl['long'][index]

    df_parcel_nam_tu_liem = df_parcel.query('district == "nam từ liêm"')

    for index, row in df_parcel_nam_tu_liem.iterrows():
        lat = int(df_parcel_nam_tu_liem['lat'][index] * 1000)
        long = int(df_parcel_nam_tu_liem['long'][index] * 1000)

        # Calculate distance between parcel and post office
        distance = int(math.sqrt((lat - lat_po) * (lat - lat_po) + (long - long_po) * (long - long_po)) * 100)

        nam_tu_liem_list.append(distance)

    '''
        List of distances of parcel in dong da district
    '''

    dong_da_list = list()

    # lat, long of dong da post office
    df_po_dd = df_post_office.query('district == "đống đa"')
    lat_po = 0
    long_po = 0

    for index, row in df_po_dd.iterrows():
        lat_po = df_po_dd['lat'][index]
        long_po = df_po_dd['long'][index]

    df_parcel_dong_da = df_parcel.query('district == "đống đa"')

    for index, row in df_parcel_dong_da.iterrows():
        lat = int(df_parcel_dong_da['lat'][index] * 1000)
        long = int(df_parcel_dong_da['long'][index] * 1000)

        # Calculate distance between parcel and post office
        distance = int(math.sqrt((lat - lat_po) * (lat - lat_po) + (long - long_po) * (long - long_po)) * 100)

        dong_da_list.append(distance)

    '''
        List of distances of parcel in thanh xuan district
    '''

    thanh_xuan_list = list()

    # lat, long of thanh xuan post office
    df_po_tx = df_post_office.query('district == "thanh xuân"')
    lat_po = 0
    long_po = 0

    for index, row in df_po_tx.iterrows():
        lat_po = df_po_tx['lat'][index]
        long_po = df_po_tx['long'][index]

    df_parcel_thanh_xuan = df_parcel.query('district == "thanh xuân"')

    for index, row in df_parcel_thanh_xuan.iterrows():
        lat = int(df_parcel_thanh_xuan['lat'][index] * 1000)
        long = int(df_parcel_thanh_xuan['long'][index] * 1000)

        # Calculate distance between parcel and post office
        distance = int(math.sqrt((lat - lat_po) * (lat - lat_po) + (long - long_po) * (long - long_po)) * 100)

        thanh_xuan_list.append(distance)


    '''
        Read list post office of a postman
    '''

    f = open('../po_list_1.txt', 'r')

    data = f.readlines()

    number_postman = int(data[0])
    po_per_postman = int(data[1])

    list_po_of_postman = [[0] * po_per_postman] * (number_postman + 1)

    for i in range(2, 2 + number_postman):
        list_po_of_postman[i - 1] = [int(j) for j in data[i].replace('\n', '').split(' ')]

    return hoan_kiem_list, ba_dinh_list, hai_ba_trung_list, nam_tu_liem_list, dong_da_list, thanh_xuan_list, cau_giay_list,\
           list_po_of_postman


def solve():
    hoan_kiem_list, ba_dinh_list, hai_ba_trung_list, nam_tu_liem_list, dong_da_list, thanh_xuan_list, cau_giay_list,\
    list_po_of_postman = read_data()


    sum_distance = [0] * 8

    sum_distance[1] = sum(hoan_kiem_list)
    sum_distance[2] = sum(ba_dinh_list)
    sum_distance[3] = sum(hai_ba_trung_list)
    sum_distance[4] = sum(nam_tu_liem_list)
    sum_distance[5] = sum(dong_da_list)
    sum_distance[6] = sum(thanh_xuan_list)
    sum_distance[7] = sum(cau_giay_list)

    number_postman = len(list_po_of_postman) - 1

    print('list_po_of_postman:', list_po_of_postman)
    print('number_postman:', number_postman)

    print('po_per_postman:', 3)

    number_po = 7

    # Xij - postman i works in post office j
    x = [[0 for i in range(number_po + 1)] for i in range(number_postman + 1)]
    check_x = [[0 for i in range(number_po + 1)] for i in range(number_postman + 1)]

    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')

    infinity = solver.infinity()

    # Declare variables
    for i in range(1, number_postman + 1):
        for j in list_po_of_postman[i]:
            x[i][j] = solver.IntVar(0.0, infinity, 'x%s%s' % (i, j))
            check_x[i][j] = 1

    obj = solver.NumVar(0.0, infinity, 'obj')

    print('Number of variables =', solver.NumVariables())

    # list of sum postman of post office, begin at index 1
    list_sp = [0.0] * (number_po + 1)

    for i in range(1, number_po + 1):
        for j in range(1, number_postman + 1):
            list_sp[i] += x[j][i]

    # list of average postman/parcel of post office, begin at index 1
    list_px = [0.0] * (number_po + 1)
    for i in range(1, number_po + 1):
        list_px[i] = list_sp[i] / sum_distance[i]


    '''
        Add constraints
    '''

    # Constraint: Sum of postman in a post office must greater than or equal 1
    for i in range(1, number_po + 1):
        solver.Add(list_sp[i] >= 1)

    # Constraint: A postman only do at a post office
    for i in range(1, number_postman + 1):
        s = 0
        for j in x[i]:
            s += j

        solver.Add(s == 1)

    for i in range(1, number_po + 1):
        for j in range(i + 1, number_po + 1):
            solver.Add(obj >= list_px[i] - list_px[j])
            solver.Add(obj >= list_px[j] - list_px[i])

    print('Number of constraints =', solver.NumConstraints())

    solver.Minimize(obj)

    start_time = time.time()
    print(datetime.now())

    status = solver.Solve()

    print(datetime.now())
    print('End in:', time.time() - start_time)

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Objective value =', solver.Objective().Value())

        for i in range(1, number_postman + 1):
            for j in range(1, number_po + 1):
                if check_x[i][j] == 1:
                    print('x[%s][%s]' % (i, j), x[i][j].solution_value())


        for j in range(1, number_po + 1):
            s = 0
            for i in range(1, number_postman + 1):
                if check_x[i][j] == 1:
                    s += x[i][j].solution_value()


            print(s, sum_distance[j])
            print('list_px_%s' % j , list_px[j].solution_value())


    else:
        print('The problem does not have an optimal solution.')

solve()