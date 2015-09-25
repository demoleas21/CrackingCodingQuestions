""" 1.5 One Away """

from unittest import TestCase
import itertools

def oneAway(stringA, stringB):
    diff = 0
    if len(stringA) == len(stringB):
        for i in range(0, len(stringA)):
            if stringA[i] != stringB[i]:
                diff = diff + 1
        if diff > 1:
            return False
        else:
            return True

    if len(stringA) > len(stringB):
        j = 0
        for i in range(0, len(stringA)):
            if stringA[i] != stringB[j]:
                diff = diff + 1
                j = j - 1
            j = j + 1
        if diff > 1:
            return False
        else:
            return True

    if len(stringA) < len(stringB):
        j = 0
        for i in range(0, len(stringB)):
            if stringB[i] != stringA[j]:
                diff = diff + 1
                j = j - 1
            print (stringB[i])
            print (stringA[j])
            print ("\n")
            j = j + 1
        if diff > 1:
            return False
        else:
            return True


class isOneAway(TestCase):
    def testOneReplaceTrue1(self):
        stringA = 'evan'
        stringB = 'even'
        self.assertTrue(oneAway(stringA, stringB))

    def testOneReplaceTrue2(self):
        stringA = 'evan'
        stringB = 'evan'
        self.assertTrue(oneAway(stringA, stringB))

    def testOneReplaceFalse(self):
        stringA = 'evan'
        stringB = 'aven'
        self.assertFalse(oneAway(stringA, stringB))

    def testOneLessTrue1(self):
        stringA = 'evan'
        stringB = 'evn'
        self.assertTrue(oneAway(stringA, stringB))

    def testOneLessTrue2(self):
        stringA = 'evan'
        stringB = 'van'
        self.assertTrue(oneAway(stringA, stringB))

    def testOneMoreTrue1(self):
        stringA = 'evan'
        stringB = 'evayn'
        self.assertTrue(oneAway(stringA, stringB))

    def testOneMoreTrue2(self):
        stringA = 'evan'
        stringB = 'evanz'
        self.assertTrue(oneAway(stringA, stringB))

    def testOneMoreFalse(self):
        stringA = 'evan'
        stringB = 'event'
        self.assertFalse(oneAway(stringA, stringB))

    def testOneLessFalse(self):
        stringA = 'evan'
        stringB = 'ven'
        self.assertFalse(oneAway(stringA, stringB))
        

stringA = 'evan'
stringB = 'evanz'
oneAway(stringA, stringB)