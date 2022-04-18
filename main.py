import random

game = True
bot_player=False
p1 = True
p2 = True
position = 0
list = 0
column_list=["A", "B", "C"]
row_list=["1", "2", "3"]

player_1_symbol = "X"
player_2_symbol = "O"

list_1 = []
list_2 = []
list_3 = []
all_lists = []


def restart():
    global list_1, list_2, list_3

    list_1 = ["", "_", "_", "_"]
    list_2 = ["", "_", "_", "_"]
    list_3 = ["", "_", "_", "_"]


def update_default():
    global all_lists
    all_lists = [list_1, list_2, list_3]
    return f"""
     |A|B|C
    1|{list_1[1]}|{list_1[2]}|{list_1[3]} 
    2|{list_2[1]}|{list_2[2]}|{list_2[3]} 
    3|{list_3[1]}|{list_3[2]}|{list_3[3]} 
    """


def correct_format():
    print("Please write your move in the correct format, e.g. 'B2'.")
    print(update_default())


def occupied(position, list):
    for _ in range(1, 4):
        if list == _:
            if all_lists[_-1][position] != "_":
                print("Place already occupied, state your move again.")
                print(update_default())
                return True


def sum_list():
    global game
    sum = 0
    for list in all_lists:
        sum += list.count("X")
        sum += list.count("O")
    if sum == 9:
        game = False
        print("Game over. Nobody won.")


def play_again():
    global game
    again = input("Do you want to play again? Type 'y' for yes and 'n' for no: ").lower()
    if again == "y":
        game = True
        restart()
        print(update_default())


def check_position(answer):
    global position

    if answer == "A":
        position = 1
    elif answer == "B":
        position = 2
    elif answer == "C":
        position = 3


def count_score(player_symbol, player_name):

    def player_won(player_name):
        global game
        game = False
        print(f"{player_name} won!")

    # columns:
    for _ in range (1, 4):
        if list_1[_] == player_symbol and list_2[_] == player_symbol and list_3[_] == player_symbol:
            player_won(player_name)

    # rows:
    for item in all_lists:
        if item[1] == player_symbol and item[2] == player_symbol and item[3] == player_symbol:
            player_won(player_name)

    # crosses:
    if list_1[1] == player_symbol and list_2[2] == player_symbol and list_3[3] == player_symbol:
        player_won(player_name)
    elif list_1[3] == player_symbol and list_2[2] == player_symbol and list_3[1] == player_symbol:
        player_won(player_name)


# Game:

print("\nWelcome to the Tic Tac Toe Game!")
print("This game is for 2 players. Player one uses 'X' and the other has 'O'.")
print("The goal is to have 3 same symbols next to each other. The cross also counts.")
input("Type 'enter' to continue: ")

print("First write letter of the column and then number of the line, e.g. 'B2'.")
input("Type 'enter' to start: ")

restart()
player_1_name = input("What's your name? ")
human_or_pc = input("Would you like to play against a 'computer' or against a 'human'? ").lower()

if human_or_pc== "computer":
    bot_player=True
    player_2_name="Computer"
else:
    player_2_name = input("What's tha name of the second player? ")

print(f"{player_1_name} starts.")
print(update_default())

# Game with two humans:
if not bot_player:
    while game:

        # PLAYER 1 move:

        p1 = True
        if p2:

            answer_p1 = input(f"{player_1_name}, what is your move? ").upper()
            # check the position of the letter:
            check_position(answer_p1[0])
            if answer_p1[0] not in column_list:
                correct_format()
                p1 = False

            if p1:
                # update the list:
                if answer_p1[1] == "1":
                    list = 1
                    if occupied(position=position, list=list):
                        p1 = False
                    else:
                        list_1[position] = "X"
                        print(update_default())

                elif answer_p1[1] == "2":
                    list = 2
                    if occupied(position=position, list=list):
                        p1 = False
                    else:
                        list_2[position] = "X"
                        print(update_default())
                elif answer_p1[1] == "3":
                    list = 3
                    if occupied(position=position, list=list):
                        p1 = False
                    else:
                        list_3[position] = "X"
                        print(update_default())
                else:
                    correct_format()
                    p1 = False

                count_score(player_1_symbol, player_1_name)
                if game:
                    sum_list()

        # PLAYER 2 move:

        if game:
            p2 = True
            if p1:
                answer_p2 = input(f"{player_2_name}, what is your move? ").upper()

                # check the position of the letter:
                check_position(answer_p2[0])
                if answer_p2[0] not in column_list:
                    correct_format()
                    p2 = False

                if p2:
                    # update the list:
                    if answer_p2[1] == "1":
                        list = 1
                        if occupied(position=position, list=list):
                            p2 = False
                        else:
                            list_1[position] = "O"
                            print(update_default())

                    elif answer_p2[1] == "2":
                        list = 2

                        if occupied(position=position, list=list):
                            p2 = False
                        else:
                            list_2[position] = "O"
                            print(update_default())
                    elif answer_p2[1] == "3":
                        list = 3
                        if occupied(position=position, list=list):
                            p2 = False
                        else:
                            list_3[position] = "O"
                            print(update_default())
                    else:
                        correct_format()
                        p2 = False

                    count_score(player_2_symbol, player_2_name)

                    if game:
                        sum_list()
        if not game:
            play_again()

# Game with a Computer:
if bot_player:
    while game:

        # PLAYER 1 move:

        p1 = True
        if p2:

            answer_p1 = input(f"{player_1_name}, what is your move? ").upper()
            # check the position of the letter:
            check_position(answer_p1[0])
            if answer_p1[0] not in column_list:
                correct_format()
                p1 = False

            if p1:
                # update the list:
                if answer_p1[1] == "1":
                    list = 1
                    if occupied(position=position, list=list):
                        p1 = False
                    else:
                        list_1[position] = "X"
                        print(update_default())

                elif answer_p1[1] == "2":
                    list = 2
                    if occupied(position=position, list=list):
                        p1 = False
                    else:
                        list_2[position] = "X"
                        print(update_default())
                elif answer_p1[1] == "3":
                    list = 3
                    if occupied(position=position, list=list):
                        p1 = False
                    else:
                        list_3[position] = "X"
                        print(update_default())
                else:
                    correct_format()
                    p1 = False

                count_score(player_1_symbol, player_1_name)
                if game:
                    sum_list()

        # PLAYER 2 move:

        if game:
            p2 = True
            if p1:
                answer_p2 = random.choice(column_list) + random.choice(row_list)
                print(f"Computer's move: {answer_p2}")

                # check the position of the letter:
                check_position(answer_p2[0])
                if answer_p2[0] not in column_list:
                    correct_format()
                    p2 = False

                if p2:
                    # update the list:
                    if answer_p2[1] == "1":
                        list = 1
                        if occupied(position=position, list=list):
                            p2 = False
                        else:
                            list_1[position] = "O"
                            print(update_default())

                    elif answer_p2[1] == "2":
                        list = 2

                        if occupied(position=position, list=list):
                            p2 = False
                        else:
                            list_2[position] = "O"
                            print(update_default())
                    elif answer_p2[1] == "3":
                        list = 3
                        if occupied(position=position, list=list):
                            p2 = False
                        else:
                            list_3[position] = "O"
                            print(update_default())
                    else:
                        correct_format()
                        p2 = False

                    count_score(player_2_symbol, player_2_name)

                    if game:
                        sum_list()
        if not game:
            play_again()