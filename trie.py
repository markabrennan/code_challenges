"""
Practice with implementing
a trie data structure.
Taking some code from various
references and re-coding for practice.
"""

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.counter = 0
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
        node.counter += 1

    def query(self, prefix):
        self.output = []
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        self.dfs(node, prefix[:-1])

        return sorted(self.output, key=lambda x: x[1], reverse=True)

    def dfs(self, node, prefix):
        if node.is_end:
           self.output.append((prefix + node.char, node.counter))

        for child in node.children.values():
            self.dfs(child, prefix + node.char) 

    def search(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return True

    def starts_with(self, prefix):
        return self.search(prefix)



"""
TEST CASES
"""
trie = Trie()
trie.insert("was")
trie.insert("word")
trie.insert("war")
trie.insert("what")
trie.insert("where")

print(trie.query("wh"))

print(trie.search("war"))
print(trie.search("whereas"))
print(trie.search('wh'))

print(trie.starts_with("wher"))
print(trie.starts_with('app'))