from collections import Counter
from typing import List


class Solution:
    p1 = 0
    p2 = 0

    def findAnagrams(self, s: str, p: str) -> List[int]:
        count, n_s, n_p = Counter(p), len(s), len(p)
        self.p1, self.p2 = 0, n_p - 1
        result = []
        window_count = Counter(s[self.p1:self.p2 + 1])

        def run():
            if count == window_count:
                result.append(self.p1)
            self.p1 += 1
            self.p2 += 1
            if self.p2 == n_s:
                return
            if s[self.p1] in window_count:
                window_count[s[self.p1]] -= 1
            if s[self.p2] in window_count:
                window_count[s[self.p2]] += 1

        run()
        while self.p2 < n_s:
            run()


if __name__ == '__main__':
    sol = Solution()
    sol.findAnagrams("bpaa", "aa")
