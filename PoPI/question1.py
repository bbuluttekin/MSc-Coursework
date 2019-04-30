def number_of_above_averages(n, m, A):
    '''implement the function'''
    number_of_elements = n * m
    total = 0
    for i in A:
        for j in i:
            total += j
    average = float(total) / number_of_elements
    result = 0
    for i in range(n):
        for j in range(m):
            if A[i][j] > average:
                result += 1
    return result
