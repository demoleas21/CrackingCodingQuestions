""" 1.4 Palindrome Permutation """

from itertools import permutations

def PalPerm(string):
    strlst = list(string)
    for i in range(0, len(strlst)):
        if strlst[i] == ' ':
            space = i
            strlst[i] = ''
    string = "".join(strlst)
    letterCount = {}
    for key in string:
        try:
            letterCount[key] = letterCount[key] + 1
        except:
            letterCount[key] = 1

    if len(string) % 2 == 0: # even
        newString = ''
        for key in letterCount:
            halfCount = letterCount[key] // 2
            for _ in range(0, halfCount):
                newString = newString + key
        perm_str = permStr(newString)
        perm_rev = []
        for item in range(0,len(perm_str)):
            perm_rev.append(perm_str[item][::-1])
        final_str = []
        for i in range(0, len(perm_str)):
            final_str.append(perm_str[i] + perm_rev[i])
        return final_str

    if len(string) % 2 == 1: # odd
        for key in letterCount:
            if letterCount[key] % 2 == 1:
                pivot = key
                letterCount[key] = letterCount[key] - 1

        newString = ''
        for key in letterCount:
            halfCount = letterCount[key] // 2
            for _ in range(0, halfCount):
                newString = newString + key
        perm_str = permStr(newString)
        perm_rev = []
        for item in range(0,len(perm_str)):
            perm_rev.append(perm_str[item][::-1])
        final_str = []
        for i in range(0, len(perm_str)):
            final_str.append(perm_str[i] + pivot + perm_rev[i])
        return final_str

def permStr(string):
    perm_results = [''.join(p) for p in permutations(string)]
    return perm_results

string = 'rraacce'
print (PalPerm(string))
#PalPerm(string)