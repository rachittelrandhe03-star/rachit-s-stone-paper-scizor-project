# OK SO HARRY BHAI INSTRUCTED TO MAKE THE GAME OF SNAKE,WATER,GUN....BUT I AM GOING TO MAKE IT OF STONE PAPER SCIZZOR....

'''
s = stone
sc = scissor
p = paper
'''
import random
dict = {"s":"stone","sc":"scissor","p":"paper"}
print("1)Enter s if you want to choose the stone \n2)Enter sc if you want to choose scissor\n3)Enter p if you want to enter paper")
a = input("please enter your choice :").strip().lower()
computer = random.choice(["s","sc","p"])
if a not in dict:
    print("please enter the valid choice :")
else:
    print(f"you enter {dict[a]} and the computer enter {dict[computer]}" )
    if(
        a=="s" and computer=="sc"or
        a=="sc"and computer=="p"or
        a=="p" and computer=="s"
    ):
        print("you win the game...")
    
    elif computer == a:
        print("its a draw...")
        
    else:
        print("you lose")
    


