from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        s_len = len(s)
        
        if s_len < total_len:
            return []

        word_count = Counter(words)
        result = []

        # Iterate through possible starting offsets based on word length
        for i in range(word_len):
            left = i
            right = i
            current_count = Counter()
            count = 0

            while right + word_len <= s_len:
                word = s[right:right + word_len]
                right += word_len

                if word in word_count:
                    current_count[word] += 1
                    count += 1

                    # If a word appears more times than allowed, shrink from the left
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        count -= 1
                        left += word_len

                    # If we have matched all words, record the starting index
                    if count == num_words:
                        result.append(left)
                else:
                    # Reset the window if we encounter an invalid word
                    current_count.clear()
                    count = 0
                    left = right

        return result