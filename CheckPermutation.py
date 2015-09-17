""" 1.2 CheckPermutation """

def permCheck(stringA, stringB):
	count = 0
	for i in range(0, len(stringB)):
		for j in range(0, len(stringA)):
			if stringB[i] == stringA[j]:
				count = count + 1
	if count == len(stringB):
		return True
	else:
		return False

stringA = 'andrew'
stringB = 'ande'
print (permCheck(stringA, stringB)) # Should return True

stringA = 'andrew'
stringB = 'andy'
print (permCheck(stringA, stringB)) # Should return False