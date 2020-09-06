from playsound import playsound


import random as R
#Needs to be true for game to be on.
gameison = True

#Set Game Mode Exploremode or Battlemode
mode = "Exploremode"





#Class to hold the stages
class stage:
     def __init__(self, prompt):
         self.prompt = prompt

         self.option1 = ""
         self.option2 = ""
         self.option3 = ""


#Create the player and health
class player:
    def __init__(self,health,attack,defense,speed):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed

    def attackTarget(self, target):
        target.health -= self.attack
        print("Player attacked dealing",self.attack,"damage")
        print("Enemy",target,"has", target.health,"health")

class enemy_npc:
    def __init__(self,name,health,attack,defense,speed):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.name = name
    def __str__(self):
        return self.name
    def attackTarget (self, target):
        target.health -= self.attack




#Create the player with random stats
user = player(R.randrange(75,100,1),R.randrange(1,10,1),R.randrange(0,5,1),R.randrange(0,5,1))

#First enemy for battlemode
enemy = enemy_npc("Ogre",R.randrange(25,50,1),R.randrange(1,10,1),R.randrange(0,5,1),R.randrange(0,5,1))

#Initiate all the stages
gamestart = stage("Welcome to the game! (write the first prompt here for users )\n Option1: go to Paris \n Option2: Guess who dropped their car keys in the Sewers. It was you.  \n Option3: Give up and be at your home. This is MTV and u will be at ur at ur crib \n")
paris = stage("Bonjour, you arrive in Paris and die of dyssentary. \n You could go somewhere though? \n")
Sewers = stage("Dripping noises and farty smells. You're not in Paris though! \n")
Home = stage("You're home because of quarantine \n")


#Set the stage paths
gamestart.option1 = paris
gamestart.option2 = Sewers
gamestart.option3 = Home

paris.option1 = Sewers
paris.option2 = Home


currentstage = gamestart



def promptresponse():
    global resp

    if mode == "Battlemode":
        resp = input('What battle action would you like to take? \n 1. Attack Timidly\n 2. Attack Angrily and sloppily\n 3. Attack soothingly\n')

    elif mode == "Exploremode":
        resp = input(currentstage.prompt)

    if resp == "Exit":
        print("Thanks for playing!")
        gameison = False

def movestage(stagenumber):
    global currentstage

    if resp == "1" and currentstage.option1 != "":
            currentstage = currentstage.option1
    elif resp == "2" and currentstage.option2 != "":
            currentstage = currentstage.option2
    elif resp == "3" and currentstage.option3 != "":
            currentstage = currentstage.option3
    else:
            print("Sorry! Bad input! Type 1 2 or 3! Also make sure that stage exists! Thanks buddy!")



#loop that runs exploremode
while gameison == True and mode == "Exploremode":
    promptresponse()

    #Function to move to the next stage.
    movestage(resp)

#loop that runs battlemode
turn = 0
if mode == "Battlemode":
    playsound("battlemusic.mp3", False)
while gameison == True and mode == "Battlemode":
    if turn == 0:
        print("You have entered battlemode, son")
        print("You have entered combat with a ferocious",enemy)
    turn = turn + 1
    promptresponse()

    if resp == "1":
        user.attackTarget(enemy)
        enemy.attackTarget(user)
    elif resp == "2" :
        user.attackTarget(enemy)
        enemy.attackTarget(user)
    elif resp == "3" :
        user.attackTarget(enemy)
        enemy.attackTarget(user)
    else:
        print("Sorry! Bad input! Type 1 2 or 3! Also make sure that stage exists! Thanks buddy!")








