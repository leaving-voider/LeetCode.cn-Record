###############################################################################################
# 此题较难，参考官方方法后，比较难理解的是第2个剪枝的部分，注释中给出了自己的理解，现解释官方的意思：
# 官方剪枝2：当我们将工作 i 分配给工人 j，使得工人 j 的工作量恰好达到 limit，且计算分配下一个工作的递归函数返回了 false，
# 此时即无需尝试将工作 i 分配给其他工人，直接返回 false 即可
# 官方原因1：常规逻辑下，递归函数返回了 false，那么我们需要尝试将工作 i 分配给其他工人，假设分配给了工人 j'，那么此时工人 j'的工作量必定不多于工人 j 的工作量
### 解释：因为我们是按照工作量从大到小排序，先安排工作量大的，因此 工人j即便去掉了工作i，将其给了j'，工人j现有的工作量也一定不小于工人j'的工作量
# 官方原因2：如果存在一个方案使得分配给工人 j'能够成功完成分配任务，那么此时必然有一个或一组工作 i'取代了工作 i 被分配给工人 j，
# 否则我们可以直接将工作 i 移交给工人 j，仍然能成功完成分配任务。
### 解释：如果工人j没有工作 i'，仅仅只是把i给了 j'，那其实再把工作i拿回给工人j也一样能够分配成功的，因此一定有工作i'替代了i
# 官方原因2续：而我们知道工作 i'的总工作量不会超过工作 i，因此我们可以直接交换工作 i 与工作 i'，仍然能成功完成分配任务。
# 这与假设不符，可知不存在这样一个满足条件的工人 j'
### 解释：即便有工作i'替代了i，但这两个工作仍然可以互换，因为j是能接受i的，而i'不会多余i，因此j'也能接受i'，说明i在j处是能够分配完成的，但事实证明不能
### 因此只能说明尝试将工作 i 分配给其他工人的操作是不可行的，没必要再继续分配了
###########
# 时间复杂度：O(nlogn+log(S-M)×n!)，sorted排序时间复杂度为n*logn，S是jobs的和，M是最大的工作量，log(S-M)代表二分查找limit
# 最坏情况会遍历所有分配方案，即n!，但经过剪枝后实际不会
# 空间复杂度：O(n)，主要消耗是递归栈，递归最多n层，n代表jobs的个数
###############################################################################################
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        def backtrack(jobs, jobsSize, workloads, workloadsSize, idx, limit):
            if idx >= jobsSize:
                return True
            cur = jobs[idx]

            for i in range(workloadsSize):
                if workloads[i] + cur <= limit:
                    workloads[i] += cur
                    if (backtrack(jobs, jobsSize, workloads, workloadsSize, idx + 1, limit)):
                        return True
                    workloads[i] -= cur
                # 剪枝1：如果当前工人未被分配工作，那么下一个工人也必然未被分配工作 (如果一个人没法被分配任何工作，人人是等价的，其他人也不行)
                # 剪枝2：或者当前工作恰能使该工人的工作量达到了上限
                # （假设：若一个人i加上工作x达到上限后没法完成后面的分配，将工作x移交给另一个人j来完成整个分配，那两种情况）：
                # 1、 要么i直接不要这个工作x，这样的话在i有工作x的情况下都没法完成不超过limit的分配，现在则更不能
                # 2、 要么i获得了其他工作y，且y的工作量不会超过x，那这样其实直接把x和y工作再互换也一样能完成分配，即x工作还是能够给i，这和假设不符
                # 因此，当i获得工作x后没法完成后面的分配，那就不可能再分配成功
                # 这两种情况下我们无需尝试继续分配工作
                if workloads[i] == 0 or workloads[i] + cur == limit:
                    break
            return False
        
        def check(jobs, jobsSize, k, limit):
            workloads = [0]*k
            return backtrack(jobs, jobsSize, workloads, k, 0, limit)
        
        jobs = sorted(jobs, reverse=True)
        l = jobs[0]
        r = sum(jobs)
        jobsSize = len(jobs)
        while(l < r):
            mid = (l+r)//2
            if (check(jobs, jobsSize, k, mid)):
                r = mid
            else:
                l = mid + 1
        return l
