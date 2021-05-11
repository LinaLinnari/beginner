
def check_cords(x, y):
    moves = 8
    edged_x = False
    if x == 1 or x == 8:
        edged_x = True
        moves -= 3
    if y == 1 or y == 8:
        if edged_x:
            moves -= 2
        else:
            moves -= 3
    return moves


cordX = int(input('insert X (1-8) >'))
cordY = int(input('insert Y (1-8) >'))


print('King may move to ', check_cords(cordX, cordY), ' ways.')

