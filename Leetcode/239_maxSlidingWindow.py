# 1. 循环
# 2. priority queue: 0 -> n - k: priority queue: O(NlogN)
# 3. special hack: deque, 死记硬背, 双端队列。时间复杂度：O(N)；空间复杂度：O(K)
class Solution:
    def maxSlidingWindow(self, nums, k):
        """3. deque"""
        if not nums: return []
        res, window_index = [], []
        for i, x in enumerate(nums):
            """
            1.判断元素是否超出滑动窗口范围
              i > k 说明滑动窗口不为空，window[0] < i - k说明最大元素超出了窗口，这时候必须舍弃
              队首元素：window.pop(0)
            """
            if i >= k and window_index[0] <= i - k:
                window_index.pop(0)
            """
            2.去除超出范围的元素后，这时候将当前x与滑动窗口内的队尾元素进行比较。
              如果当前元素大于或者等于队尾元素，则将队尾元素舍弃掉window.pop()，直到窗口不再有比x更小的数为止。
              注意判断window为空的情况
            """
            while window_index and nums[window_index[-1]] <= x:
                window_index.pop()
            """
            3.把当前元素放到窗口中
            """
            window_index.append(i)
            """
            4.将这次滑动中的最大值放入到结果集中
            注意是 大于等于，等于的时候，刚刚是窗口元素达到k个。这时候要计算最大值，否则会漏算。
            """
            if i >= k - 1:
                res.append(nums[window_index[0]])

        return res

    def maxSlidingWindow_1(self, nums, k):
        """循环"""
        if len(nums) == 0 and k == 0:
            return []
        res = []
        for i in range(len(nums) - k + 1):
            res.append(max(nums[i:i + k]))
        return res

    def maxSlidingWindow_2(self, nums, k):
        """优先队列"""
        import heapq
        if not nums:
            return []
        res = []
        for i in range(len(nums) - k + 1):
            result1 = heapq.nlargest(k, nums[i:i + k])
            res.append(result1[0])
        return res

