board = [["_", "_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_", "_"],
         ["_", "_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_", "_"],
         ["1", "2", "3", "4", "5", "6", "7"]]

player1_wins = 0
player2_wins = 0
play_again = " "
x_cnt = 0
y_cnt = 0
player1 = input("Player1: ")
player2 = input("Player2: ")


def display_board():
    for rows in board:
        for columns in rows:
            print(columns, end=" ")
        print()


while play_again.upper() != "N":
    display_board()
    cnt = 0
    available_one = 5
    available_two = 5
    available_tree = 5
    available_four = 5
    available_five = 5
    available_six = 5
    available_seven = 5
    while True:
        if (player1_wins + player2_wins) % 2 == 0:
            while True:
                player1_move = int(input(f"{player1}: "))
                if player1_move == 1:
                    if available_one < 0:
                        print("Can't place it there")
                        display_board()
                        pass
                    else:
                        board[available_one][player1_move-1] = "X"
                        available_one -= 1
                        display_board()
                        break
                elif player1_move == 2:
                    if available_two < 0:
                        print("Can't place it there")
                        display_board()
                        pass
                    else:
                        board[available_two][player1_move-1] = "X"
                        available_two -= 1
                        display_board()
                        break
                elif player1_move == 3:
                    if available_tree < 0:
                        print("Can't place it there")
                        display_board()
                        pass
                    else:
                        board[available_tree][player1_move-1] = "X"
                        available_tree -= 1
                        display_board()
                        break
                elif player1_move == 4:
                    if available_four < 0:
                        print("Can't place it there")
                        display_board()
                        pass
                    else:
                        board[available_four][player1_move-1] = "X"
                        available_four -= 1
                        display_board()
                        break
                elif player1_move == 5:
                    if available_five < 0:
                        print("Can't place it there")
                        display_board()
                        pass
                    else:
                        board[available_five][player1_move-1] = "X"
                        available_five -= 1
                        display_board()
                        break
                elif player1_move == 6:
                    if available_six < 0:
                        print("Can't place it there")
                        display_board()
                        pass
                    else:
                        board[available_six][player1_move-1] = "X"
                        available_six -= 1
                        display_board()
                        break
                elif player1_move == 7:
                    if available_seven < 0:
                        print("Can't place it there")
                        display_board()
                        pass
                    else:
                        board[available_seven][player1_move-1] = "X"
                        available_seven -= 1
                        display_board()
                        break
                else:
                    print("Wrong input")
                    pass
            if ((board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X" and board[0][3] == "X") or
                    (board[0][1] == "X" and board[0][2] == "X" and board[0][3] == "X" and board[0][4] == "X") or
                    (board[0][2] == "X" and board[0][3] == "X" and board[0][4] == "X" and board[0][5] == "X") or
                    (board[0][3] == "X" and board[0][4] == "X" and board[0][5] == "X" and board[0][6] == "X") or
                    (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X" and board[1][3] == "X") or
                    (board[1][1] == "X" and board[1][2] == "X" and board[1][3] == "X" and board[1][4] == "X") or
                    (board[1][2] == "X" and board[1][3] == "X" and board[1][4] == "X" and board[1][5] == "X") or
                    (board[1][3] == "X" and board[1][4] == "X" and board[1][5] == "X" and board[1][6] == "X") or
                    (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X" and board[2][3] == "X") or
                    (board[2][1] == "X" and board[2][2] == "X" and board[2][3] == "X" and board[2][4] == "X") or
                    (board[2][2] == "X" and board[2][3] == "X" and board[2][4] == "X" and board[2][5] == "X") or
                    (board[2][3] == "X" and board[2][4] == "X" and board[2][5] == "X" and board[2][6] == "X") or
                    (board[3][0] == "X" and board[3][1] == "X" and board[3][2] == "X" and board[3][3] == "X") or
                    (board[3][1] == "X" and board[3][2] == "X" and board[3][3] == "X" and board[3][4] == "X") or
                    (board[3][2] == "X" and board[3][3] == "X" and board[3][4] == "X" and board[3][5] == "X") or
                    (board[3][3] == "X" and board[3][4] == "X" and board[3][5] == "X" and board[3][6] == "X") or
                    (board[4][0] == "X" and board[4][1] == "X" and board[4][2] == "X" and board[4][3] == "X") or
                    (board[4][1] == "X" and board[4][2] == "X" and board[4][3] == "X" and board[4][4] == "X") or
                    (board[4][2] == "X" and board[4][3] == "X" and board[4][4] == "X" and board[4][5] == "X") or
                    (board[4][3] == "X" and board[4][4] == "X" and board[4][5] == "X" and board[4][6] == "X") or
                    (board[5][0] == "X" and board[5][1] == "X" and board[5][2] == "X" and board[5][3] == "X") or
                    (board[5][1] == "X" and board[5][2] == "X" and board[5][3] == "X" and board[5][4] == "X") or
                    (board[5][2] == "X" and board[5][3] == "X" and board[5][4] == "X" and board[5][5] == "X") or
                    (board[5][3] == "X" and board[5][4] == "X" and board[5][5] == "X" and board[5][6] == "X") or
                    (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X" and board[3][0] == "X") or
                    (board[1][0] == "X" and board[2][0] == "X" and board[3][0] == "X" and board[4][0] == "X") or
                    (board[2][0] == "X" and board[3][0] == "X" and board[4][0] == "X" and board[5][0] == "X") or
                    (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X" and board[3][1] == "X") or
                    (board[1][1] == "X" and board[2][1] == "X" and board[3][1] == "X" and board[4][1] == "X") or
                    (board[2][1] == "X" and board[3][1] == "X" and board[4][1] == "X" and board[5][1] == "X") or
                    (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X" and board[3][2] == "X") or
                    (board[1][2] == "X" and board[2][2] == "X" and board[3][2] == "X" and board[4][2] == "X") or
                    (board[2][2] == "X" and board[3][2] == "X" and board[4][2] == "X" and board[5][2] == "X") or
                    (board[0][3] == "X" and board[1][3] == "X" and board[2][3] == "X" and board[3][3] == "X") or
                    (board[1][3] == "X" and board[2][3] == "X" and board[3][3] == "X" and board[4][3] == "X") or
                    (board[2][3] == "X" and board[3][3] == "X" and board[4][3] == "X" and board[5][3] == "X") or
                    (board[0][4] == "X" and board[1][4] == "X" and board[2][4] == "X" and board[3][4] == "X") or
                    (board[1][4] == "X" and board[2][4] == "X" and board[3][4] == "X" and board[4][4] == "X") or
                    (board[2][4] == "X" and board[3][4] == "X" and board[4][4] == "X" and board[5][4] == "X") or
                    (board[0][5] == "X" and board[1][5] == "X" and board[2][5] == "X" and board[3][5] == "X") or
                    (board[1][5] == "X" and board[2][5] == "X" and board[3][5] == "X" and board[4][5] == "X") or
                    (board[2][5] == "X" and board[3][5] == "X" and board[4][5] == "X" and board[5][5] == "X") or
                    (board[0][6] == "X" and board[1][6] == "X" and board[2][6] == "X" and board[3][6] == "X") or
                    (board[1][6] == "X" and board[2][6] == "X" and board[3][6] == "X" and board[4][6] == "X") or
                    (board[2][6] == "X" and board[3][6] == "X" and board[4][6] == "X" and board[5][6] == "X") or
                    (board[5][3] == "X" and board[4][2] == "X" and board[3][1] == "X" and board[2][0] == "X") or
                    (board[5][4] == "X" and board[4][3] == "X" and board[3][2] == "X" and board[2][1] == "X") or
                    (board[1][0] == "X" and board[4][2] == "X" and board[3][1] == "X" and board[2][0] == "X") or
                    (board[5][5] == "X" and board[4][4] == "X" and board[3][3] == "X" and board[2][2] == "X") or
                    (board[1][1] == "X" and board[4][4] == "X" and board[3][3] == "X" and board[2][2] == "X") or
                    (board[1][1] == "X" and board[0][0] == "X" and board[3][3] == "X" and board[2][2] == "X") or
                    (board[5][6] == "X" and board[4][5] == "X" and board[3][4] == "X" and board[2][3] == "X") or
                    (board[1][2] == "X" and board[4][5] == "X" and board[3][4] == "X" and board[2][3] == "X") or
                    (board[1][2] == "X" and board[0][1] == "X" and board[3][4] == "X" and board[2][3] == "X") or
                    (board[4][6] == "X" and board[3][5] == "X" and board[2][4] == "X" and board[1][3] == "X") or
                    (board[0][2] == "X" and board[3][5] == "X" and board[2][4] == "X" and board[1][3] == "X") or
                    (board[3][6] == "X" and board[2][5] == "X" and board[1][4] == "X" and board[0][3] == "X") or
                    (board[5][3] == "X" and board[4][4] == "X" and board[3][5] == "X" and board[2][6] == "X") or
                    (board[5][2] == "X" and board[4][3] == "X" and board[3][4] == "X" and board[2][5] == "X") or
                    (board[1][6] == "X" and board[4][3] == "X" and board[3][4] == "X" and board[2][5] == "X") or
                    (board[5][1] == "X" and board[4][2] == "X" and board[3][3] == "X" and board[2][4] == "X") or
                    (board[1][5] == "X" and board[4][2] == "X" and board[3][3] == "X" and board[2][4] == "X") or
                    (board[1][5] == "X" and board[0][6] == "X" and board[3][3] == "X" and board[2][4] == "X") or
                    (board[5][0] == "X" and board[4][1] == "X" and board[3][2] == "X" and board[2][3] == "X") or
                    (board[1][4] == "X" and board[4][1] == "X" and board[3][2] == "X" and board[2][3] == "X") or
                    (board[1][4] == "X" and board[0][5] == "X" and board[3][2] == "X" and board[2][3] == "X") or
                    (board[4][0] == "X" and board[3][1] == "X" and board[2][2] == "X" and board[1][3] == "X") or
                    (board[0][4] == "X" and board[3][1] == "X" and board[2][2] == "X" and board[1][3] == "X") or
                    (board[3][0] == "X" and board[2][1] == "X" and board[1][2] == "X" and board[0][3] == "X")):
                print(f"{player1} WON")
                player1_wins += 1
                break
            for row in board:
                for col in row:
                    if col == "X" or col == "O":
                        cnt += 1
            if cnt == 881:
                print("TIE")
                break
            elif cnt != 881:
                pass
            # player2's turn
            while True:
                player2_move = int(input(f"{player2}: "))
                if player2_move == 1:
                    if available_one < 0:
                        print("Can't place it there")
                        display_board()
                        pass
                    else:
                        board[available_one][player2_move-1] = "O"
                        available_one -= 1
                        display_board()
                        break
                elif player2_move == 2:
                    if available_two < 0:
                        print("Can't place it there")
                        display_board()
                        pass
                    else:
                        board[available_two][player2_move-1] = "O"
                        available_two -= 1
                        display_board()
                        break
                elif player2_move == 3:
                    if available_tree < 0:
                        print("Can't place it there")
                        display_board()
                        pass
                    else:
                        board[available_tree][player2_move-1] = "O"
                        available_tree -= 1
                        display_board()
                        break
                elif player2_move == 4:
                    if available_four < 0:
                        print("Can't place it there")
                        display_board()
                        pass
                    else:
                        board[available_four][player2_move-1] = "O"
                        available_four -= 1
                        display_board()
                        break
                elif player2_move == 5:
                    if available_five < 0:
                        print("Can't place it there")
                        display_board()
                        pass
                    else:
                        board[available_five][player2_move-1] = "O"
                        available_five -= 1
                        display_board()
                        break
                elif player2_move == 6:
                    if available_six < 0:
                        print("Can't place it there")
                        display_board()
                        pass
                    else:
                        board[available_six][player2_move-1] = "O"
                        available_six -= 1
                        display_board()
                        break
                elif player2_move == 7:
                    if available_seven < 0:
                        print("Can't place it there")
                        display_board()
                        pass
                    else:
                        board[available_seven][player2_move-1] = "O"
                        available_seven -= 1
                        display_board()
                        break
                else:
                    print("Wrong input")
                    pass
            if ((board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O" and board[0][3] == "O") or
                    (board[0][1] == "O" and board[0][2] == "O" and board[0][3] == "O" and board[0][4] == "O") or
                    (board[0][2] == "O" and board[0][3] == "O" and board[0][4] == "O" and board[0][5] == "O") or
                    (board[0][3] == "O" and board[0][4] == "O" and board[0][5] == "O" and board[0][6] == "O") or
                    (board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O" and board[1][3] == "O") or
                    (board[1][1] == "O" and board[1][2] == "O" and board[1][3] == "O" and board[1][4] == "O") or
                    (board[1][2] == "O" and board[1][3] == "O" and board[1][4] == "O" and board[1][5] == "O") or
                    (board[1][3] == "O" and board[1][4] == "O" and board[1][5] == "O" and board[1][6] == "O") or
                    (board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O" and board[2][3] == "O") or
                    (board[2][1] == "O" and board[2][2] == "O" and board[2][3] == "O" and board[2][4] == "O") or
                    (board[2][2] == "O" and board[2][3] == "O" and board[2][4] == "O" and board[2][5] == "O") or
                    (board[2][3] == "O" and board[2][4] == "O" and board[2][5] == "O" and board[2][6] == "O") or
                    (board[3][0] == "O" and board[3][1] == "O" and board[3][2] == "O" and board[3][3] == "O") or
                    (board[3][1] == "O" and board[3][2] == "O" and board[3][3] == "O" and board[3][4] == "O") or
                    (board[3][2] == "O" and board[3][3] == "O" and board[3][4] == "O" and board[3][5] == "O") or
                    (board[3][3] == "O" and board[3][4] == "O" and board[3][5] == "O" and board[3][6] == "O") or
                    (board[4][0] == "O" and board[4][1] == "O" and board[4][2] == "O" and board[4][3] == "O") or
                    (board[4][1] == "O" and board[4][2] == "O" and board[4][3] == "O" and board[4][4] == "O") or
                    (board[4][2] == "O" and board[4][3] == "O" and board[4][4] == "O" and board[4][5] == "O") or
                    (board[4][3] == "O" and board[4][4] == "O" and board[4][5] == "O" and board[4][6] == "O") or
                    (board[5][0] == "O" and board[5][1] == "O" and board[5][2] == "O" and board[5][3] == "O") or
                    (board[5][1] == "O" and board[5][2] == "O" and board[5][3] == "O" and board[5][4] == "O") or
                    (board[5][2] == "O" and board[5][3] == "O" and board[5][4] == "O" and board[5][5] == "O") or
                    (board[5][3] == "O" and board[5][4] == "O" and board[5][5] == "O" and board[5][6] == "O") or
                    (board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O" and board[3][0] == "O") or
                    (board[1][0] == "O" and board[2][0] == "O" and board[3][0] == "O" and board[4][0] == "O") or
                    (board[2][0] == "O" and board[3][0] == "O" and board[4][0] == "O" and board[5][0] == "O") or
                    (board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O" and board[3][1] == "O") or
                    (board[1][1] == "O" and board[2][1] == "O" and board[3][1] == "O" and board[4][1] == "O") or
                    (board[2][1] == "O" and board[3][1] == "O" and board[4][1] == "O" and board[5][1] == "O") or
                    (board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O" and board[3][2] == "O") or
                    (board[1][2] == "O" and board[2][2] == "O" and board[3][2] == "O" and board[4][2] == "O") or
                    (board[2][2] == "O" and board[3][2] == "O" and board[4][2] == "O" and board[5][2] == "O") or
                    (board[0][3] == "O" and board[1][3] == "O" and board[2][3] == "O" and board[3][3] == "O") or
                    (board[1][3] == "O" and board[2][3] == "O" and board[3][3] == "O" and board[4][3] == "O") or
                    (board[2][3] == "O" and board[3][3] == "O" and board[4][3] == "O" and board[5][3] == "O") or
                    (board[0][4] == "O" and board[1][4] == "O" and board[2][4] == "O" and board[3][4] == "O") or
                    (board[1][4] == "O" and board[2][4] == "O" and board[3][4] == "O" and board[4][4] == "O") or
                    (board[2][4] == "O" and board[3][4] == "O" and board[4][4] == "O" and board[5][4] == "O") or
                    (board[0][5] == "O" and board[1][5] == "O" and board[2][5] == "O" and board[3][5] == "O") or
                    (board[1][5] == "O" and board[2][5] == "O" and board[3][5] == "O" and board[4][5] == "O") or
                    (board[2][5] == "O" and board[3][5] == "O" and board[4][5] == "O" and board[5][5] == "O") or
                    (board[0][6] == "O" and board[1][6] == "O" and board[2][6] == "O" and board[3][6] == "O") or
                    (board[1][6] == "O" and board[2][6] == "O" and board[3][6] == "O" and board[4][6] == "O") or
                    (board[2][6] == "O" and board[3][6] == "O" and board[4][6] == "O" and board[5][6] == "O") or
                    (board[5][3] == "O" and board[4][2] == "O" and board[3][1] == "O" and board[2][0] == "O") or
                    (board[5][4] == "O" and board[4][3] == "O" and board[3][2] == "O" and board[2][1] == "O") or
                    (board[1][0] == "O" and board[4][2] == "O" and board[3][1] == "O" and board[2][0] == "O") or
                    (board[5][5] == "O" and board[4][4] == "O" and board[3][3] == "O" and board[2][2] == "O") or
                    (board[1][1] == "O" and board[4][4] == "O" and board[3][3] == "O" and board[2][2] == "O") or
                    (board[1][1] == "O" and board[0][0] == "O" and board[3][3] == "O" and board[2][2] == "O") or
                    (board[5][6] == "O" and board[4][5] == "O" and board[3][4] == "O" and board[2][3] == "O") or
                    (board[1][2] == "O" and board[4][5] == "O" and board[3][4] == "O" and board[2][3] == "O") or
                    (board[1][2] == "O" and board[0][1] == "O" and board[3][4] == "O" and board[2][3] == "O") or
                    (board[4][6] == "O" and board[3][5] == "O" and board[2][4] == "O" and board[1][3] == "O") or
                    (board[0][2] == "O" and board[3][5] == "O" and board[2][4] == "O" and board[1][3] == "O") or
                    (board[3][6] == "O" and board[2][5] == "O" and board[1][4] == "O" and board[0][3] == "O") or
                    (board[5][3] == "O" and board[4][4] == "O" and board[3][5] == "O" and board[2][6] == "O") or
                    (board[5][2] == "O" and board[4][3] == "O" and board[3][4] == "O" and board[2][5] == "O") or
                    (board[1][6] == "O" and board[4][3] == "O" and board[3][4] == "O" and board[2][5] == "O") or
                    (board[5][1] == "O" and board[4][2] == "O" and board[3][3] == "O" and board[2][4] == "O") or
                    (board[1][5] == "O" and board[4][2] == "O" and board[3][3] == "O" and board[2][4] == "O") or
                    (board[1][5] == "O" and board[0][6] == "O" and board[3][3] == "O" and board[2][4] == "O") or
                    (board[5][0] == "O" and board[4][1] == "O" and board[3][2] == "O" and board[2][3] == "O") or
                    (board[1][4] == "O" and board[4][1] == "O" and board[3][2] == "O" and board[2][3] == "O") or
                    (board[1][4] == "O" and board[0][5] == "O" and board[3][2] == "O" and board[2][3] == "O") or
                    (board[4][0] == "O" and board[3][1] == "O" and board[2][2] == "O" and board[1][3] == "O") or
                    (board[0][4] == "O" and board[3][1] == "O" and board[2][2] == "O" and board[1][3] == "O") or
                    (board[3][0] == "O" and board[2][1] == "O" and board[1][2] == "O" and board[0][3] == "O")):
                print(f"{player2} WON")
                player2_wins += 1
                break
            for row in board:
                for col in row:
                    if col == "X" or col == "O":
                        cnt += 1
            if cnt == 881:
                print("TIE")
                break
            elif cnt != 881:
                pass
        else:
            # player2's turn
            while True:
                player2_move = int(input(f"{player2}: "))
                if player2_move == 1:
                    if available_one < 0:
                        print("Can't place it there")
                        display_board()
                        pass
                    else:
                        board[available_one][player2_move - 1] = "O"
                        available_one -= 1
                        display_board()
                        break
                elif player2_move == 2:
                    if available_two < 0:
                        print("Can't place it there")
                        display_board()
                        pass
                    else:
                        board[available_two][player2_move - 1] = "O"
                        available_two -= 1
                        display_board()
                        break
                elif player2_move == 3:
                    if available_tree < 0:
                        print("Can't place it there")
                        display_board()
                        pass
                    else:
                        board[available_tree][player2_move - 1] = "O"
                        available_tree -= 1
                        display_board()
                        break
                elif player2_move == 4:
                    if available_four < 0:
                        print("Can't place it there")
                        display_board()
                        pass
                    else:
                        board[available_four][player2_move - 1] = "O"
                        available_four -= 1
                        display_board()
                        break
                elif player2_move == 5:
                    if available_five < 0:
                        print("Can't place it there")
                        display_board()
                        pass
                    else:
                        board[available_five][player2_move - 1] = "O"
                        available_five -= 1
                        display_board()
                        break
                elif player2_move == 6:
                    if available_six < 0:
                        print("Can't place it there")
                        display_board()
                        pass
                    else:
                        board[available_six][player2_move - 1] = "O"
                        available_six -= 1
                        display_board()
                        break
                elif player2_move == 7:
                    if available_seven < 0:
                        print("Can't place it there")
                        display_board()
                        pass
                    else:
                        board[available_seven][player2_move - 1] = "O"
                        available_seven -= 1
                        display_board()
                        break
                else:
                    print("Wrong input")
                    pass
            if ((board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O" and board[0][3] == "O") or
                    (board[0][1] == "O" and board[0][2] == "O" and board[0][3] == "O" and board[0][4] == "O") or
                    (board[0][2] == "O" and board[0][3] == "O" and board[0][4] == "O" and board[0][5] == "O") or
                    (board[0][3] == "O" and board[0][4] == "O" and board[0][5] == "O" and board[0][6] == "O") or
                    (board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O" and board[1][3] == "O") or
                    (board[1][1] == "O" and board[1][2] == "O" and board[1][3] == "O" and board[1][4] == "O") or
                    (board[1][2] == "O" and board[1][3] == "O" and board[1][4] == "O" and board[1][5] == "O") or
                    (board[1][3] == "O" and board[1][4] == "O" and board[1][5] == "O" and board[1][6] == "O") or
                    (board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O" and board[2][3] == "O") or
                    (board[2][1] == "O" and board[2][2] == "O" and board[2][3] == "O" and board[2][4] == "O") or
                    (board[2][2] == "O" and board[2][3] == "O" and board[2][4] == "O" and board[2][5] == "O") or
                    (board[2][3] == "O" and board[2][4] == "O" and board[2][5] == "O" and board[2][6] == "O") or
                    (board[3][0] == "O" and board[3][1] == "O" and board[3][2] == "O" and board[3][3] == "O") or
                    (board[3][1] == "O" and board[3][2] == "O" and board[3][3] == "O" and board[3][4] == "O") or
                    (board[3][2] == "O" and board[3][3] == "O" and board[3][4] == "O" and board[3][5] == "O") or
                    (board[3][3] == "O" and board[3][4] == "O" and board[3][5] == "O" and board[3][6] == "O") or
                    (board[4][0] == "O" and board[4][1] == "O" and board[4][2] == "O" and board[4][3] == "O") or
                    (board[4][1] == "O" and board[4][2] == "O" and board[4][3] == "O" and board[4][4] == "O") or
                    (board[4][2] == "O" and board[4][3] == "O" and board[4][4] == "O" and board[4][5] == "O") or
                    (board[4][3] == "O" and board[4][4] == "O" and board[4][5] == "O" and board[4][6] == "O") or
                    (board[5][0] == "O" and board[5][1] == "O" and board[5][2] == "O" and board[5][3] == "O") or
                    (board[5][1] == "O" and board[5][2] == "O" and board[5][3] == "O" and board[5][4] == "O") or
                    (board[5][2] == "O" and board[5][3] == "O" and board[5][4] == "O" and board[5][5] == "O") or
                    (board[5][3] == "O" and board[5][4] == "O" and board[5][5] == "O" and board[5][6] == "O") or
                    (board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O" and board[3][0] == "O") or
                    (board[1][0] == "O" and board[2][0] == "O" and board[3][0] == "O" and board[4][0] == "O") or
                    (board[2][0] == "O" and board[3][0] == "O" and board[4][0] == "O" and board[5][0] == "O") or
                    (board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O" and board[3][1] == "O") or
                    (board[1][1] == "O" and board[2][1] == "O" and board[3][1] == "O" and board[4][1] == "O") or
                    (board[2][1] == "O" and board[3][1] == "O" and board[4][1] == "O" and board[5][1] == "O") or
                    (board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O" and board[3][2] == "O") or
                    (board[1][2] == "O" and board[2][2] == "O" and board[3][2] == "O" and board[4][2] == "O") or
                    (board[2][2] == "O" and board[3][2] == "O" and board[4][2] == "O" and board[5][2] == "O") or
                    (board[0][3] == "O" and board[1][3] == "O" and board[2][3] == "O" and board[3][3] == "O") or
                    (board[1][3] == "O" and board[2][3] == "O" and board[3][3] == "O" and board[4][3] == "O") or
                    (board[2][3] == "O" and board[3][3] == "O" and board[4][3] == "O" and board[5][3] == "O") or
                    (board[0][4] == "O" and board[1][4] == "O" and board[2][4] == "O" and board[3][4] == "O") or
                    (board[1][4] == "O" and board[2][4] == "O" and board[3][4] == "O" and board[4][4] == "O") or
                    (board[2][4] == "O" and board[3][4] == "O" and board[4][4] == "O" and board[5][4] == "O") or
                    (board[0][5] == "O" and board[1][5] == "O" and board[2][5] == "O" and board[3][5] == "O") or
                    (board[1][5] == "O" and board[2][5] == "O" and board[3][5] == "O" and board[4][5] == "O") or
                    (board[2][5] == "O" and board[3][5] == "O" and board[4][5] == "O" and board[5][5] == "O") or
                    (board[0][6] == "O" and board[1][6] == "O" and board[2][6] == "O" and board[3][6] == "O") or
                    (board[1][6] == "O" and board[2][6] == "O" and board[3][6] == "O" and board[4][6] == "O") or
                    (board[2][6] == "O" and board[3][6] == "O" and board[4][6] == "O" and board[5][6] == "O") or
                    (board[5][3] == "O" and board[4][2] == "O" and board[3][1] == "O" and board[2][0] == "O") or
                    (board[5][4] == "O" and board[4][3] == "O" and board[3][2] == "O" and board[2][1] == "O") or
                    (board[1][0] == "O" and board[4][2] == "O" and board[3][1] == "O" and board[2][0] == "O") or
                    (board[5][5] == "O" and board[4][4] == "O" and board[3][3] == "O" and board[2][2] == "O") or
                    (board[1][1] == "O" and board[4][4] == "O" and board[3][3] == "O" and board[2][2] == "O") or
                    (board[1][1] == "O" and board[0][0] == "O" and board[3][3] == "O" and board[2][2] == "O") or
                    (board[5][6] == "O" and board[4][5] == "O" and board[3][4] == "O" and board[2][3] == "O") or
                    (board[1][2] == "O" and board[4][5] == "O" and board[3][4] == "O" and board[2][3] == "O") or
                    (board[1][2] == "O" and board[0][1] == "O" and board[3][4] == "O" and board[2][3] == "O") or
                    (board[4][6] == "O" and board[3][5] == "O" and board[2][4] == "O" and board[1][3] == "O") or
                    (board[0][2] == "O" and board[3][5] == "O" and board[2][4] == "O" and board[1][3] == "O") or
                    (board[3][6] == "O" and board[2][5] == "O" and board[1][4] == "O" and board[0][3] == "O") or
                    (board[5][3] == "O" and board[4][4] == "O" and board[3][5] == "O" and board[2][6] == "O") or
                    (board[5][2] == "O" and board[4][3] == "O" and board[3][4] == "O" and board[2][5] == "O") or
                    (board[1][6] == "O" and board[4][3] == "O" and board[3][4] == "O" and board[2][5] == "O") or
                    (board[5][1] == "O" and board[4][2] == "O" and board[3][3] == "O" and board[2][4] == "O") or
                    (board[1][5] == "O" and board[4][2] == "O" and board[3][3] == "O" and board[2][4] == "O") or
                    (board[1][5] == "O" and board[0][6] == "O" and board[3][3] == "O" and board[2][4] == "O") or
                    (board[5][0] == "O" and board[4][1] == "O" and board[3][2] == "O" and board[2][3] == "O") or
                    (board[1][4] == "O" and board[4][1] == "O" and board[3][2] == "O" and board[2][3] == "O") or
                    (board[1][4] == "O" and board[0][5] == "O" and board[3][2] == "O" and board[2][3] == "O") or
                    (board[4][0] == "O" and board[3][1] == "O" and board[2][2] == "O" and board[1][3] == "O") or
                    (board[0][4] == "O" and board[3][1] == "O" and board[2][2] == "O" and board[1][3] == "O") or
                    (board[3][0] == "O" and board[2][1] == "O" and board[1][2] == "O" and board[0][3] == "O")):
                print(f"{player2} WON")
                player2_wins += 1
                break
            for row in board:
                for col in row:
                    if col == "X" or col == "O":
                        cnt += 1
            if cnt == 881:
                print("TIE")
                break
            elif cnt != 881:
                pass
            while True:
                player1_move = int(input(f"{player1}: "))
                if player1_move == 1:
                    if available_one < 0:
                        print("Can't place it there")
                        display_board()
                        pass
                    else:
                        board[available_one][player1_move-1] = "X"
                        available_one -= 1
                        display_board()
                        break
                elif player1_move == 2:
                    if available_two < 0:
                        print("Can't place it there")
                        display_board()
                        pass
                    else:
                        board[available_two][player1_move-1] = "X"
                        available_two -= 1
                        display_board()
                        break
                elif player1_move == 3:
                    if available_tree < 0:
                        print("Can't place it there")
                        display_board()
                        pass
                    else:
                        board[available_tree][player1_move-1] = "X"
                        available_tree -= 1
                        display_board()
                        break
                elif player1_move == 4:
                    if available_four < 0:
                        print("Can't place it there")
                        display_board()
                        pass
                    else:
                        board[available_four][player1_move-1] = "X"
                        available_four -= 1
                        display_board()
                        break
                elif player1_move == 5:
                    if available_five < 0:
                        print("Can't place it there")
                        display_board()
                        pass
                    else:
                        board[available_five][player1_move-1] = "X"
                        available_five -= 1
                        display_board()
                        break
                elif player1_move == 6:
                    if available_six < 0:
                        print("Can't place it there")
                        display_board()
                        pass
                    else:
                        board[available_six][player1_move-1] = "X"
                        available_six -= 1
                        display_board()
                        break
                elif player1_move == 7:
                    if available_seven < 0:
                        print("Can't place it there")
                        display_board()
                        pass
                    else:
                        board[available_seven][player1_move-1] = "X"
                        available_seven -= 1
                        display_board()
                        break
                else:
                    print("Wrong input")
                    pass
            if ((board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X" and board[0][3] == "X") or
                    (board[0][1] == "X" and board[0][2] == "X" and board[0][3] == "X" and board[0][4] == "X") or
                    (board[0][2] == "X" and board[0][3] == "X" and board[0][4] == "X" and board[0][5] == "X") or
                    (board[0][3] == "X" and board[0][4] == "X" and board[0][5] == "X" and board[0][6] == "X") or
                    (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X" and board[1][3] == "X") or
                    (board[1][1] == "X" and board[1][2] == "X" and board[1][3] == "X" and board[1][4] == "X") or
                    (board[1][2] == "X" and board[1][3] == "X" and board[1][4] == "X" and board[1][5] == "X") or
                    (board[1][3] == "X" and board[1][4] == "X" and board[1][5] == "X" and board[1][6] == "X") or
                    (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X" and board[2][3] == "X") or
                    (board[2][1] == "X" and board[2][2] == "X" and board[2][3] == "X" and board[2][4] == "X") or
                    (board[2][2] == "X" and board[2][3] == "X" and board[2][4] == "X" and board[2][5] == "X") or
                    (board[2][3] == "X" and board[2][4] == "X" and board[2][5] == "X" and board[2][6] == "X") or
                    (board[3][0] == "X" and board[3][1] == "X" and board[3][2] == "X" and board[3][3] == "X") or
                    (board[3][1] == "X" and board[3][2] == "X" and board[3][3] == "X" and board[3][4] == "X") or
                    (board[3][2] == "X" and board[3][3] == "X" and board[3][4] == "X" and board[3][5] == "X") or
                    (board[3][3] == "X" and board[3][4] == "X" and board[3][5] == "X" and board[3][6] == "X") or
                    (board[4][0] == "X" and board[4][1] == "X" and board[4][2] == "X" and board[4][3] == "X") or
                    (board[4][1] == "X" and board[4][2] == "X" and board[4][3] == "X" and board[4][4] == "X") or
                    (board[4][2] == "X" and board[4][3] == "X" and board[4][4] == "X" and board[4][5] == "X") or
                    (board[4][3] == "X" and board[4][4] == "X" and board[4][5] == "X" and board[4][6] == "X") or
                    (board[5][0] == "X" and board[5][1] == "X" and board[5][2] == "X" and board[5][3] == "X") or
                    (board[5][1] == "X" and board[5][2] == "X" and board[5][3] == "X" and board[5][4] == "X") or
                    (board[5][2] == "X" and board[5][3] == "X" and board[5][4] == "X" and board[5][5] == "X") or
                    (board[5][3] == "X" and board[5][4] == "X" and board[5][5] == "X" and board[5][6] == "X") or
                    (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X" and board[3][0] == "X") or
                    (board[1][0] == "X" and board[2][0] == "X" and board[3][0] == "X" and board[4][0] == "X") or
                    (board[2][0] == "X" and board[3][0] == "X" and board[4][0] == "X" and board[5][0] == "X") or
                    (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X" and board[3][1] == "X") or
                    (board[1][1] == "X" and board[2][1] == "X" and board[3][1] == "X" and board[4][1] == "X") or
                    (board[2][1] == "X" and board[3][1] == "X" and board[4][1] == "X" and board[5][1] == "X") or
                    (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X" and board[3][2] == "X") or
                    (board[1][2] == "X" and board[2][2] == "X" and board[3][2] == "X" and board[4][2] == "X") or
                    (board[2][2] == "X" and board[3][2] == "X" and board[4][2] == "X" and board[5][2] == "X") or
                    (board[0][3] == "X" and board[1][3] == "X" and board[2][3] == "X" and board[3][3] == "X") or
                    (board[1][3] == "X" and board[2][3] == "X" and board[3][3] == "X" and board[4][3] == "X") or
                    (board[2][3] == "X" and board[3][3] == "X" and board[4][3] == "X" and board[5][3] == "X") or
                    (board[0][4] == "X" and board[1][4] == "X" and board[2][4] == "X" and board[3][4] == "X") or
                    (board[1][4] == "X" and board[2][4] == "X" and board[3][4] == "X" and board[4][4] == "X") or
                    (board[2][4] == "X" and board[3][4] == "X" and board[4][4] == "X" and board[5][4] == "X") or
                    (board[0][5] == "X" and board[1][5] == "X" and board[2][5] == "X" and board[3][5] == "X") or
                    (board[1][5] == "X" and board[2][5] == "X" and board[3][5] == "X" and board[4][5] == "X") or
                    (board[2][5] == "X" and board[3][5] == "X" and board[4][5] == "X" and board[5][5] == "X") or
                    (board[0][6] == "X" and board[1][6] == "X" and board[2][6] == "X" and board[3][6] == "X") or
                    (board[1][6] == "X" and board[2][6] == "X" and board[3][6] == "X" and board[4][6] == "X") or
                    (board[2][6] == "X" and board[3][6] == "X" and board[4][6] == "X" and board[5][6] == "X") or
                    (board[5][3] == "X" and board[4][2] == "X" and board[3][1] == "X" and board[2][0] == "X") or
                    (board[5][4] == "X" and board[4][3] == "X" and board[3][2] == "X" and board[2][1] == "X") or
                    (board[1][0] == "X" and board[4][2] == "X" and board[3][1] == "X" and board[2][0] == "X") or
                    (board[5][5] == "X" and board[4][4] == "X" and board[3][3] == "X" and board[2][2] == "X") or
                    (board[1][1] == "X" and board[4][4] == "X" and board[3][3] == "X" and board[2][2] == "X") or
                    (board[1][1] == "X" and board[0][0] == "X" and board[3][3] == "X" and board[2][2] == "X") or
                    (board[5][6] == "X" and board[4][5] == "X" and board[3][4] == "X" and board[2][3] == "X") or
                    (board[1][2] == "X" and board[4][5] == "X" and board[3][4] == "X" and board[2][3] == "X") or
                    (board[1][2] == "X" and board[0][1] == "X" and board[3][4] == "X" and board[2][3] == "X") or
                    (board[4][6] == "X" and board[3][5] == "X" and board[2][4] == "X" and board[1][3] == "X") or
                    (board[0][2] == "X" and board[3][5] == "X" and board[2][4] == "X" and board[1][3] == "X") or
                    (board[3][6] == "X" and board[2][5] == "X" and board[1][4] == "X" and board[0][3] == "X") or
                    (board[5][3] == "X" and board[4][4] == "X" and board[3][5] == "X" and board[2][6] == "X") or
                    (board[5][2] == "X" and board[4][3] == "X" and board[3][4] == "X" and board[2][5] == "X") or
                    (board[1][6] == "X" and board[4][3] == "X" and board[3][4] == "X" and board[2][5] == "X") or
                    (board[5][1] == "X" and board[4][2] == "X" and board[3][3] == "X" and board[2][4] == "X") or
                    (board[1][5] == "X" and board[4][2] == "X" and board[3][3] == "X" and board[2][4] == "X") or
                    (board[1][5] == "X" and board[0][6] == "X" and board[3][3] == "X" and board[2][4] == "X") or
                    (board[5][0] == "X" and board[4][1] == "X" and board[3][2] == "X" and board[2][3] == "X") or
                    (board[1][4] == "X" and board[4][1] == "X" and board[3][2] == "X" and board[2][3] == "X") or
                    (board[1][4] == "X" and board[0][5] == "X" and board[3][2] == "X" and board[2][3] == "X") or
                    (board[4][0] == "X" and board[3][1] == "X" and board[2][2] == "X" and board[1][3] == "X") or
                    (board[0][4] == "X" and board[3][1] == "X" and board[2][2] == "X" and board[1][3] == "X") or
                    (board[3][0] == "X" and board[2][1] == "X" and board[1][2] == "X" and board[0][3] == "X")):
                print(f"{player1} WON")
                player1_wins += 1
                break
            for row in board:
                for col in row:
                    if col == "X" or col == "O":
                        cnt += 1
            if cnt == 881:
                print("TIE")
                break
            elif cnt != 881:
                pass
    print(f"{player1} won {player1_wins} times")
    print(" ")
    print(f"{player2} won {player2_wins} times")
    print(" ")

    while True:
        # play again?
        play_again = input("Do you want to play again (Y/N) ")
        if play_again.upper() == "Y":
            # create new playing field
            board = [["_", "_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_", "_"],
                     ["_", "_", "_", "_", "_", "_", "_"],
                     ["_", "_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_", "_"],
                     ["_", "_", "_", "_", "_", "_", "_"],
                     ["1", "2", "3", "4", "5", "6", "7"]]
            break
        elif play_again.upper() == "N":
            print("FINAL RESULT:")
            print(f"{player1} won {player1_wins} times")
            print(f"{player2} won {player2_wins} times")
            print(" ")
            # Who is the winner?
            if player1_wins > player2_wins:
                print(f"{player1} is the winner")
                break
            elif player2_wins > player1_wins:
                print(f"{player2} is the winner")
                break
            else:
                print("The points are equal there is no winner")
                break
        else:
            print("Wrong input try again")
            pass
