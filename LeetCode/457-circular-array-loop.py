###############################################################################################
# 一次遍历即可，不过需要考虑下一个点的情况
# 1、落脚点的行走方向和当前circle相反
# 2、下一个点已经走到以i为起点走过的区域内，则要计算循环长度，如果大于1就成功了，否则就退出，起点i设置为无效起点，任何点走到这儿都不会有好结果
# 实际上2只是个优化，不用也可以。只是为了防止更多无效循环，但真要优化的话，从无效起点i开始的每个点，都是无效点，因为他们都不能得到有效circle
# 并且每个能到达无效点的点，也同样是无效点，这一点也能优化
# 3、当下一步的方向和当前circle相同，且还没走到以i为起点走过的区域，则继续下一个
###########
# 时间复杂度：O(n)，虽然里面有个循环，但当加入优化后，实际上每个点只会被访问一次
# 空间复杂度：O(n)，存走过的点
###############################################################################################
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        len_ = len(nums)
        steped = set() # 存储走过的且不能导致有效循环的index
        for i in range(len_):
            j, k = i, 0 # j,k,flag 走的每一个位置，当前已走了多少个点
            flag = 1 if nums[j] > 0 else 0 # 1正向0反向
            steped.add(j) # 默认加入无效起点
            cur = defaultdict(int)
            while 1:
                k += 1
                cur[j] = k-1 # 标注第几个，从0记
                j = (j + nums[j]) % len_
                if (nums[j] > 0 and not flag) or (nums[j] < 0 and flag): # 下一个和当前circle反向
                    break
                if j in cur: # 说明走了个圈了
                    if k-cur[j] > 1:
                        return True
                    break
                if j in steped: # 说明走到无效起点了
                    break
        return False

# 0优化
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        len_ = len(nums)
        for i in range(len_):
            j, k = i, 0 # j,k,flag 走的每一个位置，当前已走了多少个点
            flag = 1 if nums[j] > 0 else 0 # 1正向0反向
            cur = defaultdict(int)
            while 1:
                k += 1
                cur[j] = k-1 # 标注第几个，从0记
                j = (j + nums[j]) % len_
                if (nums[j] > 0 and not flag) or (nums[j] < 0 and flag): # 下一个和当前circle反向
                    break
                if j in cur: # 说明走了个圈了
                    if k-cur[j] > 1: # 可能不是到达起点i，而是中间的某个部分，所以长度不一定为k
                        return True
                    break
        return False

# 无效点优化
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        len_ = len(nums)
        steped = set() # 存储走过的且不能导致有效循环的index
        for i in range(len_):
            j, k = i, 0 # j,k,flag 走的每一个位置，当前已走了多少个点
            flag = 1 if nums[j] > 0 else 0 # 1正向0反向
            steped.add(j) # 默认加入无效起点
            cur = defaultdict(int)
            while 1:
                k += 1
                cur[j] = k-1 # 标注第几个，从0记
                j = (j + nums[j]) % len_
                if (nums[j] > 0 and not flag) or (nums[j] < 0 and flag): # 下一个和当前circle反向
                    break
                if j in cur: # 说明走了个圈了
                    if k-cur[j] > 1:
                        return True
                    for key in cur:
                        steped.add(key) # 全部加入无效点行列
                    break
                if j in steped: # 说明走到无效点了
                    for key in cur:
                        steped.add(key) # 每个能到达无效点的点也都是无效点
                    break
        return False

# 上面即便优化了无效点，但实际的时间消耗还是大，原因是不是set多了一个，也不是while嵌套for的问题，没这种玄学
# 只是因为当遇到反向的点时，我们没有把前面的点加入无效点，这里的优化也很重要
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        len_ = len(nums)
        steped = set() # 存储走过的且不能导致有效循环的index
        for i in range(len_):
            j, k = i, 0 # j,k,flag 走的每一个位置，当前已走了多少个点
            flag = 1 if nums[j] > 0 else 0 # 1正向0反向
            steped.add(j) # 默认加入无效起点
            cur = defaultdict(int)
            while 1:
                k += 1
                cur[j] = k-1 # 标注第几个，从0记
                j = (j + nums[j]) % len_
                if (nums[j] > 0 and not flag) or (nums[j] < 0 and flag): # 下一个和当前circle反向
                    for key in cur:
                        steped.add(key) # 全部加入无效点行列
                    break
                if j in cur: # 说明走了个圈了
                    if k-cur[j] > 1:
                        return True
                    for key in cur:
                        steped.add(key) # 全部加入无效点行列
                    break
                if j in steped: # 说明走到无效点了
                    for key in cur:
                        steped.add(key) # 每个能到达无效点的点也都是无效点
                    break
        return False

# 这里参考官方的直接去掉steped，走过的点都把其nums[i]置0就表示无效点了
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        len_ = len(nums)
        for i in range(len_):
            j, k = i, 0 # j,k,flag 走的每一个位置，当前已走了多少个点
            flag = 1 if nums[j] > 0 else 0 # 1正向0反向
            cur = defaultdict(int)
            while 1:
                if nums[j] == 0: # 说明走到无效点了
                    break
                k += 1
                cur[j] = k-1 # 标注第几个，从0记
                j = (j + nums[j]) % len_
                if (nums[j] > 0 and not flag) or (nums[j] < 0 and flag): # 下一个和当前circle反向
                    break
                if j in cur: # 说明走了个圈了
                    if k-cur[j] > 1:
                        return True
                    break
            for key in cur:
                nums[key] = 0 # 所有点都变成无效点
        return False

# 仍然使用steped也可以的，就把加入无效点的操作放到while外面，免得看起来冗余，时间消耗一样大大减少
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        len_ = len(nums)
        steped = set() # 存储走过的且不能导致有效循环的index
        for i in range(len_):
            j, k = i, 0 # j,k,flag 走的每一个位置，当前已走了多少个点
            flag = 1 if nums[j] > 0 else 0 # 1正向0反向
            cur = defaultdict(int)
            while 1:
                k += 1
                cur[j] = k-1 # 标注第几个，从0记
                j = (j + nums[j]) % len_
                if (nums[j] > 0 and not flag) or (nums[j] < 0 and flag): # 下一个和当前circle反向
                    break
                if j in cur: # 说明走了个圈了
                    if k-cur[j] > 1:
                        return True
                    break
                if j in steped: # 说明走到无效点了
                    break
            for key in cur:
                steped.add(key) # 全部加入无效点行列
        return False