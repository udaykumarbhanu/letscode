"""LC: 262. Reverse Words in a String II
Given an input string, reverse the string word by word. A word is defined as a
sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are
always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space?
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        if not s: return s

        s_lst = s.split(" ")
        s_lst.reverse()

        return " ".join(s_lst)


if __name__ == '__main__':
    s = "the sky is blue"
    print Solution().reverseWords(s)
