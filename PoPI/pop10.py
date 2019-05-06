# List of combined pairs

import sys
X = sorted([int(x) for x in input().split(' ')])
Y = sorted([int(x) for x in input().split(' ')])

t = [(x, y) for x in X for y in Y if x < y]

for i, j in t:
    print(i, j)

# Squared Mapping

X = [int(x) for x in input().split()]
Y = [int(x) for x in input().split()]


def sqr(x):
    return x*x


it = zip((sqr(x) for x in X), Y)
for x in it:
    print(x[0], x[1])

# Matrix Comprehension


def create_matrix(m, n):
    M = [[i+j for i in range(n)] for j in range(m)]
    return M


# NO modifications below this line
inp = input().split()
m, n = int(inp[0]), int(inp[1])
M = create_matrix(m, n)
print(M)

# Higher Order Functions


def stringify(f):
    # implement this higher order function
    def func(s):
        new_str = ''
        for item in s:
            new_str += f(item)
        return new_str
    return func


# NO changes below this line
s = input()
complete_in = sys.stdin.read()
exec(complete_in)
F = stringify(f)
print(F(s))
