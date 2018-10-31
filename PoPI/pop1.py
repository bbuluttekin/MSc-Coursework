# Sum of three numbers
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

# Area of right-angled triangle

b = int(input())
h = int(input())
print(b * h / 2)

# Apple sharing

n = int(input())
k = int(input())
print(k // n)
print(k % n)

# Hello, Harry!

name = input()
print('Hello, {}!'.format(name))

# Previous and next

num = int(input())
print('The next number for the number {} is {}'.format(num, num + 1))
print('The previous number for the number {} is {}'.format(num, num - 1))

# School desks

class_1 = int(input())
class_2 = int(input())
class_3 = int(input())
print((class_1 // 2) + (class_1 % 2) + (class_2 // 2) +
      (class_2 % 2) + (class_3 // 2) + (class_3 % 2))

# Last digit of integer

num = input()
print(num[-1])

# Tens digit

num = int(input())
print((num % 100) // 10)

# Sum of digits

num = input()
print(int(num[0]) + int(num[1]) + int(num[2]))

# Fractional part

num = float(input())
print(num - int(num))

# First digit after decimal point

num = float(input())
print(int((((num - int(num)) * 100) - (((num - int(num)) * 100) % 10)) // 10))

# Car route

n = int(input())
m = int(input())
print((m // n) + (m % n != 0))

# Digital Clock

n = int(input())
print(n // 60, n % 60)

# Total Cost

A = int(input())
B = int(input())
N = int(input())
print((A * N + (B * N) // 100), (B * N) % 100)

# Clock Face-1

h = int(input())
m = int(input())
s = int(input())
print(30 * h + 30 / 60 * m + 30 / 3600 * s)

# Clock Face-2

A = float(input())
print(A % 30 * 12)

# Minimum of two numbers

num_1 = int(input())
num_2 = int(input())
print(min(num_1, num_2))

# Sign function

int_x = int(input())
if int_x > 0:
    print(1)
elif int_x < 0:
    print(-1)
else:
    print(0)

# Minimum of three numbers

n_1 = int(input())
n_2 = int(input())
n_3 = int(input())
if n_2 >= n_1 <= n_3:
    print(n_1)
elif n_1 >= n_2 <= n_3:
    print(n_2)
else:
    print(n_3)

# Leap year

year = int(input())
if (year % 4 == 0) and (year % 100 != 0):
    print("LEAP")
elif year % 400 == 0:
    print("LEAP")
else:
    print("COMMON")

# Equal numbers

a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print(3)
elif (a != b) and (b != c) and (a != c):
    print(0)
else:
    print(2)

# Rook move

st_1 = int(input())
st_2 = int(input())
mv_1 = int(input())
mv_2 = int(input())
if (st_1 == mv_1) or (st_2 == mv_2):
    print('YES')
else:
    print('NO')

# Chess board

st_1 = int(input())
st_2 = int(input())
mv_1 = int(input())
mv_2 = int(input())
if (st_1 + st_2 + mv_1 + mv_2) % 2 == 0:
    print('YES')
else:
    print('NO')

# King move

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
    print('YES')
else:
    print('NO')

# Bishop moves

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2):
    print('YES')
else:
    print('NO')

# Queen move

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')

# Knight move

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
dx = abs(x1 - x2)
dy = abs(y1 - y2)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('YES')
else:
    print('NO')

# Chocolate bar

n = int(input())
m = int(input())
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')
