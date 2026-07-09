class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = set()
        length = 0
        for i in nums:
            dupes.add(i)
            if len(dupes) == length:
                return True
            length += 1
        return False
        