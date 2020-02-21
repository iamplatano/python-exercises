

numlist =[]

def findNumber(numlist,numbertofind):
    firstindex = 0
    lastindex = len(numlist) - 1
    middleindex =  int((lastindex - firstindex)/2)
    while middleindex != firstindex:
        
        if numbertofind == numlist[middleindex]:
            return "Number Found"
        elif numbertofind < numlist[middleindex]:
            lastindex = middleindex
            middleindex = lastindex/2
        elif numbertofind > numlist[middleindex]:
            firstindex = middleindex
            middleindex = (lastindex - firstindex)/2

    return "Number Not Found"


def takeInNumbers():
    previousnum = 0
    
    while True:
        try:
            number = int(input("Please enter numbers in ascending order: "))
            if number >= previousnum:
                numlist.append(number)
                previousnum = number
            elif number < previousnum:
                print ("Please enter a valid number ")
            if number == 'stop':
                break
        except ValueError:
            break
    
    return numlist

takeInNumbers()
print(numlist)
numbertofind = int(input("What number do i look for? "))
print(findNumber(numlist,numbertofind))