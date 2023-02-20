import random

#print a welcome for the user and invite them to play
print("Welcome to Hangman!")
name = input("What's your name? ")
print(f"Hello {name}!")
print("-------------------------------------------")

"""
easy, medium and hard difficulty selection for users that increases 
letter count of the words to increase difficulty
"""
difficulty = input("Please select the difficulty level\n easy - 6 Letter words,\n medium - 7 Letter words,\n hard - 8 Letter words):\n ")
while difficulty not in ['easy', 'medium', 'hard']:
  print("Invalid input. Please select a valid difficulty level.")
  difficulty = input("Please select the difficulty level (easy, medium, or hard): ")

"""
chooses a word dictionary based on the users selected difficulty 
"""
if difficulty == 'easy':
  wordDictionary = ["pickax", "whacky", "quacks", "boozey", "joyful", "chubby", "enzyme", "hotdog", "cheese", "jacket"]
elif difficulty == 'medium':
  wordDictionary = ["buzzcut", "qualify", "salvage", "sunbeam", "reading", "witness", "stencil", "costume", "grimace", "serving"]
else:
  wordDictionary = ["illusion", "teaching", "policies", "exorcist", "stumbled", "invested", "pregnant", "hydrated", "tapestry", "remarked"]