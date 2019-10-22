# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
#
# Each letter in the magazine string can only be used once in your ransom note.
#
# Note:
# You may assume that both strings contain only lowercase letters.

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        notes = collections.defaultdict(self.init)
        mags = collections.defaultdict(self.init)
        for each in ransomNote:
            notes[each] += 1
        for each in magazine:
            mags[each] += 1

        for key in notes.keys():
            if key not in mags:
                return False
            if mags[key] < notes[key]:
                return False
        return True

    def init(self):
        return 0
