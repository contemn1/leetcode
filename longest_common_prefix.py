class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        def merge(str1, str2):
            min_len = min(len(str1), len(str2))
            for i in range(min_len):
                if str1[i] != str2[i]:
                    return str1[:i]

            return str1[:min_len]

        def dc(left, right, min_len):
            if min_len == 0:
                return ""

            if right - left == 1:
                return strs[left][:min_len]

            mid = left + (right - left) // 2
            left_common = dc(left, mid, min_len)
            right_common = dc(mid, right, min(left_common, min_len))

            return merge(left_common, right_common)

        if not strs:
            return ""

        # time complexity = O(min(len(strs[i])) * log(len(strs)))
        return dc(0, len(strs), min(map(len, strs)))