class Solution:
    ######
    # 72. Edit Distance
    # https://leetcode.com/problems/edit-distance/description/
    ######
    def minDistance(self, word1: str, word2: str) -> int:
        # word1 is row and word2 is column
        # w2    a  c  d
        # w1 a  1  2  1  3
        #    b  2  1  1  2
        #    d  1  1  0  1
        #       3  2  1  0

        # w2.   r  o  s
        # w1 h  3  3  4  5
        #    o  3  2  3  4
        #    r  2  3  2  3
        #    s  3  2  1  2
        #    e  3  2  1  1
        #       3  2  1  0
        # The best route from the bottom up:
        # 0 -> 1 (delete 'e') -> 1 (keep 's) -> 2 (delete 'r) -> 2 (keep 'o') -> 3 (replace 'h' with 'r')
        # inspired by neetcode https://www.youtube.com/watch?v=XYi2-LPrwm4
        cache = [[float('inf') for _ in range(len(word2)+ 1)] for _ in range(len(word1)+ 1)]
        # populate row len(word1)
        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j
        # populate column len(word2), duplicately populate cache[len(word1)][len(word2)]
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i
        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    cache[i][j] = 1 + min(cache[i+1][j+1], cache[i+1][j], cache[i][j+1])

        return cache[0][0]