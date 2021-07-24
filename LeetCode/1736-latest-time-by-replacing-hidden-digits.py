###############################################################################################
# 分情况讨论即可
###########
# 时间复杂度：O(n)
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def maximumTime(self, time: str) -> str:
        res = ""
        for i in range(len(time)):
            if i == 0 and time[i] == '?':
                res += '2' if time[1] < '4' or time[1] == '?' else '1'
            elif i == 1 and time[i] == '?':
                res += '3' if res[0] == '2' else '9'
            elif i == 3 and time[i] == '?':
                res += '5'
            elif i == 4 and time[i] == '?':
                res += '9'
            else:
                res += time[i]
        return res