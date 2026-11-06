'''
scissor =1
stone=0
paper = -1

'''
import random
print("INSTRUCTION : \n1)if you want to answer stone enter s\n2)if you want to answer paper enter p\n3)if you want to answer SCISSOR enter sc")

user_input=input("please enter your choice :").strip().lower()
dict = {"sc":"scissor","s":"stone","p":"paper"}

computer = random.choice(["s","sc","p"])

if user_input not in dict:
    print("please enter a valid input")
    
else:
    print(f"you choose {dict[user_input]}")
    print(f"and the computer chose {dict[computer]}")
    if user_input == computer:
        print("it's a draw")
    
    elif(
        (user_input =="s" and computer == "sc")or
        (user_input =="p" and computer == "s")or
        (user_input =="sc" and computer == "p")  
    ):
        print("you win")
        
    else:
        print("you lost")

