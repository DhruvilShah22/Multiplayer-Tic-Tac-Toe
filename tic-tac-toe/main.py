def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


row1 = ['1', '2', '3']
row2 = ['4', '5', '6']
row3 = ['7', '8', '9']

want_to_play = 0
row1

def player1():
    option = int(input("Enter the location you want to place your marker player 1"))
    while option > 9:
        option = int(input("Enter the location you want to place your marker player 1"))

    if option < 4:
        row1[option - 1] = 'X'
    if 7 > option > 3:
        row2[option - 4] = 'X'
    if 10 > option > 6:
        row3[option - 7] = 'X'

    display(row1, row2, row3)

    if row1[0] == 'X' and row1[1]  == 'X'and row1[2] == 'X':
        print("player 1 won")
        exit()

    elif row2[0] == 'X' and row2[1] == 'X' and row2[2] == 'X':
        print("player 1 won")
        exit()

    elif row1[1] == 'X' and row2[1] == 'X' and row1[1] == 'X':
        print("player 1 won")
        exit()

    elif row1[0] == 'X' and row2[0] == 'X' and row1[0] == 'X':
        print("player 1 won")
        exit()

    elif row3[0] == 'X' and row3[1] == 'X' and row3[2] == 'X':
        print("player 1 won")
        exit()

    elif row3[0] == 'X' and row2[1] == 'X' and row1[2] == 'X':
        print("player 1 won")
        exit()

    elif row1[0] == 'X' and row2[1] == 'X' and row3[2] == 'X':
        print("player 1 won")
        exit()

    elif row1[2] == 'X' and row2[2] == 'X' and row1[2] == 'X':
        print("player 1 won")
        exit()
    else:
        pass

def player2():
    option = int(input("Enter the location you want to place your marker player 2"))

    while option > 9:
        option = int(input("Enter the location you want to place your marker player 2"))

    if option < 4:
        row1[option - 1] = 'O'
    if 7 > option > 3:
        row2[option - 4] = 'O'
    if 10 > option > 6:
        row3[option - 7] = 'O'

    display(row1, row2, row3)

    if row1[0]== 'O' and row1[1]== 'O' and row1[2] == 'O':
        print("player 2 won")
        exit()

    elif row2[0]== 'O' and row2[1]== 'O' and row2[2] == '0':
        print("player 2 won")
        exit()

    elif row3[0]== 'O' and row3[1]== 'O' and row3[2] == 'O':
        print("player 2 won")
        exit()

    elif row1[0] == 'O'and row2[1]== 'O' and row3[2] == 'O':
        print("player 2 won")
        exit()

    elif row3[0] == 'O'and row2[1] == 'O'and row1[2] == 'O':
        print("player 2 won")
        exit()

    elif row1[0] == 'O'and row2[0] == 'O'and row1[0] == 'O':
        print("player 2 won")
        exit()

    elif row1[1]== 'O' and row2[1] == 'O'and row1[1] == 'O':
        print("player 2 won")
        exit()

    elif row1[2]== 'O' and row2[2] == 'O'and row1[2] == 'O':
        print("player 2 won")
        exit()
    else:
        pass


display(row1, row2, row3)
while want_to_play != 1:
    player1()
    player2()