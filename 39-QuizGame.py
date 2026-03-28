Questions = {
    "Which planet is known as the Red Planet?":"B",
    "Which animal is the largest mammal in the world?":"B",
    "What color do you get by mixing Blue and Yellow?":"A",
    "Who is the founder of Microsoft?":"C",
}

Options = [["A) Earth", "B) Mars", "C) Venus", "D) Jupiter"],
           ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Shark"],
           ["A) Green", "B) Purple", "C) Orange", "D) Brown"],
           ["A) Steve Jobs", "B) Elon Musk", "C) Bill Gates", "D) Mark Zuckerberg"],
           ]
        

def new_game():
    question_num = 0
    guesses = []
    score = 0
    for i in Questions:
        print("----------------------")
        print(i)
        for option in Options[question_num]:
            print(option)
        guess = input("What is your answer?: ").upper()
        guesses.append(guess)
        score += check_answer(Questions[i],guess)
        question_num +=1
    return score, guesses    
            

        
def check_answer(answer,guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0
    
    
def display_score(answer, guesses):
    print("-------------------")
    print("RESULTS")
    print("-------------------")

    print("Answers Key: ", end=" ")
    for i in Questions.values():
        print(i, end=" ")
    print() # Bir alt satıra geçmek için

    print("Your Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()
    score = (answer / len(Questions)) * 100
    print("Success rate: " + str(score) + "%")
   
def play_again():
    cycle = input ("Wanna play again?(Y/N)").upper()
    if cycle != "Y":
        return 0
    else:
        return 1

while True:
    score,guesses = new_game()
    display_score(score,guesses)
    if not play_again():
        break
    

