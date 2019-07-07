rc = input("How many rows and columns are there:\n")
rows = int(rc.split(' ')[0])
columns = int(rc.split(' ')[1])
grid = []
while rows != 0:
    grid.append(input())
    rows -= 1
lightslit = 0
innocence = 0     
light_coordinates = []

for row in grid:
    if 'S' in row:
        xcoordinate = row.find('S')
        ycoordinate = grid.index(row)
    for char in row:
        if char == '*':
            light_coordinates.append((row.find(char) , grid.index(row)))
            index = grid.index(row)
            grid.remove(row)
            if row.index(char) == 0:
                row = 'o' + row[1:]
            else:
                row = row[:row.find(char) - 1] + 'o' + row[row.find(char):]
            grid = grid[:index] + [row] + grid[index:]
while innocence == 0:
    if light_coordinates == []:
        innocence = 1
    distances = []
    for pair in light_coordinates:
        distances.append(abs(pair[0] - xcoordinate) + abs(pair[1] - ycoordinate))
    if xcoordinate == light_coordinates[distances.index(min(distances))][0] or ycoordinate == light_coordinates[distances.index(min(distances))][1]:
        check = lightslit
        if min(distances) - 1 <= 2:
            lightslit += 1
        if check == lightslit:
            innocence = 1
        
    else:
        check = lightslit
        if min(distances) -2 <= 2:
            lightslit += 1
        if check == lightslit:
            innocence = 1
    xcoordinate = light_coordinates[distances.index(min(distances))][0]
    ycoordinate = light_coordinates[distances.index(min(distances))][1]
    light_coordinates = light_coordinates.remove(light_coordinates[distances.index(min(distances))])   
print("I can switch on", str(lightslit) , "lightswitches")
