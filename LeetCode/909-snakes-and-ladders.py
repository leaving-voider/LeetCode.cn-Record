###############################################################################################
# 同样广度搜索，需要注意题目中所说的【每个回合最多爬一次】和【整个游戏最多爬一次】不一样；
# 且需要注意，广度搜索，最先到达某个location所用的step一定是最小的，所以直接记录walked即可
###########
# 时间复杂度：O(n^2), n 是board边长，因为每个位置只走第一次，所以遍历一遍下来只遍历了n^2个状态，对于每个状态查找下面6步并遍历，在此题中可省略该复杂度，因为数量级没增大
# 空间复杂度：O(n^2)，存储队列和walked哈希，状态都是数字，因此总的需求也就n^2
###############################################################################################
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        len_ = len(board)*len(board[0])
        self.board = sum([line[::-1] if i%2==1 else line for i, line in enumerate(board[::-1])], [])
        def getNextStep(location: int) -> Generator[int, None, None]:
            for i in range(1, 7):
                if location + i - 1 > len_ - 1:
                    break
                if self.board[location + i - 1] != -1: # 【每回合的前进过程中最多只能爬过蛇或梯子一次】，并不是说整个游戏都只能一次，只是不能一直跳
                    yield self.board[location + i - 1]
                else:
                    yield location + i
        
        queue = deque([(1, 0)]) # 在位置1，已走0步
        walked = {1} # 可以证明，第一次到达某个位置的step一定是最小的
        while queue:
            location, step = queue.popleft()
            for nextLocation in getNextStep(location):
                if nextLocation == len_:
                    return step + 1
                if nextLocation not in walked:
                    queue.append((nextLocation, step+1))
                    walked.add(nextLocation)
        return -1