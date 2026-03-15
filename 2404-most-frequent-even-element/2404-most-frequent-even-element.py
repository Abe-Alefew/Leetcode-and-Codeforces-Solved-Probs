class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums_dict = defaultdict(int)
        n= len(nums)
        output = -1
        max_num = 0
        nums.sort()
        for num in nums:
            if num%2 == 0:
                if num in nums_dict:
                    nums_dict[num]+=1
                else:
                    nums_dict[num]= 1

        for k,v in nums_dict.items():
            if  v > max_num:
                output = k
                max_num = v
            
                   
        
        return output