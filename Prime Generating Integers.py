def isprime(n):
    count = 0
    for num in range(1, n+1):
        if n % num == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False


output = 1
n = int(input("Input:\n"))

for number in range(2, n + 1):
    array = []
    for factor in range(1, number + 1):
        if number % factor == 0:
            array.append(factor)
    count = 0
    for f in array:
        if isprime(int(f + number / f)) is True:
            count += 1
    if count == len(array):
        output += number
print(output)
