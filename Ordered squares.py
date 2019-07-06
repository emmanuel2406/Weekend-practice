def ordSq(n):
    count1 = 0
    for index in range(len(str(n)) - 1):
        if str(n)[index] > str(n)[index + 1]:
            count1 = 1
    count2 = 0
    if int(n ** 0.5) == float(n ** 0.5):
        count2 = 1
    if count1 == 0 and count2 == 1:
        return True
    else:
        return False


array = []

V = int(input())
for num in range(1, V+1):
    if ordSq(num) is True:
        array.append(num)
array = list(map(str, array))
print(', '.join(array))
