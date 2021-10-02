# Python program to find maximum sum path
 
# This function returns the sum of elements on maximum path from
# beginning to end
 
 
def maxPathSum(ar1, ar2, m, n):
 
    # initialize indexes for ar1[] and ar2[]
    i, j = 0, 0
 
    # Initialize result and current sum through ar1[] and ar2[]
    result, sum1, sum2 = 0, 0, 0
 
    # Below 3 loops are similar to merge in merge sort
    while (i < m and j < n):
 
        # Add elements of ar1[] to sum1
        if ar1[i] < ar2[j]:
            sum1 += ar1[i]
            i += 1
 
        # Add elements of ar2[] to sum2
        elif ar1[i] > ar2[j]:
            sum2 += ar2[j]
            j += 1
 
        else:   # we reached a common point
 
            # Take the maximum of two sums and add to result
            result += max(sum1, sum2) +ar1[i]
            #update sum1 and sum2 to be considered fresh for next elements
            sum1 = 0
            sum2 = 0
            #update i and j to move to next element in each array
            i +=1
            j +=1
 
           
 
    # Add remaining elements of ar1[]
    while i < m:
        sum1 += ar1[i]
        i += 1
    # Add remaining elements of b[]
    while j < n:
        sum2 += ar2[j]
        j += 1
 
    # Add maximum of two sums of remaining elements
    result += max(sum1, sum2)
 
    return result
 
 
# Driver code
ar1 = [2, 3, 7, 10, 12, 15, 30, 34]
ar2 = [1, 5, 7, 8, 10, 15, 16, 19]
m = len(ar1)
n = len(ar2)
 
# Function call
print "Maximum sum path is", maxPathSum(ar1, ar2, m, n)