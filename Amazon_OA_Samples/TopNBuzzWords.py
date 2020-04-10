from collections import defaultdict

def topNBuzzWords(numToys, topToys, toys, numQuotes, quotes):
    # numToys, an integer representing the number of toys
    # topToys, an integer representing the number of top toys your algorithm needs to return;
    # toys, a list of strings representing the toys,
    # numQuotes, an integer representing the number of quotes about toys;
    # quotes, a list of strings that consists of space-sperated words representing articles about toys
    
#     Output:
#     Return a list of strings of the most popular N toys in order of most to least frequently mentioned

#     Note:
    # The comparison of strings is case-insensitive. If the value of topToys is more than the number of toys,       return the names of only the toys mentioned in the quotes. If toys are mentioned an equal number of           times in quotes, sort alphabetically.
    if not topToys or not toys or not quotes:
        return []
    
    toys = set(t.lower() for t in toys)
    print(toys)
    # toys = set(toys)
    hmap = defaultdict(int)
    for quote in quotes:
        quote = quote.split(' ')
        for word in quote:
            word = word.lower()
            if word in toys:
                hmap[word] += 1                
            elif (word[:-1] in toys and not word[-1].isalpha() and not word[-1].isdigit()):
                hmap[word[:-1]] += 1
    print(hmap)
    return sorted(hmap, key = lambda x: (-hmap[x], x))[:topToys]
    

topToys = 3
toys = ["anacell", "betacellular", "cetracellular", "deltacellular", "eurocellular"]
quotes = [
"I love anacell Best services provided by anacell in town ",
"betacellular has great services",
"deltacellular provides much better services than betacellular",
"cetracellular is worse than eurocell",
"betacellular is better than deltacellular",
]
print(topNBuzzWords(5, 3, toys, 6, quotes))      