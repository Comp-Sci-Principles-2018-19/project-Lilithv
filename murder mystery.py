import numpy as nump
import pandas as pand
import pyreadline as pyread


class Player:
    def __init__(self, name, msgs=""):
        self.name = name
        self.msgs = msgs


name = (input("What's your name?"))

player = Player(name, ' ')

print("Okay ", player.name, ", give me a few moments.")

import adventurelib as advlib
from adventurelib import *

Room.items = Bag()

current_room = starting_room = Room("""
You find yourself at the center of a party in a secluded location. A few of your friends are around here. To your left
 you see
Dovahkiin, the host of the party, and ahead of you is Kayla, a distant friend of yours.
""")

balcony = starting_room.north = Room("""
You walk ahead towards the balcony, looking over a clearing. Kayla stands there with her arms resting on the railing,
her hair flowing wildly in the wind.
""")

sitting_room = starting_room.west = Room("""
You turn and go towards Dovahkiin, who seems extremely relaxed with a book in hand. He almost looks sleepy.
""")

hallway = starting_room.east = Room("""
You enter a hallway. Ahead of you in the kitchen you hear someone voraciously eating
""")

kitchen = hallway.north = Room("""
You enter the kitchen to the sight of Lawrence raiding it, devouring any snacks in sight. It comes off as piggish though
he must have a reason for his appetite.
""")

pathway = starting_room.south = Room("""
""")


garden1 = pathway.west = Room("""
As you walk closer to Dorathy, you notice she seems to be picking something off the flowers and placing it in a cup. It
looks as if the inside of the cup is squirming, which makes it kind of mesmerizing.
""")

garden2 = pathway.east = Room("""
You look at the garden next to you and there seems to be fresh fruit trees and very leafy vegetables sprouting from the 
ground. They look absolutely delectable.
""")

garden3 = pathway.south = Room("""
""")

pool = garden3.west = Room("""
You walk up to the pool with Alice circling the perimeter of it. She seems lost in thought, almost hypnotized by the 
pool itself. Although the pool is in desperate need of cleaning, the leaf litter and dead insects practically piling up.
""")

forest = garden3.east = Room("""
You walk closer to Harold and notice he seemed to have come from a hiking trail that leads to here. You figure his home 
must be nearby the trail. Upon closer inspection, you see he's fiddling with a RC drone.""")


@when('north', direction='north')
@when('south', direction='south')
@when('east', direction='east')
@when('west', direction='west')
def go(direction):
    global current_room
    room = current_room.exit(direction)
    if room:
        if room == pathway and current_room == garden1 or current_room == garden2 or current_room == garden3:
            say("""You come back to the pathway, and look over the property. To the left of you Dorathy is tending to 
            some flowers. Further ahead Alice slowly paces around the edge of the pool. 
            Off closer to the forest you see Harold just arriving.""")
        elif room == pathway:
            say("""
            You exit the house, and look over the property. To the left of you Dorathy is tending to some flowers. 
            Further ahead
            Alice slowly paces around the edge of the pool. Off closer to the forest you see Harold just arriving.
            """)
        if room == garden3 and current_room == pool or current_room == forest:
            say("""The stone pathway returns and you see the pool with Alice by it to your left, and Harold preparing
             something to your right.""")
        elif room == garden3:
            say("""The stone pathway runs out and you see the pool with Alice by it to your left, 
            and Harold preparing something to your right.""")
        current_room = room
        say('You walk %s.' % direction)
        look()


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
