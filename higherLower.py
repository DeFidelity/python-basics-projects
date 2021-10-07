import random
from higherLowerArt import logo
from higherLowerArt import vs
from higherLowerData import data

def compare1():
    """it pick out a value from the datafile"""
    follower = []
    more = data[random.randint(0,len(data) - 1)]
    follower.append(more['follower_count'])
    print(f"{more['name']} a  {more['description']} from  {more['country']} ")
    return follower
def higher(first_index, second_index):
    huge = 0
    high = 0
    for val in first_index:
        huge += val
    for val in second_index:
        high += val
    if huge > high:
        print(huge)
        return huge
        
    else:
        print(high)
        return high
endgame = True
score = 0
# print logo
while endgame:
    print(logo)
    # print random value from the data file
    first_index = compare1()
    print(first_index)

    #print vs logo
    print(vs)
    # print another random value the data from the file
    second_index = compare1()
    print(second_index)
    # ask who has more followers
    higher(first_index, second_index)

    #ask to answer with a or b
    mumu = print(input("who has more instagram followers, type 'a' or 'b': "))

    if mumu == 'a':
        mumu = str(first_index)
    else:
        mumu = second_index
    if mumu == higher(first_index, second_index):
        score += 1
        print(score)
    else:
        endgame = False
        print(endgame)
    


# if the chosen is greater than the other add score plus 1
# compare the chosen with the next value
# if the chosen is wrong end game
# it should continue provided that its right
# it stops when its over and ask if it would like to play again
