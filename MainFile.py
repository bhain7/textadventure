#Prompt to start the game
currentprompt = "Welcome to the game! (write the first prompt here for users )\n"
gameison = True

def promptresponse():
    global resp
    resp = input(currentprompt)


#Define stages
class stage:
     def __init__(self, prompt, option1, option2, option3):
         self.prompt = prompt
         self.option1 = option1
         self.option2 = option2
         self.option3 = option3



#loop that runs the game
while gameison == True:
    promptresponse()

    #Allow user to quit
    if resp == "Exit":
        print("Thanks for playing!")
        gameison = False
        
    
