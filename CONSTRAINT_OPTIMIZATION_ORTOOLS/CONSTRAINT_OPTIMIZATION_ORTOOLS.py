"""Simple solve."""
from ortools.sat.python import cp_model


# def main():
#     # Creates the model.
#     model = cp_model.CpModel()
#
#     # Creates the variables.
#     var_upper_bound = max(50, 45, 37)
#     x = model.NewIntVar(0, var_upper_bound, 'x')
#     y = model.NewIntVar(0, var_upper_bound, 'y')
#     z = model.NewIntVar(0, var_upper_bound, 'z')
#
#     s1 = 0
#     s1 += 2 * x
#     s1 += 7 * y
#     s1 += 3 * z + 1
#     s2 = 3 * x - 5 * y + 7 * z
#     s3 = 5 * x + 2 * y - 6 * z
#
#     # Creates the constraints.
#     model.Add(s1 <= 50)
#     model.Add(s2 <= 45)
#     model.Add(s3 <= 37)
#
#     t = model.NewIntVar(1, 100000, 't')
#
#     tmp = model.NewIntVar(1, 100000, 'tmp')     # <---- DM CHI NHAN DUOC 2 CAI NEN DUNG 2 VAR THOI
#
#
#     a = [x, 2 * y]
#     model.AddMultiplicationEquality(tmp, a)     # tmp = x * y
#
#     a = [tmp, x]
#     model.AddMultiplicationEquality(tmp, a)
#     a = [tmp, z]
#     model.AddMultiplicationEquality(t, a)       # c= tmp * z
#     print(t)
#     model.Add(t >= 10)
#     model.Maximize(t)
#
#     # Creates a model and solves the model.
#     solver = cp_model.CpSolver()
#     status = solver.Solve(model)
#
#     if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
#         print(f'Maximum of objective function: {solver.ObjectiveValue()}\n')
#         print(f'x = {solver.Value(x)}')
#         print(f'y = {solver.Value(y)}')
#         print(f'z = {solver.Value(z)}')
#     else:
#         print('No solution found.')
#
#     # Statistics.
#     print('\nStatistics')
#     print(f'  status   : {solver.StatusName(status)}')
#     print(f'  conflicts: {solver.NumConflicts()}')
#     print(f'  branches : {solver.NumBranches()}')
#     print(f'  wall time: {solver.WallTime()} s')
#
#
# if __name__ == '__main__':
#     main()

def read_data():
    f = open('../po_list.txt', 'r')

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

    model = cp_model.CpModel()

    len_po = len(parcel)

    # Xij - postman i works in post office j
    x = [[0 for i in range(len_po)] for i in range(number_postman + 1)]
    check_x = [[0 for i in range(len_po)] for i in range(number_postman + 1)]

    '''
        Declare variables
    '''

    for i in range(1, number_postman + 1):
        for j in list_po_of_postman[i]:
            x[i][j] = model.NewIntVar(0, number_postman, 'x%s%s' % (i, j))
            check_x[i][j] = 1

    # Objective variable
    obj = model.NewIntVar(0, 1000000, 'obj')

    # list of sum postman of post office, begin at index 1
    list_sp = [0] * (number_po + 1)

    # list of average parcel/postman of post office, begin at index 1
    list_px = [0] * (number_po + 1)

    # for i in range(1, number_po + 1):
    #     # list_sp[i] = model.NewIntVar(1, 999, 'list_sp%s' % (i))
    #     list_px[i] = model.NewIntVar(1, 100000000000, 'list_px%s' % (i))

    for i in range(1, number_po + 1):
        for j in range(1, number_postman + 1):
            if check_x[j][i] == 1:
                list_sp[i] += (1000000 // parcel[i]) * x[j][i]

    # for i in range(1, number_po + 1):
    #     a = list()
    #
    #     count = 0
    #     for j in range(1, number_po + 1):
    #         if j != i:
    #             if count < 2:
    #                 a.append(list_sp[j])
    #                 count += 1
    #             elif count == 2:
    #                 model.AddMultiplicationEquality(list_px[i], a)
    #                 count = 3
    #             else:
    #                 a = [list_px[i], list_sp[j]]
    #                 model.AddMultiplicationEquality(list_px[i], a)
    #     print('list_px%s' % i, list_px[i])



    '''
        Add constraints
    '''

    # Constraint: A postman only do at a post office
    for i in range(1, number_postman + 1):
        s = 0
        for j in range(1, number_po + 1):
            if check_x[i][j] == 1:
                s += x[i][j]
        model.Add(s == 1)

    for i in range(1, number_po + 1):
        for j in range(i + 1, number_po + 1):
            model.Add(obj >= list_sp[i] - list_sp[j])
            model.Add(obj >= list_sp[j] - list_sp[i])

    model.Minimize(obj)

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f'Minimum of objective function: {solver.ObjectiveValue()}\n')

    else:
        print('No solution found.')

    # Statistics.
    print('\nStatistics')
    print(f'  status   : {solver.StatusName(status)}')
    print(f'  conflicts: {solver.NumConflicts()}')
    print(f'  branches : {solver.NumBranches()}')
    print(f'  wall time: {solver.WallTime()} s')

solve()