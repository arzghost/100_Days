import random as rnd
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def game_process():
    logo = r'''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/         
'''
    cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


    def card_chooser(cards: dict) -> list:
        return [rnd.choice(list(cards.keys())) for i in range(2)]
    

    def points(stack: list) -> int:
        result = 0
        for card in stack:
            result += cards[card]
        return result


    def add_cards(someone_cards: list) -> list:
        someone_cards += [rnd.choice(list(cards.keys()))]
        return someone_cards
    

    def time_to_play():
        input('Let\'s start a game! Press any key...')
        cls()
        player_cards, bot_cards = card_chooser(cards), card_chooser(cards)
        while True:
            print(logo)
            player_points, bot_points = points(player_cards), points(bot_cards)
            print(f'\nYour cards: {player_cards}, your sum: {player_points}')
            print(f'Bot has a card: {bot_cards[0]}')
            if bot_points <= 17:
                add_cards(bot_cards)
                bot_points = points(bot_cards)
            if player_points < 21:
                your_answer = input('Would you like to take a card? (print "yes" or "no"): ').lower()
                if your_answer in 'yes нуы':
                    add_cards(player_cards)
                    cls()
                    continue
            if player_points > 21:
                print('\nYou lose.')
            elif bot_points > 21:
                print('\nYou win!')
            elif player_points < bot_points:
                print('\nYou lose.')
            elif player_points > bot_points or player_points == 21 and bot_points != 21:
                print('\nYou win!')
            elif player_points == bot_points:
                print('\nIt\'s a draw.')
            print(f'Your cards: {player_cards}, your sum: {player_points}')
            print(f'Bot cards: {bot_cards}, bot sum: {bot_points}')
            break
            

    time_to_play()


if __name__ == '__main__':
    flag = True
    while flag:
        game_process()
        answer = input('\nWould you like to play again? (print "yes" or "no"): ').lower()
        if answer != 'yes':
            flag = False
            print('Have a nice day!')
            input('Press Enter to exit...')
        else:
            cls()
            