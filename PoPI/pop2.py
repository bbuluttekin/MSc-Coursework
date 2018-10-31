# List of squares

number = int(input())
nums = 1
while nums <= number:
    if nums ** 2 <= number:
        print(nums**2)
    nums += 1

# Least divisor

num = int(input())
num_list = []
div = 1
while div <= num:
    if (num % div == 0) and (div > 1):
        num_list.append(div)
    div += 1
print(min(num_list))

# The Power of Two

N = int(input())
num_list = []
div = 1
while div <= N:
    if 2**div <= N:
        num_list.append(div)
print(max(num_list), 2**max(num_list))

# Morning jog

X = int(input())
Y = int(input())
days = 1
while X < Y:
    X *= 1.1
    days += 1
print(days)

# The length of the sequence

N = None
lenght = 0
while N != 0:
    N = int(input())
    if N != 0:
        lenght += 1
print(lenght)

# The sum of the sequence

N = None
sum = 0
while N != 0:
    N = int(input())
    sum += N
print(sum)

# The average of the sequence

N = None
sum = 0
n_e = 0
while N != 0:
    N = int(input())
    if N == 0:
        break
    sum += N
    n_e += 1
print(sum / n_e)

# The maximum of the sequence

N = None
large = 0
while N != 0:
    N = int(input())
    if N > large:
        large = N
print(large)

# The index of the maximum of a sequence

N = None
index = 0
l_index = 0
large = 0
while N != 0:
    N = int(input())
    index += 1
    if N > large:
        large = N
        l_index = index
print(l_index)

# The number of even elements of the sequence

N = None
n_even = 0
while N != 0:
    N = int(input())
    if N == 0:
        break
    if N % 2 == 0:
        n_even += 1
print(n_even)

# The number of elements that are greater than the previous one

N = None
N_p = None
num_n = 0
while N != 0:
    N = int(input())
    if N_p != None:
        if N > N_p:
            num_n += 1
    N_p = N
print(num_n)

# The number of elements equal to the maximum

N = None
numbers = []
while N != 0:
    N = int(input())
    if N != 0:
        numbers.append(N)
num_lrg = 0
for i in numbers:
    if i == max(numbers):
        num_lrg += 1
print(num_lrg)

# Fibonacci numbers

fib = [0, 1]
index = 2
N = int(input())
while index <= N:
    fib.append(fib[-1] + fib[-2])
    index += 1
if N == 0:
    print(fib[0])
elif N == 1:
    print(fib[1])
else:
    print(fib[-1])

# The index of a Fibonacci number

N = int(input())
fib = [0, 1]
while fib[-1] < N:
    fib.append(fib[-1] + fib[-2])
if N in fib:
    print(fib.index(N))
else:
    print(-1)

# The maximum number of consecutive equal elements

N = None
N_p = None
st = 1
st_list = []
while N != 0:
    N = int(input())
    if N_p != None:
        if N == N_p:
            st += 1
        else:
            N_p = N
            st_list.append(st)
            st = 1
    else:
        N_p = N
print(max(st_list))

# Series - 1

A = int(input())
B = int(input())
for i in range(A, B+1):
    print(i)

# Series - 2

A = int(input())
B = int(input())
if A < B:
    for i in range(A, B+1):
        print(i)
elif A >= B:
    for i in range(A, B-1, -1):
        print(i)

# Sum of ten numbers

sum = 0
N = None
for i in range(1, 11):
    N = int(input())
    sum += N
print(sum)

# Sum of N numbers

N = int(input())
nums = None
sum = 0
for i in range(1, N+1):
    nums = int(input())
    sum += nums
print(sum)

# Factorial

product = 1
N = int(input())
for i in range(N, 0, -1):
    product *= i
print(product)

# The number of zeros

count = 0
N = int(input())
number = None
for i in range(1, N+1):
    number = int(input())
    if number == 0:
        count += 1
print(count)

# Adding factorials

N = int(input())
count = 0
for i in range(1, N + 1):
    if N >= 1:
        p_sum = 1
        for j in range(1, i + 1):
            p_sum *= j
        count += p_sum
print(count)

# Ladder

N = int(input())
for i in range(1, N + 1):
    print()
    for j in range(1, i + 1):
        print(j, end='')

# Lost card

N = int(input())
l_cards = list(range(1, N+1))
for i in range(1, N):
    C = int(input())
    l_cards.remove(C)

for i in l_cards:
    print(i)

# The length of the segment

X1 = float(input())
Y1 = float(input())
X2 = float(input())
Y2 = float(input())


def distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


print(distance(x1=X1, y1=Y1, x2=X2, y2=Y2))

# Negative exponent

A = float(input())
N = int(input())


def power(a, n):
    return a ** n


print(power(A, N))

# Uppercase

txt = input()


def capitalize(text):
    if ' ' in text:
        l_text = text.split(' ')
        for i in l_text:
            l_text[l_text.index(i)] = i[0].upper() + i[1:]
        return ' '.join(l_text)
    else:
        l_text = text[0].upper() + text[1:]
        return l_text


print(capitalize(txt))
