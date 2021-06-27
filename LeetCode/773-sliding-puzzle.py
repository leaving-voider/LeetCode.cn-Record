###############################################################################################
# 仿照【752 打开转盘锁】中用的广度搜索，独自完成此题；不过对于状态的定义有一点点问题，其实可以换成纯数字
###########
# 时间复杂度：O((mn)!*(mn)^2), 其中 m 和 n 分别是谜板的行数和列数，在本题中 m=2，n=3，谜板的状态的可能性一共有 (mn)! 种
### 每个状态需要mn的时间生成下一个状态并用mn时间枚举, seen的字符串哈希值计算需要(mn)!*22（22为状态转化为字符串的长度）
# 空间复杂度：O((mn)!*22)，队列存储所有状态需要空间复杂度 O((mn)!*22), seen哈希的消耗取决于所使用语言的哈希存储是否是元素的拷贝
### 如果是字符串，则需要空间O((mn)!*22)，和队列同数量级
###############################################################################################
class Solution:
    def slidingPuzzle(self, board) -> int:
        if board == [[1,2,3],[4,5,0]]:
            return 0
        def left(board, x0: int, y0: int):
            board[x0][y0], board[x0][y0-1] = board[x0][y0-1], board[x0][y0]
            return board
        def up(board, x0: int, y0: int):
            board[x0][y0], board[x0-1][y0] = board[x0-1][y0], board[x0][y0]
            return board
        def right(board, x0: int, y0: int):
            board[x0][y0], board[x0][y0+1] = board[x0][y0+1], board[x0][y0]
            return board
        def down(board, x0: int, y0: int):
            board[x0][y0], board[x0+1][y0] = board[x0+1][y0], board[x0][y0]
            return board
        def nextStatus(board, x0: int, y0: int):
            origin = copy.deepcopy(board)
            if x0 > 0:
                yield up(board, x0, y0), x0-1, y0
                board = copy.deepcopy(origin)
            if x0 < 1:
                yield down(board, x0, y0), x0+1, y0
                board = copy.deepcopy(origin)
            if y0 > 0:
                yield left(board, x0, y0), x0, y0-1
                board = copy.deepcopy(origin)
            if y0 < 2:
                yield right(board, x0, y0), x0, y0+1
                board = copy.deepcopy(origin)
        x0 = y0 = -1
        for x in range(2):
            for y in range(3):
                if board[x][y] == 0:
                    x0, y0 = x, y
                    break
            if x0 != -1:
                break
        queue = deque([(board, x0, y0, 0)])
        seen = {str(board)}
        while queue:
            status, x0, y0, step = queue.popleft()
            for perStatus, xnew, ynew in nextStatus(status, x0, y0):
                if str(perStatus) not in seen:
                    if perStatus == [[1,2,3],[4,5,0]]:
                        return step + 1
                    queue.append((perStatus, xnew, ynew, step+1))
                    seen.add(str(perStatus))
        return -1


## 总的来说，官方这个广度搜索的时间复杂度和我的解法差不多
## 官方的方法，修改了状态的定义，状态字符串中仅有数字，且对邻居进行定义，使得更简洁
## 把二维变成一维，免去深拷贝的操作，时间消耗大大减小；且不使用对0的位置记录的变量，每次单独计算
class Solution:
    # 对数组进行0-5的编号，0的邻居就是1、3；1的邻居就是0、2、4
    NEIGHBORS = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # 枚举 status 通过一次交换操作得到的状态
        def get(status: str) -> Generator[str, None, None]:
            s = list(status)
            x = s.index("0") # 直接找到0的位置
            for y in Solution.NEIGHBORS[x]: # 遍历每个邻居
                s[x], s[y] = s[y], s[x]
                yield "".join(s) # 生成下一个状态
                s[x], s[y] = s[y], s[x]

        # sum(board, [])即把空元素和board中的两个一维list相加，即把二维变成一维
        initial = "".join(str(num) for num in sum(board, []))
        if initial == "123450":
            return 0

        q = deque([(initial, 0)])
        seen = {initial}
        while q:
            status, step = q.popleft()
            for next_status in get(status):
                if next_status not in seen:
                    if next_status == "123450":
                        return step + 1
                    q.append((next_status, step + 1))
                    seen.add(next_status)
        return -1


## 实测发现：第一次计算0的位置，并如自己解法中那样每次传递0的位置参数，程序稍稍慢一点，或着差不多，没优化
class Solution:
    # 对数组进行0-5的编号，0的邻居就是1、3；1的邻居就是0、2、4
    NEIGHBORS = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # 枚举 status 通过一次交换操作得到的状态
        def get(status: str, x: int) -> Generator[str, None, None]:
            s = list(status)
            for y in Solution.NEIGHBORS[x]: # 遍历每个邻居
                s[x], s[y] = s[y], s[x]
                yield "".join(s), y # 生成下一个状态
                s[x], s[y] = s[y], s[x]

        # sum(board, [])即把空元素和board中的两个一维list相加，即把二维变成一维
        initial = "".join(str(num) for num in sum(board, []))
        if initial == "123450":
            return 0
        x0 = initial.index("0")
        q = deque([(initial, x0, 0)])
        seen = {initial}
        while q:
            status, x0, step = q.popleft()
            for next_status, xnew in get(status, x0):
                if next_status not in seen:
                    if next_status == "123450":
                        return step + 1
                    q.append((next_status, xnew, step + 1))
                    seen.add(next_status)
        return -1

### 留一个官方的A*算法还没看（这两天太忙，忙着毕业）