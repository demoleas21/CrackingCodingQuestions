""" 1.1 Is Unique """

from unittest import TestCase

def uniqueCheck(string):
    sortedStr = sorted(string)
    for x in range(0,len(string)-1):
        if sortedStr[x] == sortedStr[x+1]:
            return False
    return True

    """ Old Code """
    """for x in range (0, len(string)):
        for y in range (x+1, len(string)):
            if string[x] == string[y]:
                return False
    return True"""

class isUniqueTest(TestCase):
    def testUniqueTrue(self):
        string = 'andrew'
        self.assertTrue(uniqueCheck(string))

    def testUniqueFalse(self):
        string = 'susan'
        self.assertFalse(uniqueCheck(string))