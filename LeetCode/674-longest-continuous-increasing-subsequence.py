class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        Length = len(nums)
        if Length == 0:
            return 0
        LCISLen = 1
        i = 0
        # 一次寻找一个当前最长序列
        while(1):
            # 若此次序列的最长可能长度都还不如已知最长，则直接退出
            if Length - i <= LCISLen:
                break
            # 初始为1
            thisLongestLen = 1
            # 从第二个位置开始
            for j in range(i+1, Length):
                if nums[j] > nums[j-1]:
                    thisLongestLen += 1
                else:
                    break
            LCISLen = thisLongestLen if thisLongestLen > LCISLen else LCISLen
            # 下一个寻找的序列直接从未找过的序号开始，因为从已找过的开始不可能还有更长
            i += thisLongestLen
        return LCISLen
