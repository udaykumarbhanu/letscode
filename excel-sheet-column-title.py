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
