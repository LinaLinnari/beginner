
def check_cords(x, y):
    moves = 8
    edgedX = False
    if x == 1 or x == 8:
        edgedX = True
        moves -= 3
    if y == 1 or y == 8:
        if edgedX:
            moves -= 2
        else:
            moves -= 3
    return moves


cordX = int(input('insert X >'))
cordY = int(input('insert Y >'))


print('King may move to ', check_cords(cordX, cordY), ' ways.')

