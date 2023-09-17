def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int

    Nums is already sorted.
    The idea is to leave the single numbers ordered at the beggining of the list without repeating elements.
    This function returns the number of numbers that are without repeating (number of single numbers in the list).
    It doesnt matter what the list has after the last single number e.g. in= [0,0,1,1,1,2,2,3,3,4] out= 5 because [0,1,2,3,4,_,_,_,_,_].
    
    Slow saves the position of where the last single element found is saved in the beggining of the list.
    Fast saves the position which discovers new single numbers.

    When nums[slow] and nums[fast] are equal, it means no new single number has been discovered, so it goes on until it finds a different one

    When it finds a different one, its a new single number, so it first adds one to slow so the last single number saved is not deleted, and
    then it saves the new single number.

    Because the expected output is the position, the return value is slow+1 because the first position is interpreted as 1, not 0

    """
    slow = 0
    fast = 1
    while fast < len(nums):
        
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]
            
        fast += 1
    return slow+1