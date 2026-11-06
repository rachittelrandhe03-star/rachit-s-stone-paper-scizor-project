#ok so it is the third time i am doing this same project and now lets build the logic by ourselves

import random

dict = {
    "s" : "snake",
    "sc" : "scissor",
    "p" : "paper",   
}
print("HEY YOU ALL WELCOME TO STONE PAPER SCISSOR GAME...")
print("INSTRUCTION:\n1)if you want to enter stone please enter sc\n2)if you want to enter paper enter p\n3)if you want to enter stone enter s")

user_choice=input("please enter the choice here after thouroughly reading all the information:").strip().lower()

computer_choice =random.choice(["s","sc","p"])

if((user_choice=="s" and computer_choice=="s")
   or
   (user_choice=="sc"and computer_choice=="sc") 
   or
   (user_choice=="p" and computer_choice=="p")
):
    print(f"you choose {dict[user_choice]} and the computer choice is {dict[computer_choice]} then there is a tie")
    
elif(
    user_choice=="s" and computer_choice=="sc" or
    user_choice=="p" and computer_choice=="s" or
    user_choice=="sc" and computer_choice=="p"
):
    print(f"you choose {dict[user_choice]} and the computer choice is {dict[computer_choice]} then you win the game \n congratulations")
    
elif(
    user_choice=="sc" and computer_choice=="s" or
    user_choice=="s" and computer_choice=="p" or
    user_choice=="p" and computer_choice=="sc"
):
    print(f"you choose {dict[user_choice]} and the computer choice is {dict[computer_choice]} then you lost the game \n better luck next time...!")
    
else:
    print("please enter the valid input")
    
print("thank you for playing the game.....")
    
                               
