# Matrix Maximum Index Function

nums = input().split()
m = int(nums[0])
n = int(nums[1])
M = list()
for i in range(0, m):
    current_row_strings = input().split()
    M.append([])
    for j in range(0, n):
        M[i].append(int(current_row_strings[j]))


def matrix_max_index(M, m, n):
    row_max = []
    for i in M:
        row_max.append(max(i))
    i_row = row_max.index(max(row_max))
    i_col = M[i_row].index(max(M[i_row]))
    return i_row, i_col


(i, j) = matrix_max_index(M, m, n)
print(i, j)

# Swap Columns Function


def swap_columns(M, m, n, i, j):
    for item in M:
        i_th = item[i]
        j_th = item[j]
        item[i] = j_th
        item[j] = i_th
    return M


nums = input().split()
m = int(nums[0])
n = int(nums[1])
M = list()
for i in range(0, m):
    current_row_strings = input().split()
    M.append([])
    for j in range(0, n):
        M[i].append(int(current_row_strings[j]))

nums = input().split()
i = int(nums[0])
j = int(nums[1])

swap_columns(M, m, n, i, j)

for i in range(0, m):
    for j in range(0, n):
        if j < n-1:
            print(M[i][j], end=' ')
        else:
            print(M[i][j], end='')
    if i < m-1:
        print()

# Matrix Scaling Function

import copy


def scale_matrix(M, m, n, c):
    n_M = copy.deepcopy(M)
    for index, item in enumerate(n_M):
        for i, e in enumerate(item):
            n_M[index][i] = e * c
    return n_M


def print_matrix(M, m, n):
    for i in range(0, m):
        for j in range(0, n):
            if j < n-1:
                print(M[i][j], end=' ')
            else:
                print(M[i][j], end='')
        if i < m-1:
            print()


nums = input().split()
m = int(nums[0])
n = int(nums[1])
M = list()
for i in range(0, m):
    current_row_strings = input().split()
    M.append([])
    for j in range(0, n):
        M[i].append(int(current_row_strings[j]))
c = int(input())

N = scale_matrix(M, m, n, c)
print_matrix(N, m, n)
print()
print_matrix(M, m, n)

# Multiplication of Two Matrices


def matrix_multiplication(A, B, m, n, r):
    C = [[0 for i in range(r)] for j in range(m)]
    for i in range(m):
        for j in range(r):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return(C)


def read_matrix(m, n):
    M = list()
    for i in range(0, m):
        current_row_strings = input().split()
        M.append([])
        for j in range(0, n):
            M[i].append(int(current_row_strings[j]))
    return M


nums = input().split()
m = int(nums[0])
n = int(nums[1])
r = int(nums[2])
A = read_matrix(m, n)
B = read_matrix(n, r)

C = matrix_multiplication(A, B, m, n, r)

for i in range(0, m):
    for j in range(0, r):
        if j < r-1:
            print(C[i][j], end=' ')
        else:
            print(C[i][j], end='')
            if i < m-1:
                print()
