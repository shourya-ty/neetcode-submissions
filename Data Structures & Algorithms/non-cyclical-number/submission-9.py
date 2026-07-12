class Solution:
    def isHappy(self, n: int) -> bool:
        found = set()
        number = n
        while number not in found:
            found.add(number) # 1. ADD the current number to the set first
            
            number_str = str(number)
            total = 0
            for digit in number_str:
                int_digit = int(digit)
                total += (int_digit * int_digit)
                
            if total == 1:
                return True
                
            number = total # 2. Move to the next number
            
        return False
