gameison = True

#Class to hold the stages
class stage:
     def __init__(self, prompt):
         self.prompt = prompt
         
         self.option1 = ""
         self.option2 = ""
         self.option3 = ""

#Initiate all the stages
gamestart = stage("Welcome to the game! (write the first prompt here for users )\n Option1: go to Paris \n")
paris = stage("Bonjour, you arrive in Paris and die of dyssentary. \n")



#Set the stage paths
gamestart.option1 = (paris)




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
        
    if resp == "1":
        currentstage = currentstage.option1
    elif resp == "2":
        currentstage = currentstage.option2
    elif resp == "3":
        currentstage = currentstage.option3
    else:
        print("Sorry! Bad input! Type 1 2 or 3! Thanks buddy!")
        


    




