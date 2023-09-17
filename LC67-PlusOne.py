"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.


Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
"""
def plusOne(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]

    First we pass through digits and adding it to the sum by properly multiplying it to the correct power.
    For example for [1,2,3] sum adds 1*10**2+2*10*1+3*10*0=100+20+3=123.
    Then it sums plus one to the sum and I clear digits in memory using [:] for reusing that space.
    Then I iterate over the sum as a string and then add it to digits each digit as an integer.
    """
    sum = 0
    power = len(digits)-1
    for i, num in enumerate(digits):
        sum += num*10**(power-i)
    sum += 1
    digits[:] = []
    for i, num in enumerate(str(sum)):
        digits.append(int(num))
    return digits