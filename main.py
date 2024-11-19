def getuserchoice():
    userchoice = str(input("What is the highest mountain in the world? (lowercase)")).lower()
    while userchoice not in ['mount everest']:
        print("That's wrong, try again")
        userchoice = str(input("What is the highest mountain in the world(all lowercase)")).lower()
    if userchoice == "mount everest":
        print("You are right!")
    return userchoice
getuserchoice()