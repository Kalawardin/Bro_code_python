import random

while True:
    choices = ["R","P","S"]
    computer = random.choice(choices)
    user = input("What is your choice:(R,P,S)\n").upper()
    
    if user == computer:
        print("Tie!")
    elif user == "R" and computer == "S":
        print("Humans wins!")
    elif user == "P" and computer == "R":
        print("Humans wins!")
    elif user == "S" and computer == "P":
        print("Humans wins!")
    elif user not in choices:
        print("\nPlease enter valid input!!!!!!\n")
        continue
    else:
        print(f"\nAI predicts {computer}. Bots wins!")
    
    cycle = input("\nWanna play again?(Y/N)").upper() 
    if cycle != "Y":
        break
print("Bye!")
        
    
    
        

    
    
        