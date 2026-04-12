from collections import Counter, defaultdict
class Solution:
    def countSubarrays(self, nums: list[int], k: int, m: int) -> int:
        NOT_YET, QUALIFIED, DISQUAL = 0, 1, 2
        def check_incremental_status(orig_dict, num):
            tmp = orig_dict.copy()
            tmp[num] += 1
            if len(tmp) == k and all(value >= m for value in tmp.values()):
                return tmp, QUALIFIED
            if len(tmp) > k:
                return None, DISQUAL
            return tmp, NOT_YET

        size, n, result = k * m, len(nums), 0
        if n < size:
            return 0
        total_counter = Counter(nums)
        if len(total_counter) == 1 and list(total_counter.values())[0] == n and k == 1 and m == 1:
            return int((1 + n) * n / 2)
        l = 0  # try sliding window
        while l <= n - size:
            counter = Counter(nums[l:])
            # shortcut, check the counter overall
            if len(counter) < k:
                # No need to check the current l loop or l + 1 etc. loop.  No way to qualify
                break
            cnt_dict = defaultdict(int)
            for r in range(l, n):
                num = nums[r]
                inc_dict, status = check_incremental_status(cnt_dict, num)
                if status == DISQUAL:
                    cnt_dict[nums[l]] -= 1
                    # if nums[l] == nums[r] then k won't increase
                    if cnt_dict[nums[l]] == 0:
                        del cnt_dict[nums[l]]
                    # move the sliding window
                    l += 1
                    cnt_dict[num] += 1
                    if len(cnt_dict) == k and all(value >= m for value in cnt_dict.values()):
                        result += 1
                else:
                    cnt_dict = inc_dict
                    if status == QUALIFIED:
                        result += 1
            l += 1
        return result