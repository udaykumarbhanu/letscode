"""LC 22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        #edge case.
        if not n or n == 0: return result

        self.backtrack(n, n, result, "")
        return result

    def backtrack(self, left_paretheses_needed, right_paretheses_needed, result, temp):
        if left_paretheses_needed == 0 and right_paretheses_needed == 0:
            result.append(temp)
            return

        if left_paretheses_needed > 0:
            self.backtrack(left_paretheses_needed-1, right_paretheses_needed, result, temp + "(")

        if left_paretheses_needed < right_paretheses_needed:
            self.backtrack(left_paretheses_needed, right_paretheses_needed-1, result, temp + ")")

if __name__ == '__main__':
    n = 3
    print Solution().generateParenthesis(n)
