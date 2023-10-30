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