import unittest
import string
def URLify_easy(string):
    return string.strip().replace(' ', '%20')


print(URLify_easy('abab  abab aaaaaa '))

def URLify(string, length):
    new_index = len(string)

    for i in reversed(range(length)):
        if string[i] == ' ':
            string[new_index-3:new_index]="%20"
            new_index-=3
        else:
            string[new_index-1]=string[i]
            new_index-=1
    return string

class Test(unittest.TestCase):
    #Test Cases
    # Using lists because Python strings are immutable

    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]
    
    #data=['abab  abab aaaaaa ']

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = URLify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
