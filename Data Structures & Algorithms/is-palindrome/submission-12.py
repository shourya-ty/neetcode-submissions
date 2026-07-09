class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()
        start_slider, end_slider = 0, len(s)-1
        while(start_slider < end_slider):
            if s[start_slider].isalnum() == False:
                start_slider += 1
            elif s[end_slider].isalnum() == False:
                end_slider -= 1
            else:
                if(s[start_slider] != s[end_slider]):
                    return False
                start_slider += 1
                end_slider -= 1
        return True