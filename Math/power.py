class Solution:
    
    def pow(self, a, b):
        res = 1
        while b > 0:
            if b & 1:
                res *= a
                b -= 1
            else:
                a = a * a
                b >>= 1
        return res
    
    def moduloPow(self, a, b, n):
        res = 1
        while b > 0:
            if b & 1:
                res = (res % n * a % n) % n
                b -= 1
            else:
                a = (a % n * a % n) % n
                b >>= 1
        return res
            
a, b = 2, 7
sol = Solution()
ans1 = sol.pow(a, b) #2^6
n = 3
ans2 = sol.moduloPow(67, 567, 78)
print(ans2)
