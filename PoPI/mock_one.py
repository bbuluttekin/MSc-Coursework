# Q1 a
def Fibonacci(n):
    numbers = [0, 1]
    while len(numbers) != n:
        new_num = numbers[-1] + numbers[-2]
        numbers.append(new_num)
    num_str = " ".join([str(i) for i in numbers])
    print(num_str)


# Q1 b

def fib2000(limit=2000):
    numbers = [0, 1]
    while numbers[-1] < 2000:
        new_num = numbers[-1] + numbers[-2]
        if new_num > 2000:
            break
        else:
            numbers.append(new_num)
    num_str = " ".join([str(i) for i in numbers])
    print(num_str)
    print("{} items printed".format(len(numbers)))


def search(search_str, lst, size):
    found = 0
    for i in lst:
        if search_str in i:
            found += 1
    if found == 0:
        return -1
    else:
        return found


if __name__ == "__main__":
    Fibonacci(20)
    fib2000()
    assert search("abb", ["xyz", "abc", "abbc", "abb"], 5) == 2
