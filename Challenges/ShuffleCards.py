import random
def shuffle(card,n) :

    # Initialize seed randomly
    for i in range(n-1, 0, -1):
        r = (random.randint(0,i+1))
        tmp=card[i]
        card[i]=card[r]
        card[r]=tmp
    return card

def shuffleAlt(card, n):
    for i in range(n):
        r = i + (random.randint(0,75) % (52 -i))
        tmp=card[i]
        card[i]=card[r]
        card[r]=tmp
    return card

def checkDuplicate(card):
    b = [None]*52
    for i in range(len(card)):
        n = card[i]
        if b[n]:
            return False
        b[n] = True

    return True


#Driver code
if __name__=='__main__':
    a=[0, 1, 2, 3, 4, 5, 6, 7, 8,
       9, 10, 11, 12, 13, 14, 15,
       16, 17, 18, 19, 20, 21, 22,
       23, 24, 25, 26, 27, 28, 29,
       30, 31, 32, 33, 34, 35, 36,
       37, 38, 39, 40, 41, 42, 43,
       44, 45, 46, 47, 48, 49, 50,
       51]
    card = shuffleAlt(a, 52)
    print("cards: ",card)
    print(checkDuplicate(card))
