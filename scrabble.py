# Scrabble
# Author: Prajjwal

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


WORDLIST_FILENAME = "words.txt"

def loadWords():
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
   
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def getWordScore(word, n):
 
    word = list(word)
    sum=0
    word1 = SCRABBLE_LETTER_VALUES
    for letter in word:
        sum+=word1[letter]
    score=len(word)*sum
    if (n==len(word)):
        score+=50
    return score

def displayHand(hand):
  
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       
    print()                            

def dealHand(n):
    
    hand={}
    numVowels = n // 3

    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(numVowels, n):
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand


def updateHand(hand, word):
    handCopy = hand.copy()
    for letter in range(len(word)):
       if (word[letter] in handCopy.keys()) and (handCopy[word[letter]] > 0):
           handCopy[word[letter]] -= 1

    return handCopy

def isValidWord(word, hand, wordList):
    handCopy=hand.copy()
    for letter in range(len(word)):
        if (word[letter] in handCopy.keys()) and word[letter]!='' and (handCopy[word[letter]] > 0):
            handCopy[word[letter]] -= 1
        else:
            return False
    if word in wordList:
        return True

def calculateHandlen(hand):
    sum=0
    for v in hand:
        sum+=(hand[v])
    return (sum)


def playHand(hand, wordList, n):
    Score=0
    while(calculateHandlen(hand) > 0):
        print("Current Hand:",end='')
        displayHand(hand)

        word = input('Enter word, or a "." to indicate that you are finished: ')

        if (word == '.'):
            break

        else:
            word1=word.lower()
            if not isValidWord(word1,hand,wordList):
                print("Invalid word, please try again.")
                print('')

            else:
                wordScore = getWordScore(word1,n)
                Score += wordScore
                print("\"" + " "+ word + " "+"\"" + " earned " + str(wordScore) + " points .Total: " + str(Score) + " points " )
                print('')
                hand = updateHand(hand,word1)

        if (calculateHandlen(hand) == 0):
            break

    if (calculateHandlen(hand) == 0):
        print("Run out of letters. Total score:  "+str(Score)+"  points.")
    else:
        print("Goodbye! "+ "Total score: " + str(Score))

def playGame(wordList):
    
    hand = {}
    flag = False
    while(not flag):
        user_inp = input("Enter n to deal a new hand, r to replay the last hand, or e to end game:")
        if user_inp =='n':
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
        elif user_inp == 'r':
            if (len(hand)!=0):
                playHand(hand, wordList,HAND_SIZE)
            else:
                print("You have not played a hand yet. Please play a new hand first!")
        elif user_inp == 'e':
            flag=True
        else:
            print("Invalid command")
        

if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
