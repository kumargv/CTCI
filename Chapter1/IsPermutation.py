import unittest
from collections import Counter
def IsPermutation(string1, string2):
    #Condition to check if the lengths are same. If they dont match, we can disqualofy immediately
    if len(string1)!=len(string2):
        return False
    
    count=Counter()
    for c in string1:
        count[c]=+1
    for c in string2:
        if count[c]==0:
            return False
        count[c]=-1
    return True

class Test(unittest.TestCase):
    dataT = (
                ('abcd', 'bacd'),
                ('3563476', '7334566'),
                ('wef34f', 'wffe34'),
    )
    dataF = (
                ('abcd', 'd2cba'),
                ('2354', '1234'),
                ('dcw4f', 'dcw5f'),
        )

    def test_cp(self):
            # true check
            for test_strings in self.dataT:
                result = IsPermutation(*test_strings)
                self.assertTrue(result)
            # false check
            for test_strings in self.dataF:
                result = IsPermutation(*test_strings)
                self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()