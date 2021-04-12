import os
import requests


def start():
    print("Welcome to IsItDown.py!")
    print("Please write URL or URLs you want to check (seperated by comma)")
    a_input = input().lower()
    a_list = a_input.split(',')
    for word in a_list:
        check_URL(word)
    restart()


def check_URL(a_word):
    a_word = a_word.strip()
    if a_word.endswith('.com') == False:
        print(f'{a_word} is not a valid URL')

    elif a_word.startswith("http://"):
        get_request(a_word)

    else:
        a_word = 'http://' + a_word
        get_request(a_word)


def get_request(a_url):
    try:
        r = requests.get(a_url)
        if r.status_code == requests.codes.ok:
            print(f"{a_url} is up!")
        else:
            print(f"{a_url} is down!")

    except:
        print(f"{a_url} is down!")


def restart():
    print('Do you want to start over? y/n', end=' ')
    b_input = input().lower()
    if b_input == 'y':
        os.system('clear')
        start()
    elif b_input == 'n':
        print('k. bye!')
    else:
        print("That's not a valid answer")
        restart()


start()
