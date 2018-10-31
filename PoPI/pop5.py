# Recursive Sum


def rec_sum(val):
    if val == 1:
        return 1
    else:
        previous_sum = rec_sum(val - 1)
        return val + previous_sum


X = int(input())
print(rec_sum(X))

# Exponentiation


def power(a, n):
    if n == 1:
        return a
    elif n == 0:
        return 1
    else:
        return a * power(a, n - 1)


A = float(input())
N = int(input())
print(power(A, N))

# Recursive Max


def max(index, lst):
    if index == len(lst) - 1:
        return lst[index]
    else:
        m_variable = max(index + 1, lst)
        if lst[index] > m_variable:
            return lst[index]
        else:
            return m_variable


lst = [int(X) for X in input().split(' ')]
print(max(0, lst))

# Reverse the sequence

lst = list([1])
while lst[-1] != 0:
    X = int(input())
    lst.append(X)
del lst[0]


def reversed_seq(index, seq):
    if len(seq) == 1:
        print(seq[0])
    else:
        print(seq[index * -1])
        if index + 1 <= len(seq):
            reversed_seq(index + 1, seq)


reversed_seq(1, lst)

# Print all Strings of given length containing 0 or 1


def print_01_string(k, s, n):
    if len(s) == n:
        print(s)
    else:
        print_01_string(k, s+'0', n)
        print_01_string(k, s+'1', n)


print_01_string(0, '', int(input()))
