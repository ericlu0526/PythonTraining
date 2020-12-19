x1= 1
def test():
    x1= 2
test()
print(x1)


x2= 1
def test():
    global x2
    x2 = 2
test()
print(x2)


x3 = [1]
def test():
    x3 = [2]
test()
print(x3)


x4 = [1]
def test():
    global x4
    x4 = [2]
test()
print(x4)


x5 = [1]
def test():
    x5[0] = 2
test()
print(x5)


game = "I want to play a game"
print(id(game))


def game_board():

    global game
    print(id(game))
    game = "A game"
    print(id(game))
    return game


game_board()
print(id(game))
print(game)