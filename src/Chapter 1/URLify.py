""" 1.3 URLify """

def URLconvert(string):
    strlst = list(string)
    for i in range(0, len(strlst)):
        if strlst[i] == ' ':
            strlst[i] = '%20'
    string = "".join(strlst)
    return string

string = 'my name is andrew'
print (URLconvert(string)) # Returns: my%20name%20is%20andrew