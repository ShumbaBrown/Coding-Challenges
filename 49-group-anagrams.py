# Given an array of strings, group anagrams together.
#


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        words = collections.defaultdict(list)
        ans = list()
        for each in strs:
            copy = str(sorted(each))
            words[copy].append(each)
        for each in list(words.keys()):
            ans.append(words[each])

        return ans
            
