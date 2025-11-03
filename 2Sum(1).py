# What enumerate does: 
# 0 2
# 1 7
# 2 11
# 3 15

def two_sum(nums, target):
    hashmap = {}                         # Make a hashmap to check if weve visted that value & index yet 

    for index, value in enumerate(nums):    # Use enumerate to get our index & values 
        need = target - value               # What 2 numbers givces us taget the easier way 

        if need in hashmap:                 # if that number in hasmap return it 
            return [hashmap[need], index] 
        
        hashmap[value] = index              # If not add it into our hashmap


nums = [2, 7, 11, 15]                       # Test it out
target = 9                                  # Time Complexity: O(n)
                                            # Space Complexity: O(n)
print(two_sum(nums,target))