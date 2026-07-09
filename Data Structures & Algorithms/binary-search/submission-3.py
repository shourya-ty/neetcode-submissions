class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left > right:
                return -1 # Base case: target not found
                
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(mid + 1, right) # Search right half
            else:
                return binary_search(left, mid - 1)  # Search left half
                
        return binary_search(0, len(nums) - 1)

