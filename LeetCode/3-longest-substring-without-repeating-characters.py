###############################################################################################
# 本身不难，一次遍历即可，就是边界多，需要注意
###########
# 时间复杂度：O(n)
# 空间复杂度：O(n)，用了哈希存位置
###############################################################################################
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        res = 0
        cur = 1
        cur_set = defaultdict(int)
        cur_set[s[0]] = 0
        for i in range(1, len(s)):
            if s[i] not in cur_set:
                cur += 1
                cur_set[s[i]] = i
            else:
                res = max(res, cur) # cur是前面的长度
                cur -= cur_set[s[i]] - i + cur # 更新为当前长度，即前去前面的
                # 删除前面的
                for per in range(cur_set[s[i]], i - len(cur_set) - 1, -1): # cur指示的长度已经改变了，用len(cur_set)
                    cur_set.pop(s[per])
                cur_set[s[i]] = i # 加入这个
        res = max(res, cur)
        return res

# 也可以用双指针，不用在循环删除时考虑边界并不断维护长度；其实上面那个也不用维护长度的，自讨苦吃
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_ = len(s)
        if len_ <= 1:
            return len_
        res = 0
        cur_set = set(s[0])
        l, r = 0, 1
        while r < len_:
            if s[r] not in cur_set:
                cur_set.add(s[r])
            else:
                res = max(res, len(cur_set))
                while s[l] != s[r]: # 一样的字母就不用删了
                    cur_set.remove(s[l])
                    l += 1
                l += 1 # 这里左边再移动一位
            r += 1 # 看下一位
        res = max(res, len(cur_set))
        return res