class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lenght = len(needle)
        for i in range(len(haystack)):

            if haystack[i] == needle[0] and haystack[i:lenght+i] == needle:
                return i

        return -1
