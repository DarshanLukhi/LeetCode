# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = temp = 0
        index_map = {}

        for index in range(len(s)):
            if s[index] in index_map:
                temp = max(temp, index_map[s[index]])

            answer = max(answer, index - temp + 1)
            index_map[s[index]] = index + 1

        return answer
