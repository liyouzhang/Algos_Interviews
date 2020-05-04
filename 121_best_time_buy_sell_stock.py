'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''

def max_profit(prices):
    # input - an array of int
    # output - an int >= 0
    # look for the max and min
    # if max.index > min.index:
        # return max-min
    # else:
        # split the array into three parts. first parts end w max
        # look for the min in the max and assing as diff1
        # second parts start with min and look for max, count the diff as diff2
        # the num in middle find max min and count as diff3 
    # compare diff 1, 2, 3 and if > 0
        # return largest
    # else return 0 
    max_num = max(prices)
    min_num = min(prices)
    if prices.index(max_num) > prices.index(min_num) and (max_num - min_num) > 0:
        return max_num-min_num
    else:
        if prices.index(max_num) != 0:
            part1 = prices[::prices.index(max_num)] # cannot list[::0]
            diff1 = max_num - min(part1)
        else:
            diff1 = 0
        part2 = prices[prices.index(min_num)::]
        diff2 = max(part2) - min_num
        if prices.index(min_num) - prices.index(max_num) >= 2:
            part3 = prices[prices.index(max_num)+1:prices.index(min_num)] # note list [0:2] is [0 and 2)
            # diff3 = max(part3) - min (part3) # didn't consider the index!
            if part3.index(max(part3)) > part3.index(min(part3)):
                diff3 = max(part3) - min(part3)
            else:
                diff3 = max_profit(part3) #recursion!
        else:
            diff3 = 0
    if max(diff1,diff2,diff3) > 0:
        return max(diff1,diff2,diff3)
    else:
        return 


# elegant solution!
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        res = 0
        min_seen = prices[0]
        for p in prices[1:]:
            if p > min_seen:
                res = max(res, p - min_seen)
            else:
                min_seen = p
        return res
# solutions
# Brute Force :O(N^2)
    if not len(prices):
        return 0
	ans = []
    for i, v in enumerate(prices):
        ans += [j-v for j in prices[i:] if j >= v]
    return max(ans)

    # two pointers :O(N)
    if not len(prices):
        return 0
	n = len(prices)
    i = 0
    ans = 0
    for j in range(n):
        while prices[i] > prices[j]:
            i += 1
            if i == j:
                break
        ans = max(ans, prices[j]-prices[i])
    return ans
    
    # Greedy :O(N)
    if not len(prices):
        return 0
	minimum = float("inf")
    ans = [0]
    for v in prices:
        ans.append(v-minimum)
        minimum = min(minimum, v)
    return max(ans)