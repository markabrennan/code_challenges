"""
Second attempt to implement trie data structure.
Attempt to replicate from trie.py, except
by memory!
"""

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True

    def search(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return len(node.children) == 0 or node.is_end

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return True

            


"""
TEST CASES
"""

t = Trie()
t.insert("was")
t.insert("war")

t.insert("apple")

print(t.search("apple"))
print(t.starts_with("app"))
print(t.starts_with("wa"))
print(t.search("war"))

print(t.search("wart"))
print(f'search: app: {t.search("app")}')

print(t.starts_with("app"))

t.insert("app")
print(f'search: app: {t.search("app")}')


