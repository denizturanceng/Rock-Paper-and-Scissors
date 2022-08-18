import random
print("Welcome to Rock,Paper and Scissors.\n")
roundCount = 0
myScore=0
computerScore=0
while roundCount!=20:
    print("\nNew round starting...\n")
    print("\n1-Rock\n2-Paper\n3-Scissors")
    
    myChoice=input("Your choice is :")
    
    if myChoice !="1" and myChoice !="2" and myChoice !="3" :
        print("\nInvalid choice, please do it again.")
    else:
        roundCount+=1
        computerChoice = random.choice(["1", "2", "3"])
        
        if myChoice=="1":
            if computerChoice=="1":
                myScore+=1
                computerScore+=1
                print("Computer's choice is {}\n".format(computerChoice))
                print("Rock equals rock. {}.round finished. Result is Draw.\n".format(roundCount))
                print("Computer score:{}".format(computerScore))
                print("User score:{}".format(myScore))
                
            elif computerChoice=="2":
                computerScore+=3
                print("Computer's choice is {}\n".format(computerChoice))
                print("Paper wraps rock. Computer won the {}.round.".format(roundCount))
                print("Computer score:{}".format(computerScore))
                print("User score:{}".format(myScore))
                
            elif computerChoice=="3":
                myScore+=3
                print("Computer's choice is {}\n".format(computerChoice))
                print("Rock breaks scissors. User won the {}.round.".format(roundCount))
                print("Computer score:{}".format(computerScore))
                print("User score:{}".format(myScore))    
                
                
        elif myChoice=="2":
            if computerChoice=="1":
                myScore+=3
                print("Computer's choice is {}\n".format(computerChoice))
                print("Paper wraps rock. User won the {}.round.".format(roundCount))
                print("Computer score:{}".format(computerScore))
                print("User score:{}".format(myScore))
                
            elif computerChoice=="2":                
                myScore+=1
                computerScore+=1
                print("Computer's choice is {}\n".format(computerChoice))
                print("paper equals paper. {}.round finished. Result is Draw.\n".format(roundCount))
                print("Computer score:{}".format(computerScore))
                print("User score:{}".format(myScore))
                
            elif computerChoice=="3":
                computerScore+=3
                print("Computer's choice is {}\n".format(computerChoice))
                print("Scissors cuts paper. Computer won the {}.round.".format(roundCount))
                print("Computer score:{}".format(computerScore))
                print("User score:{}".format(myScore))  
                
            
        elif  myChoice=="3":
            if computerChoice=="1":
                computerScore+=3
                print("Computer's choice is {}\n".format(computerChoice))
                print("Rock breaks scissors. Computer won the {}.round.".format(roundCount))
                print("Computer score:{}".format(computerScore))
                print("User score:{}".format(myScore))
                
            elif computerChoice=="2":                
                myScore+=3
                print("Computer's choice is {}\n".format(computerChoice))
                print("Scissors cuts paper. User won the {}.round\n".format(roundCount))
                print("Computer score:{}".format(computerScore))
                print("User score:{}".format(myScore))
                
            elif computerChoice=="3":
                myScore+=1
                computerScore+=1
                print("Computer's choice is {}\n".format(computerChoice))
                print("Scissors equals scissors. {}.round finished. Result is Draw.\n".format(roundCount))
                print("Computer score:{}".format(computerScore))
                print("User score:{}".format(myScore))  
                

    if roundCount==20:
        if myScore > computerScore:
            print("\nThe game is finished.\n")
            print("Congratilations. You beat the computer after 20 rounds.\n")
            print("Your Score is {} and computer's score is {}".format(myScore,computerScore) )
            exit()
        elif computerScore > myScore:
            print("\nThe game is finished.\n")
            print("Unfortunately, you were beated by computer after 20 rounds.\n")
            print("Computer's Score is {} and your score is {}".format(computerScore,myScore) )
            exit()
        elif myScore == computerScore :
            print("\nThe game is finished.\n")
            print("Result is draw.\n")
            print("Your Score is {} and computer's score is {}".format(myScore,computerScore) )
            exit()
