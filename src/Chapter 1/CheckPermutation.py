""" 1.2 CheckPermutation """

from unittest import TestCase

def permCheck(stringA, stringB):
    if len(stringA) != len(stringB):
        return False

    stringCount = {}
    for val in stringA:
        try:
            stringCount[val] = stringCount[val] + 1
        except:
            stringCount[val] = 1

    for val in stringB:
        if stringCount[val] == 0:
            return False
        else:
            stringCount[val] = stringCount [val] - 1
    return True

    """
    count = 0
    for i in range(0, len(stringB)):
        for j in range(0, len(stringA)):
            if stringB[i] == stringA[j]:
                count = count + 1
    if count == len(stringB):
        return True
    else:
        return False
    """

class isPermutationsTrue(TestCase):
    def testPermIsTrue(self):
        stringA = 'andrew'
        stringB = 'werdna'
        self.assertTrue(permCheck(stringA, stringB))

    def testPermIsFalse(self):
        stringA = 'andrew'
        stringB = 'andy'
        self.assertFalse(permCheck(stringA, stringB))

    def testPermLengthNotEqual(self):
        stringA = 'andrew'
        stringB = 'werdn'
        self.assertFalse(permCheck(stringA, stringB))
