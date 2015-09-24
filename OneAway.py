""" 1.5 One Away """

from unittest import TestCase

def oneAway(stringA, stringB):
    diff = 0
    if len(stringA) == len(stringB):
        for i in range(0, len(stringA)):
            if stringA[i] != stringB[i]:
                diff = diff + 1
        if diff < 2:
            return True
        else:
            return False

    if len(stringA) > len(stringB):
        pass

    if len(stringA) < len(stringB):
        pass


class isOneAway(TestCase):
    def testOneReplaceTrue(self):
        stringA = 'evan'
        stringB = 'even'
        self.assertTrue(oneAway(stringA, stringB))

    def testOneReplaceFalse(self):
        stringA = 'evan'
        stringB = 'aven'
        self.assertFalse(oneAway(stringA, stringB))