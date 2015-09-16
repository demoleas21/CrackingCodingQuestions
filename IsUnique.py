""" 1.1 Is Unique """

def uniqueCheck(string):
    for x in range (0, len(string)):
        for y in range (x+1, len(string)):
            if string[x] == string[y]:
                return False
    return True

string = 'andrew'
print(uniqueCheck(string)) # Should return True

string = 'susan'
print(uniqueCheck(string)) # Should return False