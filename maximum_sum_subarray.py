def maxSubArraySum(a,size):
    max_so_far = -float('inf') - 1
    max_ending_here = 0
      
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
            k = i
 
        if max_ending_here < 0:
            max_ending_here = 0
    print(k)  
    return max_so_far
  
a = [-1, -2, 1, 2, 3, -5, 4, 5]
print("Maximum contiguous sum is", maxSubArraySum(a,len(a)))
  