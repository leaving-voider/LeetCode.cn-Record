###############################################################################################
# 自己本打算使用深度搜索，但不如广度方便，比如当找到一个可以的状态，如果此时使用的是广度搜索，那么可以
# 直接返回step，因为广度搜索中第一个遇到的ok的状态一定是所需step最少的；因此参考官方的方法
###########
# 时间复杂度：O(b^d*d^2+md), 其中 b 是数字的进制，d 是转盘数字的位数，m 是数组 deadends 的长度，在本题中 b=10，d=4，
## 转盘数字的可能性一共有 b^d 种，即搜索到的状态数上限；而对于每个状态，需要O(d)枚举每个【下一个状态】并加入序列，且
## 需要O(d)的时间生成这些状态（getStatus函数）；此题中，将 deadends 中的所有元素放入哈希表中，计算字符串哈希值需要时间为O(d) - 不论什么语言都是这样
## 以上为官方分析，个人认为，因为是字符串，那 seen 哈希表插入的字符串也应该需要消耗 O(b^d*d) 的时间，不过这个可以合并忽略，m大小未知，不能合并忽略
# 空间复杂度：O(b^d*d+m)，队列存储所有状态需要空间复杂度 O(b^d*d), seen的消耗和队列同数量级
## dead 哈希表的消耗为 O(m), 如果使用的语言存储的是元素的拷贝，即字符串，那么需要的空间为 O(md)
###############################################################################################
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0

        dead = set(deadends)
        if "0000" in dead:
            return -1
        
        def next_status(ch: str) -> str:
            return "0" if ch == "9" else str(int(ch) + 1)
        
        def prev_status(ch: str) -> str:
            return "9" if ch == "0" else str(int(ch) - 1)

        def getStatus(status: str) -> Generator[str, None, None]: # YieldType、SendType、ReturnType
            li = list(status)
            for i in range(4):
                this_ = li[i]
                li[i] = next_status(this_)
                yield "".join(li)
                li[i] = prev_status(this_)
                yield "".join(li)
                li[i] = this_
        
        queue = deque([("0000", 0)]) # 第一个为状态，第二个为步数;from collections import deque
        seen = {"0000"} # 记录走过的状态，可减少大量重复
        while queue:
            status, step = queue.popleft()
            for perStatus in getStatus(status):
                if perStatus not in seen and perStatus not in dead:
                    if perStatus == target:
                        return step + 1
                    queue.append((perStatus, step+1))
                    seen.add(perStatus)
        return -1 # 如果到了这儿说明没有找到满足的状态


### 留一个官方的A*算法还没看（这两天太忙，忙着毕业）