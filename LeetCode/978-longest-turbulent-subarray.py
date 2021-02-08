###############################################################################################
# 我的方法还不错，一次遍历，时间复杂度也就O(n)，就不用看官方给的答案了
###############################################################################################
class Solution:
    def maxTurbulenceSize(self, arr) -> int:
        last = 0 # 记录arr[i-1] 和 arr[i]的关系 -1 小于 1 大于 0 等于
        cur_len = 1
        longest = 1

        for i in range(len(arr)-1):
            # 如果arr[i] 与 arr[i+1] 的大小关系 和上一对相反，则长度+1，并更新last
            if (arr[i] > arr[i+1] and last!=1) or (arr[i] < arr[i+1] and last!=-1):
                cur_len += 1
                if arr[i] > arr[i+1]:
                    last = 1
                else:
                    last = -1
            else: # 不满足条件时
                # 首先更新最长记录
                if cur_len > longest:
                    longest = cur_len
                # 然后默认将len设为2，假设的前提是 arr[i] 和 arr[i+1] 同样有大小关系，因此起步为2
                cur_len = 2
                # 判断大小关系来更新last
                if arr[i] > arr[i+1]:
                    last = 1
                elif arr[i] < arr[i+1]:
                    last = -1
                else:
                    # 若是等于的关系，len则只能为1，即从arr[i+1]开始算，last也设置为0
                    last = 0
                    cur_len = 1
        # 出来后，判断最后这一串连续的长度是否大于最长
        if cur_len > longest:
            longest = cur_len
        return longest