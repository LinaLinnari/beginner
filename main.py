def cords():
    if x == 0 and y == 0:
        print("It's the origin!")
    elif (x == 0 or y == 0) and x != y:
        print("One of the coordinates is equal to zero!")
    else:
        if x >= 0 and y >= 0:
            print('I')
        if x <= 0 and y <= 0:
            print('III')
        if x >= 0 and 0 >= y:
            print('IV')
        if x <= 0 and 0 <= y:
            print('II')


x = float(input())
y = float(input())
cords()



