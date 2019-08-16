'''LC: 168. Excel Sheet Column Title
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
'''
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if not n: return ''

        letters = [chr(i) for i in range(ord('A'), ord('Z')+1)]
        if n <= 26: return letters[n-1]
        result = []

        while n:
            result.append(letters[(n-1)%26])
            n = (n-1)/26

        result.reverse()
        return ''.join(result)

if __name__ == '__main__':
    n = 52
    print Solution().convertToTitle(n)
