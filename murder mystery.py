class Player:
    def __init__(self, name, msgs=""):
        self.name = name
        self.msgs = msgs


player = Player(input("What's your name?"))


def __main__():
    player = input()


print("Okay ", Player, ", give me a few moments.")

import numpy as nump
import pandas as pand
import pyreadline as pyread
import adventurelib as advlib
from adventurelib import *

Room.items = Bag()

current_room = starting_room = Room("""
You find yourself at a party in a secluded location. A few of your friends are around here. To your left you see
Dovahkiin, the host of the party, and ahead of you is Kayla a distant friend of yours.
""")


@when('north', direction='north')
@when('south', direction='south')
@when('east', direction='east')
@when('west', direction='west')
def go(direction):
    global current_room
    room = current_room.exit(direction)
    if room:
        current_room = room
        say('You go %s.' % direction)
        look()
        if room == magic_forest:
            set_context('magic_aura')
        else:
            set_context('default')


@when('take ITEM')
def take(item):
    obj = current_room.items.take(item)
    if obj:
        say('You pick up the %s.' % obj)
        inventory.add(obj)
    else:
        say('There is no %s here.' % item)


@when('drop THING')
def drop(thing):
    obj = inventory.take(thing)
    if not obj:
        say('You do not have a %s.' % thing)
    else:
        say('You drop the %s.' % obj)
        current_room.items.add(obj)


@when('look')
def look():
    say(current_room)
    if current_room.items:
        for i in current_room.items:
            say('A %s is here.' % i)


@when('inventory')
def show_inventory():
    say('You have:')
    for thing in inventory:
        say(thing)


look()
start()


data = pand.read_csv('gumedat.csv', 'gumedat', index_col=None, na_values=['NA'])
columns = data.columns


while True:
    msg = input(Player(": "))
    if msg not in data['gumedat'].tolist():
        data.loc[len(data)] = [msg]+["default"]*(len(columns)-1)
        data.to_csv('gumedat', index=False, sheet_name='gumedat')
        print(friend, end=": ")
        data[friend][len(data)-1] = input()
        data.to_csv('gumedat', index=False, sheet_name='gumedat')
    for (i, q) in enumerate(data['inputs'].tolist()):
        if msg == q:
            print(friend, ":", data[friend].tolist()[i])
            if data[friend].tolist()[i] == "This character doesn't know how to response, please choose " \
                                           "from the prompt." or data[friend].tolist()[i] == '':
                print(friend, end=": ")
                data[friend][i] = input()
                data.to_csv('gumedat', index=False, sheet_name='gumedat')
                break
