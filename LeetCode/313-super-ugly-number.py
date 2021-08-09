###############################################################################################
# 试除法，判断每个数的质因子在不在primes，超时
# 本还思考了筛质数的方法，但超时严重，几乎是(2^32)^2的时间复杂度
###########
# 时间复杂度：O(m*sqrt(m)), m表示第n个超级丑数的数值，而不是第n
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n == 1:
            return n
        primes = set(primes)
        def divide(x):
            i, res = 2, []
            while i <= x//i:
                while x % i == 0:
                    x //= i
                    res.append(i)
                i += 1
            if x > 1:
                res.append(x)
            return res
        k = 1
        for i in range(2, int(1e9)):
            flag = 1
            for factor in divide(i):
                if factor not in primes:
                    flag = 0
                    break
            if flag:
                k += 1
            if k == n:
                return i

###############################################################################################
# 官方给的方法，每次从heap里pop一个，保证是最小的，然后和primes里每个进行相乘，再全部加入heap，这些都是超级丑数
# 这样就能保证第n次pop出来的超级丑数，就是从小到大的第n个
###########
# 时间复杂度：O(nm*O(lognm)), n表示外圈循环，m是primes个数，每次pop为O(1)，但每次push为O(lognm)，nm表示heap中数的个数，因为要up嘛
# 空间复杂度：O(nm)，堆和哈希消耗
###############################################################################################
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = [1]
        seen = set()
        for i in range(n):
            t = heapq.heappop(heap)
            for j in primes:
                k = j*t
                if k not in seen:
                    heapq.heappush(heap, k)
                    seen.add(k)
        return t