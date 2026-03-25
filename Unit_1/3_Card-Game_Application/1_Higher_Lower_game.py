"""
Higher or Lower Card Game
------------------------

This program implements a simple command-line card game using object-oriented programming.

Overview:
    The player starts with a set number of credits and is shown a card from a shuffled deck.
    They must guess whether the next card will be higher or lower in value. If the guess is
    correct, the player wins credits; otherwise, they lose credits. The game continues until
    the player runs out of credits or the deck is empty.

Classes used:
    Card:
        Represents a single playing card.
        Stores rank (e.g., Ace, King), suit (e.g., Hearts), and value (numeric).
        Cards can be concealed or revealed, which controls how they are displayed.

    Deck:
        Manages a collection of Card objects.
        Creates a full deck based on a rank-value dictionary.
        Supports shuffling, drawing cards, and returning cards to the deck.
        Maintains two lists:
            - startingDeckList: the original ordered deck
            - playingDeckList: the active shuffled deck used during gameplay

    Game:
        Controls the overall game logic.
        Handles player credits, betting, user input, and win/loss conditions.
        Uses the Deck class to draw and compare cards.

Key Concepts Demonstrated:
    - Classes and objects
    - Constructors (__init__)
    - Magic methods (__str__)
    - Encapsulation (methods controlling state like reveal/conceal)
    - Composition (Game "has a" Deck, Deck "has many" Cards)
    - Input validation and control flow

How to Run:
    Run the script and follow the prompts in the terminal.
    Enter a bet and guess whether the next card will be higher (h) or lower (l).

Note:
    The `window` parameter in the Card and Deck classes is reserved for potential
    future GUI integration but is not used in this version of the program.
"""

import random

class Card:
    def __init__(self, window, rank, suit, value):
        """
        This defines the Card class, which represents a single card in the deck with its rank, suit, and value.

        The `window` parameter can be used for GUI integration later
        """
        self.rank = rank
        self.suit = suit
        self.value = value
        self.window = window

        self.is_concealed = True


    def __str__(self):
        """
        Returns the card object (i.e. Ace of Hearts) if card not concealed or a message saying such if it is
        """
        if not self.is_concealed:
            return f"{self.rank} of {self.suit}"
        else:
            return "Card is concealed"

    def reveal(self):
        # This method reveals the card by setting `is_concealed` to False.
        self.is_concealed = False

    def conceal(self):
        # This method conceals the card by setting `is_concealed` to True.
        self.is_concealed = True


class Deck:
    """
    This class generates a deck of cards by calling the card object.

    We have the ability to generate multiple decks by passing in values used (i.e. we only use cards higher than 6 for certain games)
    """

    # These are class variables that apply to any deck object generated from this class
    SUIT_TUPLE = ('Diamonds', 'Clubs', 'Hearts', 'Spades')
    STANDARD_DECK = {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                     '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                     'Jack': 11, 'Queen': 12, 'King': 13}


    def __init__(self, window, deck_type = STANDARD_DECK):
        # The constructor initializes the deck by creating cards for each suit and rank using the given rank-value dictionary.
        self.startingDeckList = [] # The startingDeckList holds the original unshuffled deck, which allows resetting the deck if needed.
        self.playingDeckList = []  # The playingDeckList is the active deck used during gameplay, which can be shuffled and modified.

        # Generate the deck by calling the card object for each rank and value in the class variable list
        for suit in Deck.SUIT_TUPLE:
            for rank, value in deck_type.items():
                oCard = Card(window, rank, suit, value)
                self.startingDeckList.append(oCard)

        pass # call a method to separate playing deck from starting decks and shuffle the generated deck

    def shuffle(self):
        # This method shuffles the deck and ensures all cards are concealed before shuffling.
        self.playingDeckList = self.startingDeckList.copy() # Copy the deck list
        for oCard in self.playingDeckList:
            oCard.conceal()
        random.shuffle(self.playingDeckList)


    def get_card(self):
        # This method removes and returns the top card from the playing deck. Raises an error if no cards are left.
        pass


    def return_card_to_deck(self, oCard):
        # This method adds a card back to the top of the playing deck.
        pass


class Game:
    def __init__(self):
        # The Game class handles the game logic, including initializing the deck and managing the score.

        pass  # Pass "None" for window as we are not using GUI
        pass  # Starting credits for the player


    def get_bet(self):
        """
        Validates the bet.

        Returns the bet amount or a message saying the bet is invalid
        """
        pass


    def start_game(self):
        """
        This method runs the game logic during the game.
        It manages checking if there is enough cards, revealing cards, checking bets, calculating credits, and ending the game.
        """
        print("Welcome to the Higher or Lower Card Game!")
        print(f"The first card is: {self.current_card}\n")

        while True:
            pass # Check if there is any cards left first


            pass # Check if there is any credits left


            pass # Place bet


            pass # Validate input to only allow 'h' or 'l'

                pass # Start loop over of invalid input




            # Check if correct guess and adjust winnings (credit amount)
            pass

            pass # Get the next card

        # Show final result
        pass # Currently will only show 0 because this is displayed only when credits reach 0



if __name__ == "__main__":
    pass # Create a game object
    pass # Run the game
