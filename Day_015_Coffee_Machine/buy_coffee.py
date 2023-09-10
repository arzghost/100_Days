from coffeeMachine import *
from os import system
from time import sleep


def get_money(coins):
    total = 0
    for key in coins.keys():
        total += int(input(f'How many {key} will you put? '))* coins[key]
    return total

if __name__ == '__main__':
    commands = ['espresso', 'americano', 'capucchino', 'latte', 'status', 'add', 'stop', 'break', 'halt', 'take']
    while True:
        sleep(2)
        system('cls')
        request = input('''Which coffee would you like? (type espresso/americano/capucchino/latte): ''').lower()
        if request not in commands:
            print('Wrong command!')
        elif request == 'stop' or request == 'break' or request =='halt':
            print('Machine is stopped.')
            break
        elif request == 'status':
            for key, value in machine.items():
                print(f'{key.capitalize()}: {value}.')
            input('Press Enter to continue...')
        elif request == 'add':
            machine['water'] += int(input('How many milliliters of water would you like to add?: '))
            machine['coffee'] += int(input('How many grams of coffee would you like to add?: '))
            machine['milk'] += int(input('How many milliliters of milk would you like to add?: '))
            print('Everything was add in coffee machine!')
        elif request == 'take':
            machine['money'] = 0
            print('Money were taken! :)')
        else:
            if recipes[request]['water'] > machine['water'] or recipes[request]['coffee'] > machine['coffee'] or recipes[request]['milk'] > machine['milk']:
                print('Sorry, not enough ingredients. Call anyone to add them.')
            else:
                pattern = 'The {} costs {} dollars. Would you like to continue? '.format(request, recipes[request]['cost'])
                answer = input(pattern).lower()
                if answer == 'yes' or answer == '':
                    put_money = get_money(coins)
                    if put_money < recipes[request]['cost']:
                        print('Sorry, you put not enough money.')
                    else:
                        input(f'Have a nice {request}! Press Enter to continue...\n')
                        machine['water'] -= recipes[request]['water']
                        machine['coffee'] -= recipes[request]['coffee']
                        machine['milk'] -= recipes[request]['milk']
                        machine['money'] += put_money
                elif answer == 'no':
                    print('Aborting process...')
                else:
                    print('Incorrect answer.')