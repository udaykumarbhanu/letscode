"""GS online test question.
https://bit.ly/33H15CN
"""
class Solution(object):
    def numberChecker(self, nums, req_digits):
        result = []

        if not nums: return result

        nums.sort()
        for num in nums:
            if set(str(req_digits)).issubset(set(str(num))):
                result.append(num)

        return result

if __name__ == '__main__':
    nums =[1456, 345671, 43218, 123]
    req_digits = 123
    print Solution().numberChecker(nums, req_digits)
