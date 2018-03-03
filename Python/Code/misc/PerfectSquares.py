import math
from collections import deque
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        def minSqSum(n, nums, bfs): 
            def getNgbs(x):
                y = []
                for num in nums:
                    if (x - num) >= 0:
                        y.append(x-num)
                #y.sort(reverse=False)
                return y

            q = deque()
            q.appendleft(n)
            black = {s : False for s in range(0,n+1)}
            brown = {s : False for s in range(0,n+1)}
        
            

            while q:
                node = q.pop()
                brown[node] = True
                #print node
                if node == 0:
                    return True
                
                ngbs = getNgbs(node)
                #print ngbs

                for ng in ngbs:
                    if not brown[ng] and not black[ng]:
                        bfs[ng] = node
                        q.appendleft(ng)
                        brown[ng] = True
                #print q
                brown[node] = False
                black[node] = True
            return False
    
        count = 0
        bfs = {n:-1}
        
        t =  minSqSum(n, [x*x for x in range(1,int(math.floor(math.sqrt(n)))+1)], bfs)
        if t == True:
            p = bfs[0]
            while p != -1:



                count += 1
                p = bfs[p]
        #print bfs
        return count

s = Solution()
print s.numSquares(7168)        