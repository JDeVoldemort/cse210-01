#Tic-Tac-Toe Jim DeMordaunt


def main():
    try:
        game = 1
        turn_count =0
        scores = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        turn = 'x'
        print_score(1, scores)
        while game == 1:
            choice = (input('Choose a number of the ones not chosen:'))
            turn_count+=1
            if scores[choice] != 'x' and scores[choice]!= 'o':
                scores[choice] = turn
                print_score(2,scores)
                game=score_check(scores, turn, turn_count)
                if turn == 'x':
                    turn = 'o'
                elif turn == 'o':
                    turn = 'x'

            else:
                print('cheaters shall be banned. start over!')
                game = 0

            

            



    except ValueError as val_err:

        print()
        print(type(val_err).__name__, val_err, sep=': ')
        print('You entry is invalid')
        print('Run the program again and enter an number.')
    except KeyError as key_err:

        print()
        print(type(key_err).__name__, key_err, sep=': ')
        print('key error')

def print_score(state, scores):
    if state == 1:
        print(f'1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9\n')
    elif state == 2:
        print(f"{scores['1']}|{scores['2']}|{scores['3']}\n{scores['4']}|{scores['5']}|{scores['6']}\n{scores['7']}|{scores['8']}|{scores['9']}\n")

def score_check(scores, turn, turn_count):
    if scores['1'] == turn and scores ['2'] == turn and scores['3'] == turn:
        print(f'{turn} wins')
        game = 0
    elif scores['4'] == turn and scores ['5'] == turn and scores['6'] == turn:
        print(f'{turn} wins')
        game = 0
    elif scores['7'] == turn and scores ['8'] == turn and scores['9'] == turn:
        print(f'{turn} wins')
        game = 0
    elif scores['1'] == turn and scores ['4'] == turn and scores['7'] == turn:
        print(f'{turn} wins')
        game = 0
    elif scores['1'] == turn and scores ['5'] == turn and scores['9'] == turn:
        print(f'{turn} wins')
        game = 0
    elif scores['2'] == turn and scores ['5'] == turn and scores['8'] == turn:
        print(f'{turn} wins')
        game = 0
    elif scores['3'] == turn and scores ['6'] == turn and scores['9'] == turn:
        print(f'{turn} wins')
        game = 0
    elif scores['3'] == turn and scores ['5'] == turn and scores['7'] == turn:
        print(f'{turn} wins')
        game = 0
    
    elif turn_count > 9:
        print('draw please play again')
        game = 0
    else:
        print(f'next turn:')
        game = 1
    return game

    
    
    # elif state == 2 and turn == 'x':

    # elif state == 2 and turn == 'o':



if __name__ == "__main__":
    main()