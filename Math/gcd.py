class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        if a > b:
            return self.gcd(b, a % b)
        return self.gcd(a, b % a)
    
a, b = 32, 30
sol = Solution()
ans = sol.gcd(a, b)
print(ans)