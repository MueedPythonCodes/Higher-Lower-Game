from day14_game_data import data
import random
import os

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

def setfun_a():
    """The work of this function is that it is called only once in the starting to give the random value of A 
       because in case of right answer we want to Store the value of B into A . So we do not want to again store 
       a new value in A"""
    a=random.choice(data)
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    return a

def setvalueB(a):
    """ The work of this function is that it can not allow A and B having same value or dictionary """
    b=random.choice(data)
    while a==b:
        b=random.choice(data)
    return b


def call(a,score):
    """ The purpose of calling this in while loop is that in case of right answer we want to display
        the score and the new value of A when the user gets it right """
    print(logo)
    print(f"Right Answer.Your score is {score}")
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")


def game():
    score=0
    end=True
    print(logo)
    a=setfun_a()
    while end:
        # print(logo)
        
        print(vs)
        bvalue=setvalueB(a)
        print(f"Compare B: {bvalue['name']}, a {bvalue['description']}, from {bvalue['country']}")
        
        type=input("Who has more followers? Type 'A' or 'B': ").upper()

        if type=="B":
            if bvalue['follower_count']>a['follower_count']:
                a=bvalue
                score += 1
                print(f"Right Answer.Your score is {score}")
                os.system('cls')
                call(a,score)
            else:
                os.system('cls')
                print(logo)
                print(f"Sorry.Thats wrong.You have scored {score}")
                end=False
        elif type=="A":
            if a['follower_count'] > bvalue['follower_count']:
                score += 1
                # print(f"Right Answer.Your score is {score}")
                os.system('cls')
                call(a,score)
            else:
                os.system('cls')
                print(logo)
                print(f"Sorry.Thats wrong.You have scored {score}")
                end=False
        
game()