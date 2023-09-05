bill, percentage, people_number = '', '', ''

while bill == '':
    try:
        enter = input('Enter your total bill: $')
        bill = float(enter)
    except ValueError:
        print(f'Your value {enter} is incorrect')
        bill = ''

while percentage == '':
    try:
        enter = input('Enter your percent for tips: ')
        percentage = float(enter)
    except ValueError:
        print(f'Your value {enter} is incorrect')
        percentage = ''

while people_number == '':
    try:
        enter = input('Enter number of people: ')
        people_number = int(enter)
        1 / people_number
    except ValueError:
        print(f'Your value {enter} is incorrect')
        people_number = ''
    except ZeroDivisionError:
        print(f'Number of people cannot equal to 0.')
        people_number = ''


print(f'Everyone pays ${round(bill * percentage / (100 * people_number), 2)}')