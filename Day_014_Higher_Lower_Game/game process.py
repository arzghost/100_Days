from random import choice
from logo import game_logo, versus_logo
from scientists import scientists_names
from os import system

def game_process():
    def get_scientist():
        person = choice(list(scientists_names.keys()))
        data = scientists_names[person]
        del scientists_names[person]
        return (person, data)
    
    
    def get_gender(data):
        if data['Gender'] == 'Male':
            return 'he'
        elif data['Gender'] == 'Female':
            return 'she'
    
    def printed_text(person, data, queue):
        return '{0}. {1}, {2} was born in {3}.'.format(queue, person, get_gender(data), data['Country']), data['Born']

    def good_answer(person1, year1, person2, year2):
        return f'Yes, you are right! {person1} was born in {year1}, {person2} was born in {year2}.'
    person1, data1 = get_scientist()
    person2, data2 = get_scientist()
    flag = True
    correct_answers = 0
    while flag:
        input('Press enter to start: ')
        system('cls')
        print(game_logo)
        string1, year1 = printed_text(person1, data1, 'A')
        string2, year2 = printed_text(person2, data2, 'B')
        print(string1, versus_logo, string2, 'Who was born earlier?', sep = '\n')
        answer = input('Enter A or B: ').upper()
        if answer not in 'AB':
            print('Incorrect letter. Sorry, game stops...')
        else:
            if answer == 'A':
                if year1 < year2:
                    correct_answers +=1
                    print(good_answer(person1, year1, person2, year2))
                else:
                    print(f'Sorry, you fail. Correct answers: {correct_answers}')
                    flag = False
            elif answer == 'B':
                if year2 < year1:
                    correct_answers +=1
                    print(good_answer(person1, year1, person2, year2))
                else:
                    print(f'Sorry, you fail. Correct answers: {correct_answers}')
                    flag = False
        person1, data1 = person2, data2
        if len(list(scientists_names.keys())) == 0:
            print(f'You win! Total score: {correct_answers}.')
            break
        person2, data2 = get_scientist()

if __name__ == '__main__':
    while True:
        game_process()
        again = input("Wanna play again? (Yes or No): ").lower()
        if again == 'yes':
            continue
        else:
            input('Goodbye. Press Enter to exit...')
            break