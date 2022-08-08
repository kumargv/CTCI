#QUESTION 2

#Amazon Warehouse has a group of n items of various weights lined up in a row. A segment of contiguously placed items can be shipped together if and only if the difference between the weights of the heaviest and lightest item differs by at most k to avoid load imbalance.

#Given the weights of the n items and an integer k, find the number of segments of items that can be shipped together.

#Note: A segment (1,r) is a subarray starting at index land ending at index rwhere Isr.

#Example 
#k=3 
#weights = [1, 3, 6]

#Weight difference between max and min for each (1,r) index pair are:
#• (0,0) -> max(weights[0]) - min(weights[0]) = max(1) - min(1) = 1 - 1 = 0 
#• (0,1) -> max(1, 3)- min(1, 3) = 3 - 1 = 2 
#• (0,2) -> max(1, 3, 6) - min(1, 3, 6) = 6 - 1 = 5 *** difference >k *** 
#• (1, 1) as max(3) - min(3) = 3-3 = 0 
#• (1, 2) as max(3, 6) - min(3, 6) = 6 - 3 = 3 
#• (2, 2) as max(6) - min(6) = 6 - 6 = 0

#5 of the 6 possible segments have a difference less than or equal to 3. Return 5.

#Function Description 
#Complete the function countPossibleSegments in the editor below.

#countPossibleSegments has the following parameters:
# int k: the maximum tolerable difference in weights 
# int weights[n]: the weights of the items
#Returns
# long int: the number of segments of items that can be shipped together

#Constraints
#• 1<=k, weights[i] <= 10^9 
#• 1<=n<= 3*10^5

#Sample Case 0
#Sample Input For Custom Testing
#STDIN     Function
#	       -----
#3       → k = 3 
#3       → weights[]  size n = 3
#1 	     → weights = [1, 5, 4]
#5
#4

#Sample Output
#4

#Explanation 
#The balanced subsegments only are:
#• (0, 0) as max(weights[0]) - min(weights[0])= 1 - 1 = 0. 
#• (1, 2) as max(weights[1], weights(21) - min(weights[1], weights[2]) = 5-4 = 1. 
#• (2, 2) as max(weights[2]) - min(weights[2]) = 4-4 = 0. 
#• (1, 1) as max(weights[1]) - min(weights[1]) = 5 - 5 = 0.

#Sample Case 1
#Sample Input For Custom Testing
#STDIN     Function
#	       -----
#9       → k = 9 
#3       → weights[]  size n = 3
#1 	     → weights = [1, 10, 2]
#10
#2

#Sample Output
#6

#Explanation 
#The 6 possible subsegments are all balanced.

#SOLUTION (7/15 Passed)

def countPossibleSegments(k, weights):
    # Write your code here
    if not weights:
        return 0
    if len(weights) == 1:
        return 1
    
    num = len(weights)
    l = 0
    result = num
    
    while l < num:
        max_i = l
        min_i = l
        
        r = l+1
        update = True
        while r < num:
            if weights[r]>weights[max_i]:
                max_i = r
            if weights[r] < weights[min_i]:
                min_i = r
            if weights[max_i] - weights[min_i] >k:
                if min_i < max_i:
                    l = min_i+1
                else:
                    l = max_i+1
                update = False
                break
            else:
                print(weights[l:r+1])
                result+=1
                r+=1
        if update:
            l+=1
    return result
