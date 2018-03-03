def canPartition(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def canSum(s,i,numbers):
            
            print s,i,numbers
            if cache[i][s] in (1,2):
                print "From cache..."
                if cache[i][s] == 1:
                    return True
                else:
                    return False

            if len(numbers) == 1:
                cache[i][s] = s == numbers[0]
                return s == numbers[0]
            

            
            n = numbers[0]
            if n == s:
                cache[i][s] = 1
                return True
            
            if canSum(s,i+1, numbers[1:]):
                cache[i][s] = 1
                return True
            
            if s > n:
                if canSum(s-n, i+1, numbers[1:]):
                    cache[i][s-n] = 1
                    return True
            
            cache[i][s] = 2 
            return False    
             
        s = sum(nums)
        if s % 2 != 0:
            return False
        s = s/2
        cache = [[0]*(s+1) for i in range(len(nums)+1)]
        
        return canSum(s,0,nums)

print canPartition([100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100])       