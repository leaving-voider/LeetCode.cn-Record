###############################################################################################
# 遍历一遍，可以叫做双指针，分别指向读和写的位置
###########
# 时间复杂度：O(n)
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def compress(self, chars: List[str]) -> int:
        idx = 0
        i, len_ = 0, len(chars)
        while i < len_:
            num, ch = 1, chars[i]
            while i + 1 < len_ and chars[i+1] == ch:
                num += 1
                i += 1
            if num > 1:
                chars[idx] = ch
                idx += 1
                if num < 10:
                    chars[idx] = str(num)
                    idx += 1
                else:
                    for per in str(num):
                        chars[idx] = per
                        idx += 1
            else:
                chars[idx] = ch
                idx += 1
            i += 1
        return idx