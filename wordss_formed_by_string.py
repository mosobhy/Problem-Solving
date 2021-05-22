class Solution:
    def countCharacters(self, words, chars):
        found_words = []
        for word in words:
            for char in word:
                if char not in chars:
                    break
                else:
                    if word.index(char) == len(word) - 1:
                        found_words.append(word)
        return len([word for word in found_words for char in word])

s = Solution()
print(s.countCharacters(["hello","world","leetcode"], "welldonehoneyr"))
