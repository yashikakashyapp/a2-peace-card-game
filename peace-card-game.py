# Import necessary modules
import random

# Define the ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

# Create a deck of cards
deck = ((rank, suit) for rank in ranks for suit in suits)
# Shuffle the deck 
random.shuffle(deck)

# Split the deck into two hands
p1_hand = deck[:int(len(deck)/2)] #player 1 gets the first half of the deck
p2_hand = deck[int(len(deck)/2):] #player 2 gets the second half of the deck

# draw crad
def draw_card(p1_hand, p2_hand):
     p1_card = p1_hand.pop(0)
     p2_card = p2_hand.pop(0)
     
     print(f"Player 1 drew: {p1_card}")
     print(f"Player 2 drew: {p2_card}")
     
     return (p1_card, p2_card)

def card_comparison(p1_card, p2_card):
    """This is the logic that compares two cards to find the stronger card
		Return 1 if player 1's card is strong, 2 for player 2
		if the cards are equal, return 0.

		Hint, using the index function will make this very simple (one liner)"""
    # Your code here

def play_round(player1_hand, player2_hand):
    """Play a single round of the game.
		That is, each player flips a card, and the winner is determined using the card_comparison function
		if both players flip the same value card, call the war function
	"""
    # Your code here

def war(player1_hand, player2_hand):
    """Handle the 'war' scenario when cards are equal.
		recall the rules of war, both players put 3 cards face down, 
		then both players flip face up a 4th card. The player with the stronger
		card takes all the cards.		
	"""
    # Your code here

def play_game():
    """Main function to run the game."""
    # Your code here

# Call the main function to start the game
play_game()
