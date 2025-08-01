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

List1=[rock,paper,scissors]

x=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if x == 0:
    print(f"User Chose: {List1[0]}")
elif x == 1:
    print(f"User Chose: {List1[1]}")
else:
    print(f"User Chose: {List1[2]}")
    
import random   
n=len(List1)
rand=random.randint(0,n-1)
print(f"Computer Chose: {List1[rand]}")

if x>=2 or x<0:
    print("You typed an invalid number, you lose!")

elif rand>x:
    print("Computer Wins")

elif rand<x:
    print("User Wins")

else:
    print("Draw")