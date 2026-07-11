class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequencies efficiently
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # 2. Create buckets where index = frequency
        # Example: bucket[3] will hold all numbers that appear exactly 3 times
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            bucket[freq].append(num)
            
        # 3. Collect the top k elements by scanning buckets backward
        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
