from random import randint
import time
import math
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

wins = 0
losses = 0

def monty_hall():

    print('''
Welcome! This is a Monty Hall Problem Python Program... Monty Python.
Some light reading before we begin...

Type Enter twice as you read to continue to the next segment. Or type
skip + Enter at any point to skip the intro text.''')

    next = input('')
    if next == 'skip':
        play_or_simulate()
    elif next != '\n':
        next = input('')


    print('''Monty Hall was the presenter on the game show \'Let's Make a Deal\', and the
problem is based on a game that was played on that show. It goes like this:''')

    next = input('')
    if next == 'skip':
        play_or_simulate()
    elif next != '\n':
        next = input('')

    print('''Monty shows you three doors. Behind one is a brand new car; the others,
goats (these are working goats, you can't take them home as a prize).''')

    next = input('')
    if next == 'skip':
        play_or_simulate()
    elif next != '\n':
        next = input('')

    print('''First, you choose a door, and of course you have a 1/3 chance of choosing
the prize door. This is where things get interesting.''')

    next = input('')
    if next == 'skip':
        play_or_simulate()
    elif next != '\n':
        next = input('')

    print('''Monty will then open one of the doors you didn't choose, always revealing a
goat (since there are two goats and one you, he can always do this). You are
then offered the following choice:''')

    next = input('')
    if next == 'skip':
        play_or_simulate()
    elif next != '\n':
        next = input('')


    print(      '''Stay with your original choice of door, or switch doors.\n''')

    next = input('')
    if next == 'skip':
        play_or_simulate()
    elif next != '\n':
        next = input('')

    print('''What should you do? It seems you now have a 50/50 chance (stay or change) of
winning. Or are appearances deceiving?

    ''')

    next = input('')
    if next == 'skip':
        play_or_simulate()
    elif next != '\n':
        next = input('')



    play_or_simulate()




def play_or_simulate():

    res = input('''Type p + Enter to play the game yourself.

Type s + Enter to simulate a large number of games.

Type r + Enter to see win/loss record.

Type c + Enter to clear win/loss record.

Type exit + Enter to quit.\n''')

    global wins
    global losses

    if res == 'p':
        play()
    elif res == 's':
        simulate()
    elif res == 'exit':
        quit()
    elif res == 'c':
        wins = 0
        losses = 0
        play_or_simulate()
    elif res == 'r':
        print('Wins: {wins}. Losses: {losses}\n'.format(wins=wins, losses=losses))
        time.sleep(2)
        play_or_simulate()
    else:
        play_or_simulate()




def play():
    print('\nLet\'s play! Here are the doors:\n')
    doors = ['1', '2', '3']
    prizes = ['goat' for i in range(0, 3)]
    prize_idx = randint(0, 2)
    prizes[prize_idx] = 'car!'
    print(doors)
    print('')
    first_choice = None
    while first_choice not in ['1', '2', '3']:
        first_choice = input('Which door do you want to choose?\n')
    first_choice_idx = int(first_choice) - 1
    Montys_choice_idx = None
    if prize_idx == first_choice_idx:
        remaining_indices = [0, 1, 2]
        remaining_indices.remove(prize_idx)
        random_binary = randint(0, 1)
        remaining_indices.pop(random_binary)
        Montys_choice_idx = remaining_indices[0]
    else:
        remaining_indices = [0, 1, 2]
        remaining_indices.remove(prize_idx)
        remaining_indices.remove(first_choice_idx)
        Montys_choice_idx = remaining_indices[0]
    Montys_choice = doors[Montys_choice_idx]
    print('You chose door {}!\n'.format(first_choice))
    time.sleep(2)
    print('And here\'s Monty, opening door {}!'.format(Montys_choice))
    time.sleep(2)
    doors[Montys_choice_idx] = 'goat'
    print('\nHere are the doors now:')
    print(doors)
    time.sleep(3)
    res = None
    while res not in ['y', 'n']:
        res = input('\nYour first choice was door {}. Would you like to switch? y/n\n'.format(first_choice))
    second_choice = None
    if res == 'y':
        switch_indices = [0, 1, 2]
        switch_indices.remove(first_choice_idx)
        switch_indices.remove(Montys_choice_idx)
        switch_idx = switch_indices[0]
        second_choice = doors[switch_idx]
    else:
        second_choice = first_choice
    print('''Let's see what's behind your door!\n''')
    time.sleep(3)
    behind_your_door = prizes[int(second_choice)-1]
    print('You found: {}'.format(behind_your_door))
    if behind_your_door == 'goat':
        global losses
        losses += 1
        print('Sorry! You lose!\n')
    else:
        global wins
        wins += 1
        print('You win a brand new car!!!\n')
    print('Wins: {wins},  Losses: {losses}'.format(wins=wins, losses=losses))
    time.sleep(4)
    play_or_simulate()




def simulate():
    N = input('How many games do you want to simulate?\n')
    try:
        N = int(N)
    except:
        simulate()
    if int(N) <= 0:
        simulate()
    else:
        strategy = None
        while strategy not in ['a', 'b', 'c']:
            strategy = input('''Which strategy would you like to implement?
[a] Always stay.
[b] Always switch.
[c] Live Laugh Love (random on-the-spot decision).\n''')
    if strategy == 'a':
        simulate_stay(N)
    elif strategy == 'b':
        simulate_switch(N)
    elif strategy == 'c':
        simulate_live_laugh_love(N)

def simulate_stay(N):
    fig, ax = plt.subplots()
    #x = ['Win %', 'Loss %']
    y = [0, 0]

    def animate(i):
        car_idx = randint(0, 2)
        player_idx = randint(0, 2)
        if car_idx == player_idx:
            y[0] += 1
        else:
            y[1] += 1
        ax.clear()
        ax.set_ylim(0, 1)
        ax.set_title('Always Staying')
        ax.set_xlabel('Round {}'.format(i))
        ax.bar(['Win %: {}'.format(round((y[0]/i)*100, 2)), 'Loss %: {}'.format(round((y[1]/i)*100, 2))], [y[0]/i, y[1]/i], color=['green', 'red'])


    ani = FuncAnimation(fig, animate, frames=range(1, N + 1), repeat=False, interval=10)

    plt.show()

    play_or_simulate()

def simulate_switch(N):
    fig, ax = plt.subplots()
    x = ['Win %', 'Loss %']
    y = [0, 0]

    def animate(i):
        car_idx = randint(0, 2)
        player_idx = randint(0, 2)
        if car_idx == player_idx:
            indices = [0, 1, 2]
            indices.remove(car_idx)
            rand_bin = randint(0, 1)
            Monty_idx = indices[rand_bin]
        else:
            indices = [0, 1, 2]
            indices.remove(car_idx)
            indices.remove(player_idx)
            Monty_idx = indices[0]
        switch_to_list = [0, 1, 2]
        switch_to_list.remove(player_idx)
        switch_to_list.remove(Monty_idx)
        new_player_idx = switch_to_list[0]
        if car_idx == new_player_idx:
            y[0] += 1
        else:
            y[1] += 1
        ax.clear()
        ax.set_ylim(0, 1)
        ax.set_title('Always Switching')
        ax.set_xlabel('Round {}'.format(i))
        ax.bar(['Win %: {}'.format(round((y[0]/i)*100, 2)), 'Loss %: {}'.format(round((y[1]/i)*100, 2))], [y[0]/i, y[1]/i], color=['green', 'red'])


    ani = FuncAnimation(fig, animate, frames=range(1, N + 1), repeat=False, interval=10)

    plt.show()

    play_or_simulate()

def simulate_live_laugh_love(N):
    fig, ax = plt.subplots()
    x = ['Win %', 'Loss %']
    y = [0, 0]

    def animate(i):
        stay_or_switch = randint(0, 1)
        if stay_or_switch == 0:
            car_idx = randint(0, 2)
            player_idx = randint(0, 2)
            if car_idx == player_idx:
                y[0] += 1
            else:
                y[1] += 1
        else:
            car_idx = randint(0, 2)
            player_idx = randint(0, 2)
            if car_idx == player_idx:
                indices = [0, 1, 2]
                indices.remove(car_idx)
                rand_bin = randint(0, 1)
                Monty_idx = indices[rand_bin]
            else:
                indices = [0, 1, 2]
                indices.remove(car_idx)
                indices.remove(player_idx)
                Monty_idx = indices[0]
            switch_to_list = [0, 1, 2]
            switch_to_list.remove(player_idx)
            switch_to_list.remove(Monty_idx)
            new_player_idx = switch_to_list[0]
            if car_idx == new_player_idx:
                y[0] += 1
            else:
                y[1] += 1
        ax.clear()
        ax.set_ylim(0, 1)
        ax.set_title('Randomly Staying or Switching')
        ax.set_xlabel('Round {}'.format(i))
        ax.bar(['Win %: {}'.format(round((y[0]/i)*100, 2)), 'Loss %: {}'.format(round((y[1]/i)*100, 2))], [y[0]/i, y[1]/i], color=['green', 'red'])


    ani = FuncAnimation(fig, animate, frames=range(1, N + 1), repeat=False, interval=10)

    plt.show()

    play_or_simulate()



monty_hall()
