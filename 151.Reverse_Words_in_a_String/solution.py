class Solution:
    def reverseWords(self, s: str) -> str:
        marker = len(s)
        words = []

        # skip trailing spaces
        while marker > 0 and s[marker - 1] == ' ':
            marker -= 1

        i = marker - 1
        while i >= 0:
            if s[i] == ' ':
                if i + 1 < marker:                 # avoid empty slices
                    words.append(s[i + 1:marker])  # word after this space
                # skip the whole run of spaces
                while i >= 0 and s[i] == ' ':
                    i -= 1
                marker = i + 1
            else:
                i -= 1

        # append the first word (ignore any leading spaces)
        if marker > 0:
            j = 0
            while j < marker and s[j] == ' ':
                j += 1
            if j < marker:
                words.append(s[j:marker])

        return " ".join(words)
