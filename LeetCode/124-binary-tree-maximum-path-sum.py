###############################################################################################
# 暴搜超时, 以每个点为起点，进行DFS
###########
# 时间复杂度：O(n^2)
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        N = int(3e4+10)
        h = defaultdict(list)

        def insert(a, b):
            h[a].append(b)
        
        stack = [root]
        while stack:
            t = stack.pop()
            if t.left:
                insert(t, t.left)
                insert(t.left, t)
                stack.append(t.left)
            if t.right:
                insert(t, t.right)
                insert(t.right, t)
                stack.append(t.right)

        def search(u, valsum, st):
            st[u] = 1
            nonlocal max_
            max_ = max(max_, valsum)

            for nex in h[u]:
                if not st[nex]:
                    search(nex, valsum+nex.val, st)

        res = float("-inf")
        max_ = float("-inf")
        def dfs(u):
            if not u:
                return

            st = defaultdict(int)
            nonlocal max_
            max_ = float("-inf")
            search(u, u.val, st)
            nonlocal res
            res = max(res, max_)

            dfs(u.left)
            dfs(u.right)
        dfs(root)
        return res


###############################################################################################
# 确实有点难想，参考官方，主要思路是求解最右儿子的最大贡献值，然后加上自己的值就是通过自己的最大路径和
# 然后递归处理两边，这样就计算了不经过该根节点的最大路径和
###########
# 时间复杂度：O(n)
# 空间复杂度：O(n),最大递归可能为n，比如一根整链
###############################################################################################
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = float("-inf")
        def dfs(u):
            nonlocal res
            if not u:
                return 0
            leftgain = max(dfs(u.left), 0) # 返回以左儿子为根节点的最大贡献值，最大贡献值为负值就当0来算，即不加这个点
            rightgain = max(dfs(u.right), 0)
            # 求解的是左右最大贡献值+自己的值，即以自己为根节点的最大路径和
            res = max(res, u.val + leftgain + rightgain)
            # 返回的是最大贡献值，之所以不返回以自己为根节点的最大路径和，是因为一个点只能走一次
            # 而以自己为根节点的最大路径可能跨了左右两边，如果被上层加上去，就一点多走了
            return u.val + max(leftgain, rightgain)
        dfs(root)
        return res