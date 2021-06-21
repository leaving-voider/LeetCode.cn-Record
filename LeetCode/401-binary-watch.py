###############################################################################################
# 递归遍历所有情况，直接超时；太蠢了，这种想法是想着往LED填，来凑齐满足要求的时间
###############################################################################################
class Solution:
    def analyze(self, string):
        # 0 - 3 代表 1 2 4 8
        first = sum([int(string[i])*(2**i) for i in range(4)])
        # 4 - 9 代表 1 2 4 8 16 32
        second = sum([int(string[i])*(2**(i-4)) for i in range(4, 10)])
        if first > 12 or second > 60:
            return []
        return f"{first}:0{second}" if second < 10 else f"{first}:{second}"
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def digLevel(level, total, timeNow):
            if level == total:
                return [self.analyze(timeNow)]
            res = []
            for i in range(10):
                if timeNow[i] != 1:
                    newTime = copy.copy(timeNow)
                    newTime[i] = 1
                    res.extend(digLevel(level+1, total, newTime))
            return res
        return digLevel(0, turnedOn, [0,0,0,0,0,0,0,0,0,0])

###############################################################################################
# 迭代遍历所有时间
###########
# 时间复杂度：O(1)
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = list()
        for h in range(12):
            for m in range(60):
                if bin(h).count("1") + bin(m).count("1") == turnedOn:
                    # %2d 宽度为2 左边补空格
                    # %02d 宽度为2 左边补0
                    # %-2d 右边补空格
                    ans.append(f"{h}:{m:02d}")
        return ans

###############################################################################################
# 迭代遍历所有灯开闭组合
###########
# 时间复杂度：O(1)
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = list()
        for i in range(1024):
            h, m = i >> 6, i & 0x3f   # 用位运算取出高 4 位和低 6 位
            if h < 12 and m < 60 and bin(i).count("1") == turnedOn:
                ans.append(f"{h}:{m:02d}")
        return ans