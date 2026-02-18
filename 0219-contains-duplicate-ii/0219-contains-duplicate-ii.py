class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_set = set()
        i=0
        for num in nums:
            if num in nums_set:
                i+=1
                return True
            nums_set.add(num)
            if len(nums_set) > k:
                nums_set.remove(nums[i-k])
            i+=1
        return False