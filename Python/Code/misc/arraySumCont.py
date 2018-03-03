
#Given array of integers, find how many continuous subarrays sum up to a given sum.
#Leetcode
def subarraySum(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = {}
        sums = [0]
        
        count = 0
        cSums = 0
        for i in range(0,len(nums)):
            cSums += nums[i]
            print sums, "Checking ", cSums-k
            if ((cSums-k) in sums):
                count += sums.count(cSums-k)
            sums.append(cSums)  
        
        return count   

print subarraySum([0,0,0,0,0,0,0,0,0,0],0)           