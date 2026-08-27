class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        grouped_nums = defaultdict(list)
        for num in nums:
            grouped_nums[num].append(num)
        result = sorted(grouped_nums, key=lambda x:len(grouped_nums[x]),reverse = True)
        return list(result)[:k]