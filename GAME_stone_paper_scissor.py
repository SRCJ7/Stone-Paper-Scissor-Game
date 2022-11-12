import random
while(True):
    
    g=["STONE","PAPER","SCISSOR"]
    print(g,"\nchoose any one\n")
    a=input(": ")
    b=a.upper()
    if b=="EXIT":
        print("\nTHANK YOU FOR PLAYING\n")
        break
    comp=random.choice(g)
    print("computer choise:",comp)
    
    if b=="STONE":
        if comp=="SCISSOR":
            print("\nYOU WIN\n")
        elif comp=="STONE":
            print("\nDRAW PLAY AGAIN\n")
        else:
            print("\nCOMPUTER WIN\n")
    elif b=="PAPER":
        if comp=="PAPER":
            print("\nDRAW PLAY AGAI\n")
        elif comp=="STONE":
            print("\nYOU WON\n")
        else:
            print("\nCOMPUTER win\n")
    elif b=="SCISSOR":
        if comp=="SCISSOR":
            print("\nDRAW PLAY AGAIN\n")
        elif comp=="STONE":
            print("\nCOMPUTER WIN\n")
        else:
            print("\nYOU WIN\n")

    else:
        print("inv4alid input \n play again\n")
        continue

    print("\nPLAY AGAIN.....for exit type exit\n")
    
