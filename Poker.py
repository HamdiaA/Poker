#Assignment #1
#Hamdia Abdulhafiz Abdullahi

'''
EXAMPLES OF TEST RUNS (ALL TYPES OF HANDS):

#general test cases left, 

TdJdQdKdAd
Royal Flush <--

3d4d5d6d7d     
Straight FLush  <-

TcTsThTd2s
Four of a Kind

3d3s3c8s8c
Full House

2s4s6sTsQs
Flush    

3s4d5s6h7c
Straight    

Ah6c6s3c6h
Three of a Kind    

4s8d8hJcJs
Two Pair    

7h7h6s9h3c
Pair    

4sJh7dKc9s
K high    
'''

import random 

rank = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'] #list with all the ranks
suit = ['c', 'd', 'h', 's'] #list with all the suits

counter = 1
randomHand = ''

while counter <= 10 : #generates a random hand each time
    cardRank = random.choice(rank) #picks a random rank
    cardSuit = random.choice(suit) #picks a random suit
    
    if counter % 2 == 1 : #adds a random rank to the hand at an odd index
        randomHand = randomHand + cardRank #random rank added to hand
    else: #adds a random suit to the hand at an even index
        randomHand = randomHand + cardSuit #random suit added to hand
    counter = counter + 1

def evaluate(hand):
    new = []
    newStrt = []
    rank = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'] #list with all the ranks
    handType = ''
    c, d, h, s = 'c', 'd', 'h', 's' #suits
    clubCount, diamondCount, heartCount, spadesCount = 0, 0, 0, 0 #number of cards with each suit

    if c in hand or d in hand or h in hand or s in hand: #count how many cards have each suit
        clubCount = hand.count(c)
        diamondCount = hand.count(d)
        heartCount = hand.count(h)
        spadesCount = hand.count(s)

    #1 - ROYAL FLUSH (5 highest cards, T, J, Q, K, A, with all the same suit)
    if (clubCount == 5 or diamondCount == 5 or heartCount == 5 or spadesCount == 5):
        if ('T' in hand and 'J' in hand and 'Q' in hand and 'K' in hand and 'A' in hand): #if there are 5 cards or any suit then
            handType = 'Royal Flush'
            return handType #this hand is a royal flush

    #2 - STRAIGHT FLUSH (5 card straight, all in the same suit)
        elif (('5' in hand and ('4' in hand or '6' in hand)) or ('T' in hand and ('9' in hand or 'J' in hand))):        
                for i in hand:
                    if hand.index(i) % 2 == 0 : #for every rank (even index)
                        if type(int(i)) == int and int(i) >= 2 and int(i) <= 9:
                            new.append(int(i))
                        else:
                            case = {
                                i == 'T' : new.append(10),
                                i == 'J' : new.append(11),
                                i == 'Q' : new.append(12),
                                i == 'K' : new.append(13),
                                i == 'A' : new.append(1),
                            }
                            case[i]()
                    new.sort()
                    newStrt = list(range(min(new), max(new)+1))

                    for i, rank in enumerate(newStrt):
                        case = {
                                rank == 10 : newStrt[i] == 'T',
                                rank == 11 : newStrt[i] == 'J',
                                rank == 12 : newStrt[i] == 'Q',
                                rank == 13 : newStrt[i] == 'K',
                                rank == 1 : newStrt[i] == 'A',
                        }
                    
                if new == newStrt:
                    handType = 'Straight Flush'
                    return handType  #this hand is a straight flush

    #5 - FLUSH (All five cards in hand have the same suit)
        else:
            handType = 'Flush'
            return handType #this hand is a flush

    #3 - FOUR OF A KIND (Four cards with the same rank)
    elif (hand.count(hand[0]) >= 3 or hand.count(hand[2]) >= 3 or hand.count(hand[4]) >= 3 or hand.count(hand[6]) >= 3 or hand.count(hand[8]) >= 3):
        for i in hand:
            if hand.index(i) % 2 == 0 : #for every rank (even index)
                if hand.count(i) == 4 : #if there is exactly four cards with the same rank
                    handType = 'Four of a Kind' #this hand is a four of a kind
                    return handType
    
    #7 - THREE OF A KIND (Three cards with the same rank)
                elif hand.count(i) == 3 : #if there is exactly three cards with the same rank
                    handType = 'Three of a Kind' #this hand is a three of a kind
    #4 - FULL HOUSE (Three cards with the same one rank and the other two cards with another same rank)
                    newHand = hand.replace(i, '') #get rid of the three cards that have the same rank
                    newHand = newHand.replace('s', '') #get rid of all suits in the string
                    newHand = newHand.replace('c', '')
                    newHand = newHand.replace('h', '')
                    newHand = newHand.replace('d', '')
                    
                    if newHand.count(newHand[0]) == 2: #if the last 2 cards have the same rank then
                        handType = 'Full House' #this hand is a full house
        return handType

    #6 - STRAIGHT (Five cards of sequential value. Every possible straight will contain either a 5 or a 10)
    elif (('5' in hand and ('4' in hand or '6' in hand)) or ('T' in hand and ('9' in hand or 'J' in hand))):        
        for i in hand:
            if hand.index(i) % 2 == 0 : #for every rank (even index)
                if i.isdigit() and int(i) >= 2 and int(i) <= 9: #type(int(i)) == int
                    new.append(int(i))
                else:
                    case = {
                        i == 'T' : new.append(10),
                        i == 'J' : new.append(11),
                        i == 'Q' : new.append(12),
                        i == 'K' : new.append(13),
                        i == 'A' : new.append(1),
                    }
                    case[i]()
        new.sort()
        newStrt = list(range(min(new), max(new)+1))
                    
        if new == newStrt:
            handType = 'Straight'
            return handType  #this hand is a straight

    #7 - THREE OF 
#    elif (hand.count(hand[0]) == 3 or hand.count(hand[2]) == 3 or hand.count(hand[4]) == 3 or hand.count(hand[6]) >= 3 or hand.count(hand[8]) >= 3):
#        for i in hand:
#            hand.count(i) == 3 #if there is exactly three cards with the same rank
#            handType = 'Three of a Kind' #this hand is a three of a kind
#           return handType

    #9 - PAIR (One pair of cards with the same rank)
    elif (hand.count(hand[0]) == 2 or hand.count(hand[2]) == 2 or hand.count(hand[4]) == 2 or hand.count(hand[6]) == 2 or hand.count(hand[8]) == 2):
        for i in hand:
            if hand.index(i) % 2 == 0 : #for every rank (even index)
                if hand.count(i) == 2:
                    handType = 'Pair'

    #8 - TWO PAIRS (two pairs of cards with the same rank)
                    newHand = hand.replace(i, '') #get rid of the three cards that have the same rank
                    newHand = newHand.replace('s', '') #get rid of all suits in the string
                    newHand = newHand.replace('c', '')
                    newHand = newHand.replace('h', '')
                    newHand = newHand.replace('d', '')
                    
                    if (newHand.count(newHand[0]) == 2 or newHand.count(newHand[1]) == 2 or newHand.count(newHand[2]) == 2): #if the last 2 cards have the same rank then
                        handType = 'Two Pair' #this hand is a full house
                        return handType
        return handType

    #10 - HIGHEST (If none of the types of hands apply then output the card with the highest rank)
    else:
        for element in rank[::-1]:
            if element in hand:
                handType = element + ' high'
                return handType

hand = input('Enter a poker hand: ') #Evaluates poker hand that the user enters
print(evaluate(hand), '\n')

print(randomHand) # EXAMPLE RUN - generates any hand to work in all 6 cases
print(evaluate(randomHand)) #evaluates a randomly generated poker hand

#            if newStrt[i] == 1 or newStrt[i] >= 10 and newStrt[i] <= 13:
#                for i, rank in enumerate(newStrt):
#                    case = {
#                        rank == 10 : newStrt[i] == 'T',
#                        rank == 11 : newStrt[i] == 'J',
#                        rank == 12 : newStrt[i] == 'Q',
#                        rank == 13 : newStrt[i] == 'K',
#                        rank == 1 : newStrt[i] == 'A',
#                        rank >= 2 and rank <=9 : newStrt[i] == rank,
#                    }