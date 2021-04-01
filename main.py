# Importing Modules
from termcolor import colored
from os import system
from time import sleep
from random import randrange

# Logo & Start-up Menu
print("██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗  "+colored("██████╗ ██████╗ ███████╗", "red"))
print("██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║  "+colored("██╔══██╗██╔══██╗██╔════╝", "yellow"))
print("██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║  "+colored("██████╔╝██████╔╝███████╗", "green"))
print("██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║  "+colored("██╔══██╗██╔═══╝ ╚════██║", "cyan"))
print("██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║  "+colored("██║  ██║██║     ███████║", "blue"))
print("╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝  "+colored("╚═╝  ╚═╝╚═╝     ╚══════╝", "magenta"))

# List of possible answers
answers = ["1", "rock", "roc", "ro", "r", "2", "paper", "pape", "pap", "pa", "p", "3", "scissors", "scissor", "scisso", "sciss", "scis", "sci", "sc", "s"]

# Renaming 1, 2, 3 to Rock, Paper, Scissors
rpsDict = {
  "1": "Rock",
  "2": "Paper",
  "3": "Scissors"
}

# Ascii Art for each Rock, Paper, and Scissors
asciiDict = {
  "1": """    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
  "2": """     _______
---'    ____)____
          ______)
          _______)
        _______)
---.__________)
""",
  "3": """   ________
---'   ____)____
          ______)
      __________)
      (____)
---.__(___)
"""
}



# Clearing Screen after menu
sleep(2)
system("clear")

# Setting scores to 0 for default
pScore = 0
cScore = 0
score1 = 0
score2 = 0

options = input("Would you like to play 1-Player or 2-Player?: ")

def tri():

  system("clear")
  options = input("Would you like to play 1-Player or 2-Player?: ")

  if options in ["1", "1-player", "1p", "1player"]:

    system("clear")

    # Input for username
    name = input("What is your username?: ")
    system("clear")

    while True:

      # Tie function; 0 score added
      def tie():
        print("You tied with the computer.\n")
        global pScore
        global cScore
        pScore+=0
        print(name+": "+str(pScore)+" | Computer: "+str(cScore))

      # Won function; +1 score added to player
      def won():
        print(name+" won!\n")
        global pScore
        global cScore
        pScore+=1
        print(name+": "+str(pScore)+" | Computer: "+str(cScore))

      # Lost function; +1 score added to computer
      def lost():
        print("The computer won!\n")
        global cScore
        global pScore
        cScore+=1
        print(name+": "+str(pScore)+" | Computer: "+str(cScore))

      # Input for rock/paper/scissors for the user
      choice = input("[PLAYER 1] Enter your choice:\n 1. Rock\n 2. Paper\n 3. Scissors\n")

      while choice not in answers:
        # Sets the choice to a number for ease of use. 1 = Rock
        if(choice.lower() in ["1", "rock", "roc", "ro", "r"]):
          choice = 1
          break

        # Sets the choice to a number for ease of use. 2 = Paper
        elif(choice.lower() in ["2", "paper", "pape", "pap", "pa", "p"]):
          choice = 2
          break

        # Sets the choice to a number for ease of use. 3 = Scissors
        elif(choice.lower() in ["3", "scissors", "scissor", "scisso", "sciss", "scis", "sci", "sc", "s"]):
          choice1 = 3
          break

        else:
          system("clear")
          choice1 = input("[PLAYER 1] Enter your choice:\n 1. Rock\n 2. Paper\n 3. Scissors\n")

      # Gets a random option for the computer.
      bot = randrange(1,3)

      # Clears screen after user inuts their choice
      system("clear")

      # Displaying computer choice with ASCII art
      print("The computer chose",rpsDict[str(bot)])
      print(asciiDict[str(bot)])

      # Displaying user choice with ASCII art
      print(name+" chose",rpsDict[str(choice)])
      print(asciiDict[str(choice)])

      # Win & Lose Functions for Rock
      if(int(bot) == 1):
        if(int(choice) == 1):
          tie()
        elif(int(choice) == 2):
          won()
        elif(int(choice) == 3):
          lost()

      # Win & Lose Functions for Paper
      elif(int(bot) == 2):
        if(int(choice) == 1):
          lost()
        elif(int(choice) == 2):
          tie()
        elif(int(choice) == 3):
          won()

      # Win & Lose Functions for Scissors    
      elif(int(bot) == 3):
        if(int(choice) == 1):
          won()
        elif(int(choice) == 2):
          lost()
        elif(int(choice) == 3):
          tie()

      # Waiting for the user to press enter to restart. 
      input('\nPress Enter to continue.')

      # Clearing screen after every restart.
      system("clear")

  elif options in ["2", "2-player", "2p", "2player"]:

    system("clear")

    player1 = input("Player 1 Name: ")
    system("clear")

    player2 = input("Player 2 Name: ")
    system("clear")

    while True:

      choice1 = input("[PLAYER 1] Enter your choice:\n 1. Rock\n 2. Paper\n 3. Scissors\n")

      while choice1 not in answers:
        # Sets the choice to a number for ease of use. 1 = Rock
        if(choice1.lower() in ["1", "rock", "roc", "ro", "r"]):
          choice1 = 1
          break

        # Sets the choice to a number for ease of use. 2 = Paper
        elif(choice1.lower() in ["2", "paper", "pape", "pap", "pa", "p"]):
          choice1 = 2
          break

        # Sets the choice to a number for ease of use. 3 = Scissors
        elif(choice1.lower() in ["3", "scissors", "scissor", "scisso", "sciss", "scis", "sci", "sc", "s"]):
          choice1 = 3
          break

        else:
          system("clear")
          choice1 = input("[PLAYER 1] Enter your choice:\n 1. Rock\n 2. Paper\n 3. Scissors\n")

      system("clear")

      choice2 = input("[PLAYER 2] Enter your choice:\n 1. Rock\n 2. Paper\n 3. Scissors\n")

      while choice2 not in answers:
        # Sets the choice to a number for ease of use. 1 = Rock
        if(choice2.lower() in ["1", "rock", "roc", "ro", "r"]):
          choice2 = 1
          break

        # Sets the choice to a number for ease of use. 2 = Paper
        elif(choice2.lower() in ["2", "paper", "pape", "pap", "pa", "p"]):
          choice2 = 2
          break

        # Sets the choice to a number for ease of use. 3 = Scissors
        elif(choice2.lower() in ["3", "scissors", "scissor", "scisso", "sciss", "scis", "sci", "sc", "s"]):
          choice2 = 3
          break
        else:
          system("clear")
          choice2 = input("[PLAYER 2] Enter your choice:\n 1. Rock\n 2. Paper\n 3. Scissors\n")
        

      system("clear")

      # Displaying computer choice with ASCII art
      print(player1+" chose",rpsDict[str(choice1)])
      print(asciiDict[str(choice1)])

      # Displaying user choice with ASCII art
      print(player2+" chose",rpsDict[str(choice2)])
      print(asciiDict[str(choice2)])

      score1 = 0
      score2 = 0

      # Tie function; 0 score added
      def tie():
        print("Tie!\n")
        global score1
        global score2
        score1+=0
        print(player1+": "+str(score1)+" | "+player2+": "+str(score2))

      # Won function; +1 score added to player
      def won():
        print(player1+" won!\n")
        global score1
        global score2
        score1+=1
        print(player1+": "+str(score1)+" | "+player2+": "+str(score2))

      # Lost function; +1 score added to computer
      def lost():
        print(player2+" won!\n")
        global score1
        global score2
        score2+=1
        print(player1+": "+str(score1)+" | "+player2+": "+str(score2))

        # Win & Lose Functions for Rock
      if(int(choice1) == 1):
        if(int(choice2) == 1):
          tie()
        elif(int(choice2) == 2):
          lost()
        elif(int(choice2) == 3):
          won()

      # Win & Lose Functions for Paper
      elif(int(choice1) == 2):
        if(choice2 == 1):
          won()
        elif(int(choice2) == 2):
          tie()
        elif(int(choice2) == 3):
          lost()

      # Win & Lose Functions for Scissors    
      elif(int(choice1) == 3):
        if(int(choice2) == 1):
          lost()
        elif(int(choice2) == 2):
          won()
        elif(int(choice2) == 3):
          tie()

      input("\nPress Enter to Continue")

      system("clear")

tri()

while options not in ["1", "1-player", "1p", "1player", "2", "2-player", "2p", "2player"]:
  tri()

