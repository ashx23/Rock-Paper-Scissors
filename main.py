import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
gameimages = [rock, paper, scissors]
userchoice = int(input("What do you choose? Type 0 for Rock, type 1 for paper, type 2 for scissors \n"))

if userchoice >= 3 or userchoice < 0:
 print("You typed invalid number you lose")

else:

  print(gameimages[userchoice])  
  
  computerchoice = random.randint(0,2)
  print("Computer chose ")
  print(gameimages[computerchoice])
  
  
  if userchoice == 0 and computerchoice == 2:
    print("You Win!")
  elif computerchoice == 0 and userchoice == 2 :
    print("You lose!")
  elif computerchoice > userchoice:
    print("You lose!")
  elif userchoice > computerchoice:
    print("You Win!")
  elif computerchoice == userchoice:
    print("Its a draw.")

  

