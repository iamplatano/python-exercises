def reverseString(str):
    str = str.split(" ")
    stringLength = len(str)
    for i in range(int(stringLength/2)):
        holder = str[i]
        str[i] = str[(stringLength - 1) - i]
        str[(stringLength - 1) - i] = holder
    print(str)
str = input("Please enter a phrase ")
reverseString(str)