import collections

Trie = lambda: collections.defaultdict(Trie)


class WordFilter:
    def __init__(self, words):
        self.trie = Trie()

        for weight, word in enumerate(words):
            for i in range(len(word) + 1):
                node = self.trie
                node['weight'] = weight
                word_to_insert = word[i:] + '#' + word
                for c in word_to_insert:
                    node = node[c]
                    node['weight'] = weight

    def f(self, prefix, suffix):
        node = self.trie
        for c in suffix + '#' + prefix:
            if c not in node: return -1
            node = node[c]
        return node['weight']


if __name__ == '__main__':
    obj = WordFilter(["apple"])
    param_1 = obj.f("a", "e")
