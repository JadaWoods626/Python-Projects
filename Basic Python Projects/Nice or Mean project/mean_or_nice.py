def start(nice=0,mean=0,name=""): #get user name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)
    
def describe_game(name):
    """
    check if this is a new game or not.
    if it is new, get user name.
    if it is not a new game, thank the player for
    playing afin and continue with game
    """
    #meaning, if we do not already have this user's name,
    #then they are a new player and we need to get their name
    if name != "":
        print("\nThank you for playing agian, {}".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \n You can choose between nice or mean")
                    print("but at the end of the game your faye \n will be sealed by your actions.")
                    stop = False
    return name
def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\n stranger approaches you for a \nconversation. Will you be nice or mean? (N/M) \n>>>".lower())
        if pick == "n":
                   print("\nThe stranger walks away smiling...")
                   nice = (nice + 1)
                   stop =False
        if pick == "m":
                   print("n\The stranger glares at you \nmenacingly and storms off...")
                   mean = (mean +1)
                   stop =False
        score(nice,mean,name) #pass the 3 variables to the score()
                   
def show_score(nice,mean,name):
                   print("\n{}, your current total: \n({}, Nice and ({}, Mean)".format(name,nice,mean))
     
def score(nice,mean,name):
    if nice > 2:
        win(nice,mean,name)
    if mean > 2:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)
        
def win(nice,mean,name):
    print("\nNice job {}, you win! \n Everyone loves you and you've \nmade lots of friends along the way!".format(name))
    again(nice,mean,name)

def lose(nice,mean,name):
    print("\nAhhh to bad, game over! \n{}, you have negative rizz and you \n live in a dirty beat up van \n by the river!".format(name))
    again(nice,mean,name)
    
def again(nice,mean,name):
    stop = True
    choice = input("\nDo you want to play again? (y/n):\n>>>").lower()
    if choice == "y":
        stop = False
        reset(nice,mean,name)
    if choice == "n":
        print("\nOh, so sad, sorry to see you go!")
        stop = False
        quit()
    else:
        print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    start(nice,mean,name)

if __name__ == "__main__":
    start()
        
