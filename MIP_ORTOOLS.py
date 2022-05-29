from ortools.linear_solver import pywraplp
import time
from datetime import datetime


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
    f = open('po_list.txt', 'r')

    data = f.readlines()

    # Number post office
    number_po = int(data[0])

    # List of parcel of post office, begin at index 1
    parcel = [0] * (number_po + 1)

    for i in range(1, number_po + 1):
        parcel[i] = int(data[i].replace('\n', ''))

    number_postman = int(data[number_po + 1])

    # Number of post office, each postman can do
    po_per_postman = int(data[number_po + 2])

    list_po_of_postman = [[0] * po_per_postman] * (number_postman + 1)

    min_index_pm = number_po + 3

    for i in range(min_index_pm, min_index_pm + number_postman):
        list_po_of_postman[i - min_index_pm + 1] = [int(j) for j in data[i].replace('\n', '').split(' ')]

    return parcel, list_po_of_postman, number_postman, number_po, po_per_postman


def solve():
    parcel, list_po_of_postman, number_postman, number_po, po_per_postman = read_data()

    print('parcel:', parcel)
    print('list_po_of_postman:', list_po_of_postman)
    print('number_postman:', number_postman)
    print('number_po:', number_po)
    print('po_per_postman:', po_per_postman)

    len_po = len(parcel)

    # Xij - postman i works in post office j
    x = [[0 for i in range(len_po)] for i in range(number_postman + 1)]
    check_x = [[0 for i in range(len_po)] for i in range(number_postman + 1)]
    print(check_x)
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
        list_px[i] = list_sp[i] / parcel[i]


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


            print(s, parcel[j])
            print('list_px_%s' % j , list_px[j].solution_value())


    else:
        print('The problem does not have an optimal solution.')

solve()