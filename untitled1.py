# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rCzKVET54L3KVI2k-9pmgZtmBBxewGQb
"""

#ODD OR EVEN GAME

import random
from gtts import gTTS
import os
import time


print('Final Project made by:\nMUHAMMED ALTHAF K.N')
print('___________________________')
print('___________________________')
time.sleep(3)
print('WELCOME TO ODD OR EVEN GAME')
print('___________________________')
tts = gTTS('welcome to odd or even game', lang='en')
tts.save('start.mp3')
os.system('start start.mp3')
time.sleep(3)
print('Please read the instructions carefully before every entries.')
tts = gTTS('Please read the instructions carefully before every entries', lang='en')
tts.save('instructions.mp3')
os.system('start instructions.mp3')
time.sleep(3)
print('__________Lets begin the game!__________')
time.sleep(1)
def odd_even():
    while True:
        tts = gTTS('choose odd or even', lang='en')
        tts.save('select.mp3')
        os.system('start select.mp3')
        time.sleep(1)
        user_choice = input("Choose odd or even: ").lower()
        if user_choice.lower() not in ['odd', 'even']:
            print("Invalid input. Please enter 'odd' or 'even'.")
            continue

        if user_choice.lower() == 'even':
            computer_choice = 'odd'
        else:
            computer_choice = 'even'
            time.sleep(2)
        print(f"Computer chose: {computer_choice}")

        user_number = int(input("Enter a number 1 or 2: "))
        if user_number < 1 or user_number > 2:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue
        computer_number = random.randint(1, 2)
        time.sleep(1)
        print(f"Computer chose: {computer_number}")

        if ((user_number+computer_number)==2 or (user_number+computer_number)==4) and user_choice=='even':
            tts = gTTS('hurray! you won the odd or even game', lang='en')
            tts.save('odevwon.mp3')
            os.system('start odevwon.mp3')
            print("You won the Odd or Even game! Now choose batting or bowling.")
            time.sleep(2)
            tts = gTTS('Please choose batting or bowling', lang='en')
            tts.save('batorbow.mp3')
            os.system('start batorbow.mp3')
            time.sleep(2)
            user_bat_choice = input("Enter 'bat' or 'bowl': ")
            if user_bat_choice.lower() == 'bat':
                batting = 'user'
            else:
                batting = 'computer'
            break
        elif ((user_number+computer_number)==1 or (user_number+computer_number)==3) and user_choice=='odd':
            tts = gTTS('hurray! you won the odd or even game', lang='en')
            tts.save('odev won.mp3')
            os.system('start odev won.mp3')
            print("You won the Odd or Even game! Now choose batting or bowling.")
            time.sleep(2)
            user_bat_choice = input("Enter 'bat' or 'bowl': ")
            if user_bat_choice.lower() == 'bat':
                batting = 'user'
            else:
                batting='computer'
            break
        else:
            time.sleep(1)
            tts = gTTS('Computer won! computer gets to choose batting or bowling', lang='en')
            tts.save('cbatorbow.mp3')
            os.system('start cbatorbow.mp3')
            time.sleep(2)
            print("Computer won the Odd or Even game! Computer gets to choose whether to bat or bowl.")
            computer_decision = random.choice(['bat', 'bowl'])
            time.sleep(2)
            print(f"Computer chose to {computer_decision}.")
            x=computer_decision
            if x=='bat':
                batting='computer'
            else:
                batting = 'user'
            break

    print('_________FIRST INNINGS_________')
    time.sleep(1)
    user_score=0
    computer_score=0

    while True:
        if batting == 'user':
            user_run=int(input('Enter your run : '))
            computer_run = random.randint(1, 6)
            if user_run<1 or user_run>6:
                print('Please enter run between 1 and 6')
                continue
            time.sleep(1)
            print(f"Computer rolled: {computer_run}")
            if user_run == computer_run:
                tts = gTTS('oooooohhhh! you are stumped.', lang='en')
                tts.save('ystump.mp3')
                os.system('start ystump.mp3')
                time.sleep(1)
                print("You are out!")
                batting = 'computer'
                break
            else:
                user_score += user_run
        else:
            user_run = int(input('Enter your run : '))
            computer_run = random.randint(1, 6)
            if user_run<1 or user_run>6:
                print('Please enter run between 1 and 6')
                continue
            time.sleep(1)
            print(f"Computer rolled: {computer_run}")
            if user_run == computer_run:
                tts = gTTS('wowwww! you stumped computer', lang='en')
                tts.save('cstump.mp3')
                os.system('start cstump.mp3')
                time.sleep(1)
                print("Computer's out!")
                batting = 'user'
                break
            else:
                computer_score += computer_run

    time.sleep(2)
    print(f'user score is {user_score}')
    print(f'computer score is {computer_score}')



    print('_________SECOND INNINGS_________')



    while True:
        if batting == 'user':

            user_run=int(input('Enter your run : '))
            computer_run = random.randint(1, 6)
            if user_run<1 or user_run>6:
                print('Please enter run between 1 and 6')
                continue
            time.sleep(1)
            print(f"Computer rolled: {computer_run}")
            if   user_score>computer_score:
                break
            if user_run == computer_run:
                tts = gTTS('oooooohhhh! you are stumped.', lang='en')
                tts.save('ystump.mp3')
                os.system('start ystump.mp3')
                time.sleep(1)
                print("You are out!")
                batting = 'computer'
                break
            else:
                user_score += user_run
        else:
            user_run = int(input('Enter your run : '))
            computer_run = random.randint(1, 6)
            time.sleep(1)
            print(f"Computer rolled: {computer_run}")
            if user_run == computer_run:
                tts = gTTS('wowwww! you stumped computer', lang='en')
                tts.save('cstump.mp3')
                os.system('start cstump.mp3')
                time.sleep(1)
                print("Computer's out!")
                batting = 'user'
                break
            else:
                computer_score += computer_run
                if computer_score > user_score:
                    break

    time.sleep(2)
    print(f'user score is {user_score}')
    print(f'computer score is {computer_score}')

    time.sleep(2)
    if computer_score>user_score:
        print('Computer Won!')
        tts = gTTS('ouch! computer won this time.thanks for playing', lang='en')
        tts.save('loss.mp3')
        os.system('start loss.mp3')
    elif user_score>computer_score:
        print('You Won!')
        tts = gTTS('Hurray! you won the game.thanks for playing', lang='en')
        tts.save('victory.mp3')
        os.system('start victory.mp3')
    else:
        print('Tie Match!')
        tts = gTTS('this game ended in a tie.thanks for playing', lang='en')
        tts.save('tie.mp3')
        os.system('start tie.mp3')
odd_even()