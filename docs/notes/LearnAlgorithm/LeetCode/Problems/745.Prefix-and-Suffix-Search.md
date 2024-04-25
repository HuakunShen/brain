# 745. Prefix and Suffix Search

## Python

Both of the 2 following python solutions timed out.

```python
from typing import List


class Node:
    def __init__(self, value):
        self.indices = set()
        self.value = value
        self.children = {}
        
class Tree:
    def __init__(self):
        self.root = Node(None)
    
    @staticmethod
    def add_word(i: int, node: Node, word: str):
        if len(word) != 0:
            if word[0] in node.children:
                next_node = node.children[word[0]]
                next_node.indices.add(i)
                Tree.add_word(i, next_node, word[1:])
            else:
                new_node = Node(word[0])
                new_node.indices.add(i)
                node.children[word[0]] = new_node
                Tree.add_word(i, new_node, word[1:])
        else:
            return
    
    @staticmethod
    def find_fix_indices(fix: str, node: Node) -> set:
        if len(fix) == 1:
            if fix[0] in node.children:
                return node.children[fix[0]].indices
        else:
            if fix[0] in node.children:
                return Tree.find_fix_indices(fix[1:], node.children[fix[0]])
        return set()
        
    
        

class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        self.prefix_tree = Tree()
        self.suffix_tree = Tree()
        for i, word in enumerate(self.words):
            Tree.add_word(i, self.prefix_tree.root, word)
            Tree.add_word(i, self.suffix_tree.root, word[::-1])
    

    def f(self, prefix: str, suffix: str) -> int:
        prefix_indices = Tree.find_fix_indices(prefix, self.prefix_tree.root)
        suffix_indices = Tree.find_fix_indices(suffix[::-1], self.suffix_tree.root)
        if len(prefix_indices) < 1 or len(suffix_indices) < 1:
            return -1
        return max(prefix_indices & suffix_indices)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)

```

Two trees are created to store both forward direction and backward direction word.

I call them prefix_tree and suffix_tree.

Then traverse the 2 trees with given prefix and suffix.

```python
class Node:
    def __init__(self, value):
        self.indices = set()
        self.value = value
        self.children = {}
        
class Tree:
    def __init__(self):
        self.root = Node(None)
    
    @staticmethod
    def add_word(i: int, node: Node, word: str):
        if len(word) != 0:
            if word[0] in node.children:
                next_node = node.children[word[0]]
                next_node.indices.add(i)
                Tree.add_word(i, next_node, word[1:])
            else:
                new_node = Node(word[0])
                new_node.indices.add(i)
                node.children[word[0]] = new_node
                Tree.add_word(i, new_node, word[1:])
        else:
            return
    
    @staticmethod
    def find_fix_indices(fix: str, node: Node) -> set:
        if len(fix) == 1:
            if fix[0] in node.children:
                return node.children[fix[0]].indices
        else:
            if fix[0] in node.children:
                return Tree.find_fix_indices(fix[1:], node.children[fix[0]])
        return set()
        
    
        

class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        self.prefix_tree = Tree()
        self.suffix_tree = Tree()
        for i, word in enumerate(self.words):
            Tree.add_word(i, self.prefix_tree.root, word)
            Tree.add_word(i, self.suffix_tree.root, word[::-1])
    

    def f(self, prefix: str, suffix: str) -> int:
        prefix_indices = Tree.find_fix_indices(prefix, self.prefix_tree.root)
        suffix_indices = Tree.find_fix_indices(suffix[::-1], self.suffix_tree.root)
        if len(prefix_indices) < 1 or len(suffix_indices) < 1:
            return -1
        return max(prefix_indices & suffix_indices)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
```

Similar to Solution 1, We use a single tree, the key for children is the combination of 2 letters (forward and backward direction).

e.g.
```
abcd
dcba
```
Keys:
- ad
- bc
- cb
- da

```python
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

```

A solution copied from discussion.

Very special & smart & tricky solution. Use the debugger to find out.