gameison = True

#Class to hold the stages
class stage:
     def __init__(self, prompt, option1, option2, option3):
         self.prompt = prompt
         self.option1 = option1
         self.option2 = option2
         self.option3 = option3

gamestart = stage("Welcome to the game! (write the first prompt here for users )\n","stage1","stage2","stage3")
currentstage = gamestart

def promptresponse():
    global resp
    resp = input(currentstage.prompt)


#loop that runs the game
while gameison == True:
    promptresponse()

    #Allow user to quit
    if resp == "Exit":
        print("Thanks for playing!")
        gameison = False
        
    
