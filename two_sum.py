def twoSum(nums: list[int], target: int) -> list[int]:
    # Stores seen numbers and their indices
    seen = {} 
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if the complement already exists
        if complement in seen:
            return [seen[complement], i]
            
        # Record the current number and its index
        seen[num] = i
        
    return []  # Return empty if no pair is found