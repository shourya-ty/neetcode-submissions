class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ""

        for i in digits:
            number += str(i)
        
        new_num = int(number)+1
        new_digits = []
        
        for i in str(new_num):
            new_digits.append(i)
        
        return new_digits