#
# Q3

size = int(input("How many numbers: "))

maxm = 0
lst = []

for index in range(0, size):
    lst.append(int(input("number: ")))
    if lst[index] > maxm:
        maxm = lst[index]
print()

for j in range(maxm, 0, -1):
    print("{0:4d}".format(j), end=" "*4)

    for i in range(0, size):
        ch = " "
        if lst[i] >= j:
            ch = "*"
        print(ch, end="")
    print()

print("-"*4, "+", "-" * size)
