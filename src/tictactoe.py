#Tic Tac Toe
import random
import time

marker = {'Player 1': 'X', 'Player 2': 'O'}

def display_board(board):
    print('+' + '-' * 26 + '+\n|7\t|8\t|9\t|')
    print('|' + ' ' * 3 + board[7] + ' ' * 3 + '|' + ' ' * 3 + board[8] + ' ' * 3 + '|' + ' ' * 3 + board[9] + ' ' * 3 + '|')
    print('| \t| \t| \t|\n' + '+' + '-' * 26 + '+\n|4\t|5\t|6\t|')
    print('|' + ' ' * 3 + board[4] + ' ' * 3 + '|' + ' ' * 3 + board[5] + ' ' * 3 + '|' + ' ' * 3 + board[6] + ' ' * 3 + '|')
    print('| \t| \t| \t|\n' + '+' + '-' * 26 + '+\n|1\t|2\t|3\t|')
    print('|' + ' ' * 3 + board[1] + ' ' * 3 + '|' + ' ' * 3 + board[2] + ' ' * 3 + '|' + ' ' * 3 + board[3] + ' ' * 3 + '|')
    print('| \t| \t| \t|\n' + '+' + '-' * 26 + '+')

def choose_first():
    player = random.randint(0,1)
    if(player):
        return 'Player 1'
    else:
        return 'Player 2'

def display_score(score):
    print('Final Score :')
    print('Player 1 : ' + str(score['Player 1']))
    print('Player 2 : ' + str(score['Player 2']))

def place_marker(board, marker, position):
    board[position] = marker


def win_check(board,mark):
    if((board[7] == board[4] == board[1] == mark) or \
    (board[8] == board[5] == board[2] == mark) or \
    (board[9] == board[6] == board[3] == mark) or \
    (board[7] == board[8] == board[9] == mark) or \
    (board[4] == board[5] == board[6] == mark) or \
    (board[1] == board[2] == board[3] == mark) or \
    (board[7] == board[5] == board[3] == mark) or \
    (board[9] == board[5] == board[1] == mark)):
        return True
    else:
        return False


def board_check(board):
    empty = 0
    for i in range(0,len(board)):
        if(board[i] == ' '):
            empty += 1
    if(empty > 1):
        return False
    else:
        return True

def player_choice(board, turn):
    try:
        choice = int(input(turn + '[ ' + marker[turn] + ' ]: Pick Square: (1 - 9): '))
    except ValueError:
        print('Wrong Input !')
        return player_choice(board,turn)
    if(choice < 1 or choice > 9):
        print('Your choice should be between 1 and 9 !')
        return player_choice(board,turn)
    if(board[choice] == ' '):
        return choice
    else:
        print('This square has already been marked with {}'.format(board[choice]))
        return player_choice(board,turn)

def replay():
    answer = input('Do you want to play again? [Yes / No] : ')
    if(answer == 'Yes' or answer == 'yes'):
        return True
    elif(answer == 'No' or answer == 'no'):
        return False
    else:
        return replay()
def next_player(turn):
    if(turn == 'Player 1'):
        return 'Player 2'
    elif(turn == 'Player 2'):
        return 'Player 1'

def main():
    score = {'Player 1': 0, 'Player 2': 0}
    print('Here we go!\nPicking random player sto start ', end = '')
    for t in range(1):
        print(".", flush='True', end=' ')
        time.sleep(0.2)
    print()
    turn = choose_first()
    print("\n" + turn + ' plays first.')
    first = turn
    game_round = 1
    while True:
        theBoard = [' '] * 10
        game_on = True
        while game_on:
            display_board(theBoard)
            position = player_choice(theBoard, turn)
            place_marker(theBoard, marker[turn], position)
            if win_check(theBoard, marker[turn]):
                display_board(theBoard)
                print('Winner is '+ turn)
                score[turn] = score.get(turn, 0) + 1
                game_on = False
            elif board_check(theBoard):
                display_board(theBoard)
                print('Tie!')
                game_on = False
            else:
                turn = next_player(turn)
        if not replay():
            ending = ''
            if game_round>1 : ending = 's'
            print("After {} round{}".format(game_round, ending))
            display_score(score)
            break
        else :
            game_round += 1
            turn = next_player(first)
            first = turn
main()
