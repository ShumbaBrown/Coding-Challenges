class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        L = len(beginWord)

        # Find all combination of words that can be formed from each word.
        all_combo_dict = dict()
        for word in wordList:
            for i in range(L):
                comb = word[:i] + "*" + word[i+1:]
                if comb not in all_combo_dict:
                    all_combo_dict[comb] = [word]
                else:
                    all_combo_dict[comb].append(word)

        queue = collections.deque([(beginWord, 1)])
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]
                if intermediate_word in all_combo_dict:
                    for word in all_combo_dict[intermediate_word]:
                        if word == endWord:
                            return level + 1
                        if word not in visited:
                            visited[word] = True
                            queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0
