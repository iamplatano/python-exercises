def vert_mirror(strng):
    splitstring = strng.split( )
    newstrng = ""
    for ind in range(len(splitstring)):
        string = splitstring[ind]
        string = string[::-1]
        splitstring[ind] = string
        newstrng += splitstring[ind] 
    return newstrng
    
def hor_mirror(strng):
   
    splitstring = strng.split()
    low = 0
    high = len(splitstring) - 1

    while low <= high:
        splitstring[low],splitstring[high] = splitstring[high],splitstring[low]
        low += 1
        high -= 1

    return splitstring


def oper(fct,s):
    return fct(s)
        
print(vert_mirror(r"abcd\nefgh\nijkl\nmnop"))