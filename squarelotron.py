'''
    program: squarelotron.py
    author: Ding
    date: 06/09/2017
    Description: A squarelotron game. The program will ask you to start
    a 5X5 squarelotron, then tell it which flips to perform.
'''
import copy
def instruction():
    print("ui ---- up_down flip for inner ring")
    print("uo ---- up_down flip for outer ring")
    print("li ---- left_right flip for inner ring")
    print("lo ---- left_right flip for outer ring")
    print("ii ---- inverse_diagonal_flip for inner ring")
    print("lo ---- inverse_diagonal_flip for outer ring")
    print("mi ---- main_diagonal flip for inner ring")
    print("mo ---- main_diagonal flip for outer ring")
    print("r ---- restart the game")
    print("q ---- quit the game")


def make_squarelotron(list):
    print("Starting a 5X5 squarelotron game:")
    squarelotron = []
    for i in range(0, 5):
        squarelotron.append(list[(i * 5) : (i * 5) + 5])
    return squarelotron

def print_squarelotron(squarelotron):
    for i in range(0, 5):
        for j in range(0, 5):
            print('{:10}'.format(squarelotron[i][j]), end="")
        print('\n')
    return

def make_list(squarelotron):
    list = []
    row = len(squarelotron)
    col = len(squarelotron[1])
    for i in range(0, row):
        for j in range(0, col):
            list.append(squarelotron[i][j])
    return list

def upside_down_flip(squarelotron, ring):
    fliped_squarelotron = copy.deepcopy(squarelotron)
    if ring == 'o':
        flip_row = fliped_squarelotron[0]
        fliped_squarelotron[0] = fliped_squarelotron[len(squarelotron) - 1]
        fliped_squarelotron[len(squarelotron) - 1] = flip_row
    elif ring == 'i':
        flip_element = fliped_squarelotron[1][1:4]
        fliped_squarelotron[1][1:4] = fliped_squarelotron[3][1:4]
        fliped_squarelotron[3][1:4] = flip_element
    return fliped_squarelotron

def left_right_flip(squarelotron, ring):
    fliped_squarelotron = copy.deepcopy(squarelotron)
    if ring == 'o':
        for i in range(0, 5):
            fliped_squarelotron[i][0], fliped_squarelotron[i][4] = \
                                       fliped_squarelotron[i][4], fliped_squarelotron[i][0]

    elif ring == 'i':
        for i in range(1, 4):
            fliped_squarelotron[i][1], fliped_squarelotron[i][3] = \
                                       fliped_squarelotron[i][3], fliped_squarelotron[i][1]
            
    return fliped_squarelotron

def inverse_diagonal_flip(squarelotron, ring):
    fliped_squarelotron = copy.deepcopy(squarelotron)
    if ring == 'o':
        for i in range(0, 5):
            fliped_squarelotron[0][i], fliped_squarelotron[4 - i][4] = \
                                               fliped_squarelotron[4 - i][4], fliped_squarelotron[0][i]
        for i in range(1, 5):
            fliped_squarelotron[i][0], fliped_squarelotron[4][4 - i] = \
                                               fliped_squarelotron[4][4 - i], fliped_squarelotron[i][0]

    elif ring == 'i':
        for i in range(1, 4):
            fliped_squarelotron[1][i], fliped_squarelotron[4 - i][3] = \
                                               fliped_squarelotron[4 - i][3], fliped_squarelotron[1][i]
        for i in range(2, 4):
            fliped_squarelotron[i][1], fliped_squarelotron[3][4 - i] = \
                                               fliped_squarelotron[3][4 - i], fliped_squarelotron[i][1]


    return fliped_squarelotron

def main_diagonal_flip(squarelotron, ring):
    fliped_squarelotron = copy.deepcopy(squarelotron)
    if ring == 'o':
        for i in range(0, 5):
            fliped_squarelotron[0][i], fliped_squarelotron[i][0] = \
                                               fliped_squarelotron[i][0], fliped_squarelotron[0][i]
        for i in range(1, 5):
            fliped_squarelotron[4][i], fliped_squarelotron[i][4] = \
                                               fliped_squarelotron[i][4], fliped_squarelotron[4][i]
    elif ring == 'i':
        for i in range(1, 4):
            fliped_squarelotron[1][i], fliped_squarelotron[i][1] = \
                                               fliped_squarelotron[i][1], fliped_squarelotron[1][i]
        for i in range(2, 4):
            fliped_squarelotron[3][i], fliped_squarelotron[i][3] = \
                                               fliped_squarelotron[i][3], fliped_squarelotron[3][i]
    return fliped_squarelotron

def ini_squarelotron():
    squarelotron = make_squarelotron(list(range(1, 26)))
    print_squarelotron(squarelotron)
    return squarelotron

def play_squarelotron(squarelotron):
    action = input("How to flip next:?\n")
    print(action)
    while action[0] != 'q':
        if action[0] == 'u':
            if action[1] == 'i' or 'o':
                new_squarelotron = upside_down_flip(squarelotron, action[1])
                print_squarelotron(new_squarelotron)
            else:
                print("please input the correct action!")
                instruction()
        elif action[0] == 'l':
            if action[1] == 'i' or 'o':
                new_squarelotron = left_right_flip(squarelotron, action[1])
                print_squarelotron(new_squarelotron)
            else:
                print("please input the correct action!")
                instruction()
        elif action[0] == 'm':
            if action[1] == 'i' or 'o':
                new_squarelotron = main_diagonal_flip(squarelotron, action[1])
                print_squarelotron(new_squarelotron)
            else:
                print("please input the correct action!")
                instruction()
        elif action[0] == 'i':
            if action[1] == 'i' or 'o':
                new_squarelotron = inverse_diagonal_flip(squarelotron, action[1])
                print_squarelotron(new_squarelotron)
            else:
                print("please input the correct action!")
                instruction()
        elif action[0] == 'r':
            print("restart the game")
            ini_squarelotron()
        else:
            print("please input the correct action!")
            instruction()

        action = input("How to flip next:?\n")

    return

def main():
    instruction()
    squarelotron = ini_squarelotron()
    play_squarelotron(squarelotron)
    #print_squarelotron(squarelotron)
    #play_squareloctron(squarelotron)

if __name__== "__main__":
    main()
