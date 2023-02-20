import random


#print a welcome for the user and invite them to play
print("Welcome to Hangman!")
name = input("What should we call you? ")
print(f"Hello {name}! Let's play")
print("You must complete the game within 6 guesses... OR ELSE!!!")
print("\n+---+")
print(" O   |")
print("/|\  |")
print("/ \  |")
print("    ===")
print("-------------------------------------------")


#add difficulty selection for users that increases the letter count relative to difficulty selected
difficulty = input("Select your preferred difficulty level\n easy - 6 Letter words,\n medium - 7 Letter words,\n hard - 8 Letter words):\n ")
while difficulty not in ['easy', 'medium', 'hard']:
  print("Invalid input. Please select a valid difficulty level.")
  difficulty = input("Please select the difficulty level (easy, medium, or hard): ")


#chooses a word dictionary based on the users selected difficulty 
if difficulty == 'easy':
  word_dictionary = ["pickax", "whacky", "quacks", "boozey", "joyful", "chubby", "enzyme", "hotdog", "cheese", "jacket"]
elif difficulty == 'medium':
  word_dictionary = ["buzzcut", "qualify", "salvage", "sunbeam", "reading", "witness", "stencil", "costume", "grimace", "serving"]
else:
  word_dictionary = ["illusion", "teaching", "policies", "exorcist", "stumbled", "invested", "pregnant", "hydrated", "tapestry", "remarked"]


#chooses a random word from a dictionary based on the players selected difficulty
randomWord = random.choice(word_dictionary)


#prints an underscore to represent the number of letters in a chosen word
for x in randomWord:
  print("_", end=" ")


def print_hangman(wrong):
    """
    Prints a different piece of the hangman character depending on the number of incorrect guesses
    """
    if(wrong == 0):
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 1): 
        print("\n+---+")
        print("O   |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 2):
        print("\n+---+")
        print("O   |")
        print("|   |")
        print("    |")
        print("   ===")
    elif(wrong == 3):
        print("\n+---+")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("   ===")
    elif(wrong == 4):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("    |")
        print("   ===")
    elif(wrong == 5):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/   |")
        print("   ===")
    elif(wrong == 6):
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("/ \  |")
        print("    ===")