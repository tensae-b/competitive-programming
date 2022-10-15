
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        stri=""
        for i in range(len(nums)):
            for j in range(0, len(nums)-i-1):
                if nums[j]> nums[j+1]:
                    temp= nums[j]
                    nums[j]= nums[j+1]
                    nums[j+1]=temp
                    
        for x in range(len(nums)):
            nums[x]= str(nums[x])

        for y in range(len(nums)):
            stri+= nums[y]
            
        print(stri)
