###############################################################################################
# 双指针模拟滑动窗口解决，可以叫双指针，也可以叫滑动窗口，统一叫双指针吧
###########
# 时间复杂度：O(n*Σ)，最多遍历两遍，所以是O(n)的复杂度，每次都要比较，比较的time complexit根据字符集的长度来，此题中Σ=52
# 空间复杂度：O(Σ)，存字符集
###############################################################################################
class Solution:
    def minWindow(self, s: str, t: str) -> str: 
        l = r = 0
        len_ = len(s)
        diclr = defaultdict(int)
        diclr[s[0]] = 1
        
        dict_ = defaultdict(int)
        for ch in t: # 预处理，看t中各个字母有多少个
            dict_[ch] += 1
        
        def check():
            for key in dict_: # 大小写英文字母，最多52个
                if dict_[key] > diclr[key]:
                    return False
            return True

        res = float("inf")
        minl = minr = -1
        while r < len_:
            if check(): # 只要满足当前窗口内包含了t串的所有字符，则就可以更新最短窗口并尝试缩小窗口（把l往右移）
                if r - l + 1 < res:
                    res = r - l + 1
                    minl, minr = l, r
                diclr[s[l]] -= 1
                l += 1
            else: # 当前窗口不满足包含t时，只能把r往右移，扩大窗口以求包含t
                r += 1
                if r < len_:
                    diclr[s[r]] += 1
        return s[minl:minr+1]