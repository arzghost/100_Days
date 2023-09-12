import requests


response = requests.get('https://opentdb.com/api.php?amount=10&type=boolean').json()
question_data = response['results']

if __name__ == '__main__':
    print(question_data)
