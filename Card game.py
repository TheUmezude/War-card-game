# In this program, a 'War card game' is created on backend.
# To do this, properly, we would be creating three classes.
# A card class that handles all the card information (suit-name and rank)
# A deck class
# A player class
# A values dictionary -- as a global dictionary variable
# A suits-name tuple (so that it is non editable) -- as a global tuple
# A ranks tuple (so that it is also non-editable) -- as a global tuple

import random

suits = ('hearts', 'diamonds', 'clubs', 'spades')

ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
         'ten', 'jack', 'queen', 'king', 'ace')

values = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
          'nine': 9, 'ten': 10, 'jack': 11, 'queen': 12, 'king': 13, 'ace': 14}


# Class for getting the information of the cards and analyzing them.
class Card:

    def __init__(self, suit, rank):
        if type(suit) != str or type(rank) != str:
            raise TypeError('Two items, \'suit\' and \'rank\' have to be entered as strings')
        self.suit = suit.lower()
        self.rank = rank.lower()
        self.value = values[self.rank]

    # Adding a string-output here,
    # in-case information on the cards needs to be gotten
    def __str__(self):
        return f"Card: {self.rank.capitalize()} of {self.suit.capitalize()}."


# The Deck class should create all 52 card objects and hold them
# Hold as a list of card objects
# Shuffle the deck
# Deal cards from the deck object
class Deck:

    def __init__(self):
        self.all_cards = list(range(0, 52))  # to hold all the cards
        # self.card_variables = list(range(0, 52))
        pockets = 0

        for items in range(0, len(suits)):
            for rankings in range(0, len(ranks)):
                # I'm gonna use a class within a class -- The deck cards are instances of the card class
                self.all_cards[pockets] = Card(suits[items], ranks[rankings])
                pockets += 1

    def shuffle_deck(self):  # You don't need to return anything because shuffle is happening in place.
        random.shuffle(self.all_cards)
        # If I print out the cards before running the 'shuffle_deck' function, they would print out normally.
        # If I print after the shuffle function, cards print out shuffled.

    def deal_one(self):  # For dealing out one card at a time
        return self.all_cards.pop()


class Player:

    def __init__(self, name):
        self.name = name
        self.entire_cards = []

    def remove_one(self):
        # We have to specify that the card we intend to remove occurs at the index 0 -- i.e, top of the card deck
        return self.entire_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == list:
            self.entire_cards.extend(new_cards)  # extend is used because we can't append a list to another list

        else:
            self.entire_cards.append(new_cards)  # append is used because we can't extend by a non-iterable aspect

    def __str__(self):
        return f"Player {self.name} has {len(self.entire_cards)} cards."


# Game Logic begins here.
# Create players

player_one = Player('One')  # instance of the Player class
player_two = Player('Two')  # instance of the Player class

# Create a new deck
new_deck = Deck()  # instance of the Deck class. Now new_deck has an object called 'all_cards' which creates all 52 cards
# Shuffle the deck of cards to begin the game
new_deck.shuffle_deck()
# print(len(new_deck.all_cards))

# Deal cards to each player
for items in range(0, 26):
    player_one.add_cards(new_deck.deal_one())  # Taking cards from the 52 cards in new_deck, and instance of Deck
    player_two.add_cards(new_deck.deal_one())  # Taking cards from the 52 cards in new_deck, an instance of deck

# print(len(player_one.entire_cards))
# print(len(player_two.entire_cards))

# Now, player_one and player_two both have 26 cards, each.

game_on = True
round_num = 0

while game_on == True:
    round_num += 1
    print(f"Game-play: Round {round_num}")

    if len(player_one.entire_cards) == 0:
        print(f"Player {player_one.name} is out of cards! Player {player_two.name} WINS!")
        game_on = False
        break

    elif len(player_two.entire_cards) == 0:
        print(f"Player {player_two.name} is out of cards! Player {player_one.name} WINS!")
        game_on = False
        break

    # start a new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    # Start war
    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:
            # We take all the cards on the table, both for player 1 and 2 - whether cards are list or single cards
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False

        elif player_two_cards[-1].value > player_one_cards[-1].value:
            # We take all the cards on the table, both for player 1 and 2 - whether cards are list or single cards
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)
            at_war = False

        else:
            print('\nWe have a war!!!\n')

            if len(player_one.entire_cards) < 3:
                print(f'Player {player_one.name} is unable to declare a war.')
                print(f'Player {player_two.name} WINS!!')
                game_on = False
                break

            elif len(player_two.entire_cards) < 3:
                print(f'Player {player_two.name} is unable to declare a war.')
                print(f'Player {player_one.name} WINS!!')
                game_on = False
                break

            else:
                for items in range(0, 3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

                if player_one_cards[-1].value > player_two_cards[-1].value:
                    # We take all the cards on the table, both for player 1 and 2 - list or single cards
                    player_one.add_cards(player_one_cards)
                    player_one.add_cards(player_two_cards)
                    at_war = False

                elif player_two_cards[-1].value > player_one_cards[-1].value:
                    # We take all the cards on the table, both for player 1 and 2 - list or single cards.
                    player_two.add_cards(player_two_cards)
                    player_two.add_cards(player_one_cards)
                    at_war = False





