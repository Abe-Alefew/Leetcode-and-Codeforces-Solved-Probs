class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        nums_dict = defaultdict(int)
        output = []
        for i in range(n):
            if nums[i] in nums_dict:
                nums_dict[nums[i]] += 1
            else:
                nums_dict[nums[i]] = 1

        for k,v in nums_dict.items():
            if v > (n//3):
                output.append(k)
        
        return output