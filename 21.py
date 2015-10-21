import random

cards = {}

def deck():
	x = 1
	#cards = {}
	index = 0
	suits = ["Clubs", "Hearts", "Diamonds", "Spades"]
	
	while x <= 14:
		for suit in suits:
			if x < 11:
				cards["{} of {}".format(x, suit)] = x 
			elif x == 11:
				cards["Jack of {}".format(suit)] = 10
			elif x == 12:
				cards["Queen of {}".format(suit)] = 10
			elif x == 13:	
				cards["King of {}".format(suit)] = 10
			elif x == 14:
				cards["Ace of {}".format(suit)] = 1
		x += 1


	return cards


def play():
	deck()
	player_cards = []

	print "Here are you first 2 cards"


def player_score():
	pcard1 = random.choice(cards.keys())
	del cards[pcard1]
	pcard2 = random.choice(cards.keys())
	del cards[pcard2]

	print pcard1
	print pcard2

	ptotal = pcard1 + pcard2

	while True:
		print "Your total is {}...".format(total)
		if ptotal = 21:
			break
		elif ptotal < 21:
			n = raw_input(Would you like to draw another card?)
			if n.upper() in ("Y, YES")
				pcard3 = random.choice(cards.keys())
				del cards[pcard3]
				ptotal = ptotal + pcard3
		else:
			break

	return ptotal

def dealer():
	dcard1 = random.choice(cards.keys())
	del cards[dcard1]
	dcard2 = random.choice(cards.keys())
	del cards[dcard2]

	dtotal = dcard1 + dcard2

def dealer_rules(dtotal):
	if dtotal = 21

play()

