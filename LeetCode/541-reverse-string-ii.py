###############################################################################################
# 遍历一遍
###########
# 时间复杂度：O(n)
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        list_s, len_ = list(s), len(s)
        i = 0
        while i < len_:
            if i + k - 1 < len_:
                l, r = i, i + k - 1
                while l < r:
                    list_s[l], list_s[r] = list_s[r], list_s[l]
                    l += 1
                    r -= 1
            else:
                for j in range(i, i+(len_-i)//2):
                    list_s[j], list_s[len_-(j-i)-1] = list_s[len_-(j-i)-1], list_s[j]
            i += 2*k
        return ''.join(list_s)