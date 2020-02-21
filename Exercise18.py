import random


def makeNumber():
    number = ""
    for x in range(4):
        number += str((random.randint(0,9)))
    return number

def countCowsAndBulls(guess,number):
    cows = 0
    bulls = 0
    for i in range(4):
        if guess[i] == number[i]:
            cows = cows + 1
        else: 
            bulls = bulls + 1
    return cows,bulls


if __name__ == "__main__":
    numberoftries = 0
    number = makeNumber()
    
    while(True):
        guess = input("Enter your lucky numbers ")
        
        (cows,bulls) = countCowsAndBulls(guess,number)
        
        if (cows == 4) and (bulls == 0):
            print("We have a Winner!! Congrats go get a cookie! :) \n this took you",numberoftries,"tries")
    
            break       
        
        print(cows,"Cows , ",bulls," Bulls")
        numberoftries +=1