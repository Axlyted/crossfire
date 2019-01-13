from npcs import Human
from art import *
import sys,time,random

def slow_type(t):
    typing_speed = 90 #wpm
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)

print(text2art("CrossFir3 Xi"))

name = input("Please enter your name: ")
player = Human(name)



slow_type("Hello " + name + "!, Welcome to CrossFir3, a modern CLI adventure.\n\n" + 
"You standing in the fortest when suddenly you hear a strange sound coming out of the woods.\n")

a = input(name +" : what was that? I better go check it out\n")

options1 = {
    "check" : "The woods are on the east. I can see a well on the west and a road to the south"
    "north" : "Ouch! I thought it was unnecessary to mention the huge wall infront of me :("
    "west" : 
}



