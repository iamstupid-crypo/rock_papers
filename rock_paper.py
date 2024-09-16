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
game_images=[rock, paper, scissors]
user_choice=int(input("what do u choose? type 0 for Rock,1 for paper or 2 for scissor\n"))
print(game_images[user_choice])
#0,1,2
computer_choice=random.randint(0,2)
print(f"computer chose {computer_choice}")
print(game_images[computer_choice])
if user_choice==0 and computer_choice==2:
    print("you win!")

elif computer_choice==0 and user_choice==2:
    print("you lose!")
elif user_choice >= 3 or user_choice < 0:
    print("you typed an invalid number. you lose!")
elif computer_choice>user_choice:
    print("you lose :(")
elif computer_choice<user_choice:
    print("you win")
elif computer_choice==user_choice:
    print("it's a draw!")

