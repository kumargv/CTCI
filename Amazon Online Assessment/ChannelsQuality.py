#QUESTION 1

#Amazon's AWS provides fast and efficient server solutions. The developers want to stress-test the quality of the servers' channels. They must ensure the following:
#• Each of the packets must be sent via a single channel.
#• Each of the channels must transfer at least one packet.
#The quality of the transfer for a channel is defined by the median of the sizes of all the data packets sent through that channel.
#Note: The median of an array is the middle element if the array is sorted in non-decreasing order. If the number of elements in the array is even, the median is the average of the two middle elements.
#Find the maximum possible sum of the qualities of all channels. If the answer is a floating-point value, round it to the next higher integer.
#Example packets = [1,2,3,4,5) channels = 2
#At least one packet has to go through each of the 2 channels. One maximal solution is to transfer packets {1, 2, 3, 4 through channel 1 and packet {5} through channel 2.
#Channel 1
#Channel 2
#The quality of transfer for channel 1 is (2 + 3)/2 = 2.5 and that of channel 2 is 5. Their sum is 2.5 + 5 = 7.5 which rounds up to 8.

#Function Description 

#Complete the function maximumQuality in the editor below.
#maximumQuality has the following parameter(s):
# int packets[n]: the packet sizes 
# int channels: the number of channels
#Returns
# long int: the maximum sum possible

#Constraints
#• 1 <= len(packets) < 5 * 105 
#• 1 <= packets[i] = 109 
#• 1 <= channels < len(packets)

#Sample Case 0 
#Sample Input For Custom Testing

#STDIN     Function
#	       -----
#5       → packets [] size n = 5
#2       → packets = [2, 2, 1, 5, 3]
#2
#1
#5
#3
#2	    → channels = 2

#Sample Output
#Explanation 
#One solution is to send packet (5) through one channel and {2, 2, 1, 3) through the other. The sum of quality is 5+ (2 + 2)/2 = 7.

#Sample Case 1
#Sample Input For Custom Testing

#STDIN     Function
#	       -----
#3       → packets [] size n = 3 
#89 	 → packets = [89, 48, 14]
#48
#14
#3 	  → channels = 3

#Sample Output
#151

#Explanation 
#There are 3 channels for 3 packets. Each channel carries one, so the overall sum of quality is 89, +48 + 14 = 151.

#Sample Case 2 
#Sample Input For Custom Testing

#STDIN     Function
#	       -----
#1      → packets [] size n = 1 
#1 	    → packets = [1]
#1 	    → channels = 1

#Sample Output
#1

#Explanation 
#There is only one channel and only one packet. The only choice is to send the packet through this channel. The quality of the transfer is 1 since the median of an array of a single element is that element itself.
#SOLUTION (12/15 Passed)

def maximumQuality(packets, channels):
    # Write your code here
    n = len(packets)
    print(n)
    result = 0
    
    #if (n == channels):
    #    for i in range(n):
    #        result += packets[i]        
    #    return int(result)
    
    packets.sort()
    
    for i in range(n-channels+1, n):
        result+=packets[i]
        
    n = n-channels
    #n = n-channels+1
    if (n%2==0):
        result +=packets[int(n/2)]
    else:
        val = packets[int(n/2)] + packets [int(n/2)+1]
        result += val/2
    
    return int(result)
