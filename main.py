import random
print("Play rock paper scissors\nEnter 'r' for rock, 'p' for paper, and 's' for scissors")

# init
W = 0
L = 0
T = 0
i = 0

# game rules
def check():
   if (user_choice == 'r' and comp_choice == 's') or (user_choice == 'p' and comp_choice == 'r') or (user_choice == 's' and comp_choice == 'p'):
       return True
   return False

# game loop
while i < 8:
   user_choice = input("Enter your choice: ")
   comp_choice = random.choice(['r', 'p', 's'])

   if user_choice == comp_choice:
       T += 1
       print("Computer threw " + str(comp_choice) + ", game tied.")
   elif check() is True:
       W += 1
       print("Computer threw " + str(comp_choice) + ", you win.")
   else:
       L += 1
       print("Computer threw " + str(comp_choice) + ", you lose.")
   i += 1
   record = "Wins: " + str(W) + ", Losses: " + str(L) + ", Ties: " + str(T)
   print(record)
