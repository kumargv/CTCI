#QUESTION 2 - Demo Assessment

#At Audible, a subscriber can gift an audiobook from his/her library to any other non-subscriber to kick start their audiobook journey. The first time subscriber can receive up to a maximum of N audiobooks from their friends/relatives. When a non-subscriber receives an audiobook, we can infer that the two may be related. Similarly, if the non-subscriber receives gifted books from two other subscribers, we can inter that all of them are related and the three of them form a group. More formally, a group is composed of all of the people who know one another, whether directly or transitively. Audible would like your help finding out the number of such distinct groups from the input data.
#Example 
#Consider the following input matrix M: 
#110
#110 
#001
#  0 1 2
#0 1 1 0
#1 1 1 0
#2 0 0 1

#Every row corresponds to a subscriber and the value M[i][j] determines if j was gifted a book by i. In the above example, user 0 has gifted a book to user 1 and so they are connected [0][1], while person 2 has not received a book from anyone or gifted book to anyone. Therefore, there are 2 groups. 
#M[i][i] = 1 if i == j; (Each of the people is known to self),

#Determine the number of groups represented in a matrix,
#Note: The method signatures may vary slightly depending on the requirements of the chosen language. For example, C Language will have an argument that represents the number of rows and columns in the matrix. Also, Java will receive a list rather than an array.

#Function Description 
#Complete the function countGroups in the editor below.
#countGroups has the following parameter(s):
# int related[n]: an array of strings of binary digits related[i] that represent connections of people

#Returns:
# int: an integer that represents the number of groups of people

#Constraints
#• 1<=n<=300 
#• 0<i<n 
#• /related/ = n 
#• Each related contains a binary string of n zeros and ones. related is a square matrix.

#Input Format for Custom Testing
#Input from stdin will be processed as follows and passed to the function.

#The first line contains an integer n, the size of the square, association matrix, related. 
#The next n lines each contain a binary string of length n that, represents a row in the matrix, related[i] where O<=i<n.

#Sample Case 0
#Sample Input

#STDIN    Function 
#	      -----
#4	    → size of related [] n = 4 
#1100   → related = ['1100', '1110', '0110', '0001']
#1110 
#0110 
#0001

#Sample Output
#2

#Explanation 
#Squares highlighting a connection between two people are highlighted in green. Each of the people is known to self, so they are highlighted in gray.

#    related[]

#    0 1 2 3
#0   1 1 0 0
#1   1 1 1 0
#2   0 1 1 0
#3   0 0 0 1

#The 2 groups formed are: {related[0], related[1], related[2]} and related[3]}

#There are n = 4 people numbered related[O] through related[3]. There are 2 pairs who directly know each another: (related[0], related[1]) and (related[1],related[2]). Because a relation is transitive, the set of people {related[0], related[1], related[2]} is considered a single group. 
#The remaining person, related[3], does not know any other people, and is a separate group: {related[3]}. 
#There are a total of 2 groups.

#Sample Case 1 
#Sample Input

#STDIN    Function
#	      -----
#5 	    → size of related[] n = 5 
#10000  → related = ['10000', '61000', '00100', '00010', '00001'] 
#01000 
#00100 
#00010 
#00001

#Sample Output
#5

#Explanation
    
#    related []

#1 0 0 0 0
#0 1 0 0 0
#0 0 1 0 0
#0 0 0 1 0
#0 0 0 0 1

#No direct relationships are shown so there are 5 groups: 
#{related[0]}, {related[1]}, {related[2]}, {related[3]), and {related[4]}.

#SOLUTION:

def countGroups(related):
    # Write your code here
    count = 0
    length = len(related)
    mod_related = []
    for char in related:
        mod_related.append([int(x) for x in char])
        
    for i in range(length):
        if mod_related[i][i] == 1:
            count+=1
            dfs(i, length, mod_related)
    return count

def dfs(index, length, matrix):
    if matrix[index][index] == 0:
        return
    else:
        for i in range(length):
            if matrix[index][i] == 1:
                matrix[index][i] = 0
                dfs(i, length, matrix)