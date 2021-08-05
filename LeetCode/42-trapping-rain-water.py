###############################################################################################
# 两次遍历，每次遍历里的循环总数不会超过n，所以总的时间复杂度还是在O(n)
# 官方给了所谓的动规版和双指针版，其实思想和我的解法一样，我在正向遍历时，start就是存的i左边最高
# 因此我也反向来了一次，start存右边最高；只不过官方所谓的动规预处理了每一个位置的左右最高；而官方的双指针版
# 基本思想还是一样的，只不过做法不一样，循环次数稍微少一点；单调栈同样，存储的是一段积水的区间
###########
# 时间复杂度：O(n)
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        res = 0
        for i in range(len(height)):
            if height[i] >= height[start]: # 如果更高，那就统计，并且更新start
                for j in range(start+1, i): # 当更高的就在右边一个，则不会进入此循环统计阶段性的积水
                    res += height[start] - height[j]
                start = i # 更新高度
        # 上面一次遍历会漏掉最后一段没有更高的墙闭口的情况，因此反过来再搜一次
        re = start # 记住这个点，倒过来搜索时就到这儿，避免重复
        start = len(height) - 1
        for i in range(len(height)-1, re-1, -1): # 从右往左
            if height[i] >= height[start]:
                for j in range(start-1, i, -1):
                    res += height[start] - height[j]
                start = i # 更新高度
        return res