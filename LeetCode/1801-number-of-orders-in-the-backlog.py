###############################################################################################
# 堆优化 + 遍历
###########
# 时间复杂度：O(n)
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy = []
        sell = []
        amount_buy = amount_sell = 0
        mod = int(1e9 + 7)
        for price, amount, orderType in orders:
            if orderType == 0: # 买
                while amount and sell and sell[0][0] <= price:
                    if amount < sell[0][1]: # 买够了
                        sell[0][1] -= amount
                        amount_sell -= amount
                        amount -= amount # 所需amount清0
                    elif amount == sell[0][1]: # 正好买完
                        amount_sell -= sell[0][1]
                        amount -= amount # 所需amount清0
                        heapq.heappop(sell)
                    else: # 不够买
                        amount_sell -= sell[0][1]
                        amount -= sell[0][1] # 不够买，看下一家
                        heapq.heappop(sell)
                if amount: # 如果还没买够
                    heapq.heappush(buy, [-price, amount])
                    amount_buy += amount
            else: # 卖
                while amount and buy and -buy[0][0] >= price:
                    if amount < buy[0][1]: # 全部卖完
                        buy[0][1] -= amount
                        amount_buy -= amount
                        amount -= amount # 要卖amount清0
                    elif amount == buy[0][1]: # 正好卖完 
                        amount_buy -= buy[0][1]
                        amount -= amount # 要卖amount清0
                        heapq.heappop(buy)
                    else: # 还没卖完
                        amount_buy -= buy[0][1]
                        amount -= buy[0][1] # 不够卖，看下一家
                        heapq.heappop(buy)
                if amount:
                    heapq.heappush(sell, [price, amount])
                    amount_sell += amount
        return (amount_sell + amount_buy) % mod
        