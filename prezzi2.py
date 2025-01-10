import random
import json
import collections
import os.path

AUTH_PASSWORD = '7 of spades'
DECKS_FILE = "decks.txt"

decks = []

def authorization():
    password = None
    while password != AUTH_PASSWORD:
        password = input("What is the password? ")

def save_decks():
    with open(DECKS_FILE, 'w') as file:
        json.dump(decks, file)

def load_decks():
    global decks
    if os.path.exists(DECKS_FILE) and os.path.getsize(DECKS_FILE) > 0:
        with open(DECKS_FILE, 'r') as file:
            decks = json.load(file)
    else:
        decks = []

def start():
    print("""
    Hi! Welcome to Your Own Personal Card Deck Chooser,

    What would you like to do?
    a) Add a card deck
    b) Remove a card deck
    c) List your personal card decks
    d) Choose a random card deck
    """)

    choice = input("Please choose an option (a/b/c/d): ").lower()

    if choice == 'a':
        deck_name = input("What deck you would like to add: ")
        decks.append(deck_name)
        save_decks()
        print("Deck " + deck_name + " has been added :D ")
        restart = input("Would you like to start again? (y/n) ")
        if restart == 'y':
            start()
        else:
            print("No worries, have a brilliant day! ")
            
    elif choice == 'b':
        deck_name_remove = input("What deck you would like to remove: ")
        if deck_name_remove in decks:
            decks.remove(deck_name_remove)
            save_decks()
            print("Your deck was removed successfully :)")
            restart = input("Would you like to start again? (y/n) ")
            if restart == 'y':
                start()
            else:
                print("No worries, have a fantastic day! ")
        else:
            print("That deck is not in your deck list : " + (deck_name_remove) + " .")
            restart = input("Would you like to start again? (y/n) ")
            if restart == 'y':
                start()
            else:
                print("No worries, have a bewildering day! ")
            
    elif choice == 'c':
        print("Your saved decks are: " +  ", ".join(decks))
        restart = input("Would you like to start again? (y/n) ")
        if restart == 'y':
            start()
        else:
            print("No worries, have a good day! ")
            
    elif choice == 'd':
        if decks:
            random_deck = random.choice(decks)
            print("Your card deck is: " + random_deck)
            restart = input("Would you like to start again? (y/n) ")
            if restart == 'y':
                start()
            else:
                print("No worries, have a amazing day! ")            
        else:
            print("You haven't added any decks yet!")
            restart = input("Would you like to start again? (y/n) ")
            if restart == 'y':
                start()
            else:
                print("No worries, have a astounding day! ")  
    else:
        print("You didn't select valid letter, please try again.")
        start()
        
load_decks()
authorization()
start()
