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

# flips a card from hand
def flip_card(p1_hand, p2_hand):
     p1_card = p1_hand.pop(0)
     p2_card = p2_hand.pop(0)
     
     print(f"Player 1 flipped: {p1_card}")
     print(f"Player 2 flipped: {p2_card}")
     
     return (p1_card, p2_card)

def card_comparison(p1_card, p2_card):
    """This is the logic that compares two cards to find the stronger card
		Return 1 if player 1's card is strong, 2 for player 2
		if the cards are equal, return 0.

		Hint, using the index function will make this very simple (one liner)"""
    if ranks.index(p1_card[0]) > ranks.index(p2_card[0]):
        print("Player 1 has the stronger card")
        return 1
    elif ranks.index(p1_card[0]) < ranks.index(p2_card[0]):
        print("Player 2 has the stronger card")
        return 2
    else:
        print("Both players have equal cards")
        return 0

def play_round(player1_hand, player2_hand):
    """Play a single round of the game.
		That is, each player flips a card, and the winner is determined using the card_comparison function
		if both players flip the same value card, call the war function
	"""
    cards =  flip_card(player1_hand, player2_hand)
    p1_card = cards[0]
    p2_card = cards[1]
    
    comparison_result = card_comparison(p1_card, p2_card)
	
    if comparison_result == 0:
        print("WAR!")
        war(player1_hand, player2_hand)
    
def draw_three_cards(player_hand):
    cards_drawn = []
    
    for i in range(0, 3):
        
        # check if the player still has cards left
        if len(player_hand) > 0:
            cards_drawn.append(player_hand.pop(0))
        else:
            break
    
    return cards_drawn
        
def add_cards_to_hand(player_hand, cards_to_add):
    for card in cards_to_add:
        player_hand.append(card)
    
    return player_hand

def war(player1_hand, player2_hand):
    """Handle the 'war' scenario when cards are equal.
		recall the rules of war, both players put 3 cards face down, 
		then both players flip face up a 4th card. The player with the stronger
		card takes all the cards.		
	"""
    
	# Player 1 draws 3 face down cards
    player1_cards = draw_three_cards(player1_hand)
    
	# check if player_1 had enough cards
    if len(player1_cards) < 3:
        # Player 1 lost
        print("Player 1 lost - not enough cards")
        return
    
    player2_cards = draw_three_cards(player2_hand)
    
	# check if player_2 had enough cards
    if len(player2_cards) < 3:
        # Player 2 lost
        print("Player 2 lost - not enough cards")
        return
    
	# Both players have put down three cards
    # Draw the last card - face up
    
    p1_card = None
    p2_card = None
    
    if len(player1_hand) > 0:
        p1_card = player1_hand.pop(0)
        print(f"Player 1 flipped: {p1_card}")
        
    if len(player2_hand) > 0:
        p2_card = player2_hand.pop(0)
        print(f"Player 2 flipped: {p2_card}")
    
    comparison_result = card_comparison(p1_card, p2_card)
    
    player_cards = player1_cards
    for card in player2_cards:
        player_cards.append(card)
        
    if comparison_result == 1:
        # Player 1 won
        add_cards_to_hand(player1_hand, player_cards)
    elif comparison_result == 2:
        # Player 2 won
        add_cards_to_hand(player2_hand, player_cards)
    elif comparison_result == 0:
        # Draw
        print("WAR!")
        war(player1_hand, player2_hand)
    
    return 
        
    

def play_game():
    """Main function to run the game."""
    # Your code here

# Call the main function to start the game
play_game()
pass