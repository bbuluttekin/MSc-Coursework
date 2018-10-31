# Even indices

my_list = input()
my_list = my_list.split(' ')
for item in range(len(my_list)):
    if item % 2 == 0:
        print(my_list[item])

# Even elements

my_list = input()
my_list = my_list.split(' ')
for item in my_list:
    if int(item) % 2 == 0:
        print(item)

# Greater than previous

my_list = input()
my_list = my_list.split(' ')
for item in range(len(my_list)):
    if item != 0:
        if int(my_list[item]) > int(my_list[(item - 1)]):
            print(my_list[item])

# Neighbors of the same sign

my_list = input()
my_list = my_list.split(' ')
for item in range(len(my_list) - 1):
    if (int(my_list[item]) > 0) and (int(my_list[item + 1]) > 0):
        print(my_list[item], my_list[item + 1])
        break
    elif (int(my_list[item]) < 0) and (int(my_list[item + 1]) < 0):
        print(my_list[item], my_list[item + 1])
        break
    else:
        print()

# Greater than neighbours

my_list = input()
my_list = my_list.split(' ')
i_list = 0
for i in range(len(my_list)):
    if i != 0 and i != (len(my_list) - 1):
        c_1 = int(my_list[i - 1]) < int(my_list[i])
        c_2 = int(my_list[i]) > int(my_list[i + 1])
        if c_1 and c_2:
            i_list += 1
print(i_list)

# The largest element

my_list = input()
my_list = my_list.split(' ')
i_list = []
for i in my_list:
    i_list.append(int(i))
print(max(i_list), i_list.index(max(i_list)))

# The number of distinct elements

my_list = input()
my_list = my_list.split(' ')
i_list = []
for item in my_list:
    i_list.append(int(item))
print(len(set(i_list)))

# Swap neighbours

my_list = input()
my_list = [int(i) for i in my_list.split(' ')]
for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
for item in my_list:
    print(item)

# Swap min and max

my_list = input()
my_list = my_list.split(' ')
i_list = []
for item in my_list:
    i_list.append(int(item))
i_max = i_list.index(max(i_list))
i_min = i_list.index(min(i_list))
my_list[i_max] = str(min(i_list))
my_list[i_min] = str(max(i_list))
for item in my_list:
    print(item)

# The number of pairs of equal

L = [int(x) for x in input().split(' ')]
c = 0
for i in range(len(L)):
    for j in range(i + 1, len(L)):
        if L[i] == L[j]:
            c += 1
print(c)

# Unique elements

my_list = input()
my_list = my_list.split(' ')
for i in range(len(my_list)):
    if my_list[i] in my_list[i + 1:] or my_list[i] in my_list[:i]:
        continue
    else:
        print(my_list[i])

# Queens

A = 8
x = []
y = []
for item in range(A):
    x_l, y_l = [int(i) for i in input().split(' ')]
    x.append(x_l)
    y.append(y_l)
status = True
for i in range(A):
    for j in range(i + 1, A):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            status = False
if status:
    print('NO')
else:
    print('YES')

# The bowling alley

N, K = [int(x) for x in input().split()]
C = ["I"] * N
for item in range(K):
    l, r = [int(x) for x in input().split()]
    for i in range(l - 1, r):
        C[i] = '.'
print(''.join(C))

# Slices

c_str = input()
print(c_str[2])
print(c_str[-2])
print(c_str[:5])
print(c_str[:-2])
print(c_str[::2])
print(c_str[1::2])
print(c_str[::-1])
print(c_str[::-2])
print(len(c_str))

# The number of words

S = input()
print(S.count(" ") + 1)

# The first and last occurrence

S = input()
if S.count('f') == 1:
    print(S.find("f"))
elif S.count("f") >= 2:
    print(S.find("f"), S.rfind("f"))

# Reverse the fragment

S = input()
H = S[:S.find("h")]
H_i = S[S.find("h"):S.rfind("h") + 1]
H_ii = S[S.rfind("h") + 1:]
S = H + H_i[::-1] + H_ii
print(S)

# Replace within the fragment

S = input()
S_i = S[:S.find('h') + 1]
S_ii = S[S.find('h') + 1:S.rfind('h')]
S_iii = S[S.rfind('h'):]
S = S_i + S_ii.replace('h', 'H') + S_iii
print(S)

# Delete every third character

S = input()
x = ''
for item in range(len(S)):
    if item % 3 != 0:
        x = x + S[item]
print(x)

# The number of distinct numbers

S = set([int(x) for x in input().split()])
print(len(S))

# The number of equal numbers

print(len(set(input().split()).intersection(set(input().split()))))

# The intersection of sets

S = set(input().split()).intersection(set(input().split()))
o_l = [int(x) for x in S]
for i in sorted(o_l):
    print(i)

# Cubes

N, M = [int(x) for x in input().split()]
al = set()
bob = set()
for i in range(N):
    al.add(int(input()))
for i in range(M):
    bob.add(int(input()))

print(len(al & bob))
print(*[str(x) for x in sorted(al & bob)])
print(len(al - bob))
print(*[str(x) for x in sorted(al - bob)])
print(len(bob - al))
print(*[str(x) for x in sorted(bob - al)])

# Guess the number

N = int(input())
numbers = set(range(1, N + 1))
p = numbers
while True:
    g = input()
    if g == "HELP":
        break
    g = {int(x) for x in g.split()}
    a = input()
    if a == "YES":
        p &= g
    else:
        p &= numbers - g
print(" ".join([str(x) for x in sorted(p)]))

# Polyglots

S = [{input() for i in range(int(input()))} for x in range(int(input()))]
ke, ks = set.intersection(*S), set.union(*S)
print(len(ke), *sorted(ke), sep='\n')
print(len(ks), *sorted(ks), sep='\n')

# Number of occurrences

c = {}
for w in input().split():
    c[w] = c.get(w, 0) + 1
    print(c[w] - 1, end=' ')

# Dictionary of synonyms

number = int(input())
d = {}
for x in range(number):
    f, s = input().split()
    d[f] = s
    d[s] = f
print(d[input()])

# Access rights

p = {'read': 'R', 'write': 'W', 'execute': 'X'}
fp = {}
for x in range(int(input())):
    fi, *pe = input().split()
    fp[fi] = set(pe)
for item in range(int(input())):
    o, fi = input().split()
    if p[o] in fp[fi]:
        print('OK')
    else:
        print('Access denied')

# Frequency analysis

from collections import Counter
w = []
for x in range(int(input())):
    w.extend(input().split())

c = Counter(w)
p = [(-x[1], x[0]) for x in c.most_common()]
w = [i[1] for i in sorted(p)]
print('\n'.join(w))

# English-Latin dictionary

from collections import defaultdict
le = defaultdict(list)
for x in range(int(input())):
    ew, ltc = input().split(' - ')
    lt = ltc.split(', ')
    for i in lt:
        le[i].append(ew)
print(len(le))
for i, j in sorted(le.items()):
    print(i + ' - ' + ', '.join(j))
