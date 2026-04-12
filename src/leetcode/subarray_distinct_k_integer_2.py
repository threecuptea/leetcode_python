from collections import Counter
class Solution:
    def countSubarrays(self, nums: list[int], k: int, m: int) -> int:
        size, n, result = k * m, len(nums), 0
        if n < size:
            return 0
        total_counter = Counter(nums)
        # special case
        if len(total_counter) == 1 and list(total_counter.values())[0] == n and k == 1 and m == 1:
            return int((1 + n) * n / 2)
        for start in range(n - size + 1):
            counter = Counter(nums[start:(start + size)])
            for end in range(start + size, n + 1):
                if end > start + size:
                    counter[nums[end - 1]] += 1
                if len(counter) == k and all(value >= m for value in counter.values()):
                    result += 1
                elif len(counter) > k:
                    break
        return result