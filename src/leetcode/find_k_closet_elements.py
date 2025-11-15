class Solution:
    #####
    # 658. Find K Closest Elements
    # https://leetcode.com/problems/find-k-closest-elements/description/
    #####
    def fill_result(self, lp, rp, nums, result, k, target):
        n = len(nums)
        while True:
            if len(result) == k or lp < 0 or rp > n -1:
                break
            if abs(nums[lp]-target) <= abs(nums[rp]-target):
                result.append(nums[lp])
                lp -= 1
            else:
                result.append(nums[rp])
                rp += 1
        if len(result) == k:
            return sorted(result)
        # Did not finish fill in the result because one side of date is out of range
        cap = k - len(result)
        if lp >= 0:
            result.extend(nums[lp-cap+1:lp+1])
        else:
            result.extend(nums[rp:rp+cap])
        return sorted(result)

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        l, r = 0, n - 1
        result = []
        while l <= r:
            mid = l + (r -l) // 2
            if arr[mid] == x:
                break
            elif x > arr[mid]:
                l = mid + 1
            else:
                r = mid - 1
        if l > r:
            return self.fill_result(r, l, arr, result, k, x)
        # found the target
        result.append(arr[mid])
        return self.fill_result(mid-1, mid+1, arr, result, k, x)
