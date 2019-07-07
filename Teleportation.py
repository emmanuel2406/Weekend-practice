no_of_buildings = int(input("Input the number of buildings\n"))
array =input().split(' ')
teleports = 1
height = array[0]
final = array[-1]
while array.index(height) != array.index(final):
    height = max(array[array.index(height)  + 1:])
    teleports += 1
    array = array.remove(array[:array.index(height) + 1])
print("The number of teleports is:", teleports)