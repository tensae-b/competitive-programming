class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        for x in range(len(nums)):
            nums[x]= int(nums[x])

      
        for i in range(len(nums)):
            for j in range(0, len(nums)-i-1):
                if nums[j]> nums[j+1]:
                    temp= nums[j]
                    nums[j]= nums[j+1]
                    nums[j+1]=temp
        res= str(nums[len(nums)-k])          
        print(res)
