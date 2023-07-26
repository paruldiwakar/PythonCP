class Solution:
    def soe(self, n):
        primes = [True for _ in range(n + 1)]
        primes[0] = primes[1] = False
        result = []
        i = 2
        while i * i <= n:
            for j in range(i*2, n + 1):
                if j % i == 0:
                    primes[j] = False
            i += 1
            
        result = [i for i, a in enumerate(primes) if a == True]
        return result
        
n = 12
sol = Solution()
ans1 = sol.soe(n)
print(ans1)

