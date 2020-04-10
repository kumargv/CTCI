import unittest
def IsUnique(string):
    
    if len(string)>128:
        return False
    
    letters ={}
    for letter in string:
        if letter in letters:
            return False
        letters[letter]= True
    return True

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = IsUnique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = IsUnique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()