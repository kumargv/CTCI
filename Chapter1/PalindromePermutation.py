import unittest
def PalindromPermutation(string):
    table = [0 for _ in range(ord('z') - ord('a') + 1)]
    oddcount = 0
    for s in string:
        x=char_number(s)
        if x!=-1:
            table[x]+=1
            if table[x]%2:
                oddcount+=1
            else:
                oddcount-=1
    return oddcount<=1
'''This is a function to get the value of the character in the array of 26'''
def char_number(s):
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    val = ord(s)

    if a<=val<=z:
        return val-a
    if A<=val<=Z:
        return val-A
    return -1

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = PalindromPermutation(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main() 


    