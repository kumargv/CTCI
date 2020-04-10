import unittest

def EditDistance(str1, str2):
    '''Check if a string can converted to another string with a single edit'''
    if len(str1) == len(str2):
        return one_edit_replace(str1, str2)
    elif len(str1) + 1 == len(str2):
        return one_edit_insert(str1, str2)
    elif len(str1) - 1 == len(str2):
        return one_edit_insert(str2, str1)
    return False

def one_edit_replace(str1, str2):
    foundDifference=False
    for s1, s2 in zip(str1, str2):
        if s1 != s2:
            if foundDifference:
                return False
            foundDifference=True
    return True
          
def one_edit_insert(str1, str2):
    foundDifference = False
    index1=0
    index2=0
    while index1<len(str1) and index2<len(str2):
        if(str1[index1]!=str2[index2]):
            if foundDifference:
                return False
            foundDifference=True
            index2+=1
        else:
            index1+=1
            index2+=1
    return True

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = EditDistance(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
