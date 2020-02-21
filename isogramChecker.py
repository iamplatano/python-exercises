def is_isogram(string):
    
    for i in range(len(string)):    
        
        for j in range (i+1,len(string)):
            if string[j] == string[i]:
                return False
    return True
print(is_isogram("Dermatoglyphics"))