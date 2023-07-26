class BitMask:
    
    def swap(self, a, b):
        a = a ^ b
        b = a ^ b
        a = a ^ b
        return a, b
    
    def findIthbit(self, n, i):
        mask = 1 << i
        return 1 if mask & n else 0

    def setIthbit(self, n, i):
        mask = 1 << i
        return n | mask
    
    def clearIthbit(self, n, i):
        mask = ~(1 << i)
        return n & mask
    
    def getSetbits(self, n):
        count = 0
        while n != 0:
            n = n & (n - 1)
            count += 1
        return count

sol = BitMask()
a, b = 5, 7
print(sol.swap(a, b))
n = 309
print(sol.findIthbit(n, 5))
print(sol.setIthbit(n, 7)) #437
print(sol.clearIthbit(n, 5)) #277
print(sol.getSetbits(n))
