from player import Player
from enum import Enum

class Move(Enum):
    HIT = '1'
    STAY = '2'

target = 21

player1 = Player('Player1')
player2 = Player('Player2')

def determine_winner():
    if player1.total_score == player2.total_score:
        return None
    if player1.total_score > target and player2.total_score > target:
        return None
    if player1.total_score == target:
        return player1
    if player2.total_score == target:
        return player2
    if player1.total_score > target and player2.total_score <= target:
        return player2
    if player2.total_score > target and player1.total_score <= target:
        return player1
    if abs(player1.total_score) > abs(player2.total_score):
        return player1
    if abs(player2.total_score) > abs(player1.total_score):
        return player2

def initialize_game():
    for i in range(0,2):
        player1.hit()
        player2.hit()

def print_score():
    print('\nScore:')
    print('{}: {} = {}'.format(player1.name, player1.score_list, player1.total_score))
    print('{}: {} = {}'.format(player2.name, player2.score_list, player2.total_score))

def print_prompt_for_player_move(player):
    print('\n{} Select option:'.format(player.name))
    print('1. Hit')
    print('2. Stay')

def get_player_move(player):
    print_prompt_for_player_move(player)
    player_move = input()
    while player_move != Move.HIT.value and player_move != Move.STAY.value:
        print('Incorrect option. Try again.')
        print_prompt_for_player_move(player)
        player_move = input()
    return player_move

def perform_move(player):
    if not player.is_staying:
        player_move = get_player_move(player)
        if player_move == Move.HIT.value:
            player.hit()
        else:
            player.stay()
    else:
        print('\n{} chose to stay.'.format(player.name))

def main():
    initialize_game()
    while player1.total_score < target and player2.total_score < target:
        if player1.is_staying and player2.is_staying:
            break
        if player1.is_staying and player2.total_score > player1.total_score:
            break
        if player2.is_staying and player1.total_score > player2.total_score:
            break
        print_score()
        perform_move(player1)
        perform_move(player2)
    winner = determine_winner()
    print('\n****Final Score****')
    print_score()
    if winner:
        print('The winner is', winner.name)
    else:
        print('Draw')

if __name__=="__main__":
    main()

    



        

