F = int(input())
S = int(input())
L = int(input())
array = [F, S]
while L != 2:
    array.append(array[-1] + array[-2])
    L -= 1
array = list(map(str, array))
print(', '.join(array))
