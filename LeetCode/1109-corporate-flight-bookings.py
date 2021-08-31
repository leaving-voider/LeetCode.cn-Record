###############################################################################################
# 经典差分应用
###########
# 时间复杂度：O(n)
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0]*(n+2)
        def insert(l, r, num):
            res[l] += num
            res[r+1] -= num
        for first, last, num in bookings:
            insert(first, last, num)
        answer = [res[1]]
        for i in range(2, n+1):
            answer.append(res[i] + answer[-1])
        return answer