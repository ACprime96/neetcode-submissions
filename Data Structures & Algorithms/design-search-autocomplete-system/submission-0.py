class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isLeaf = False

class Trie:
    def __init__(self):
        self.root = TrieNode("")
    
    def add_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c)
            node = node.children[c]
        node.isLeaf = True
    
    def find(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return []
            node = node.children[c]
        res = [prefix[:-1] + x for x in self._dfs(node)]
        return res
    
    def _dfs(self, node):
        if not node:
            return []
        res = []
        for childNode in node.children.values():
            res.extend([node.val + x for x in self._dfs(childNode)])
        if node.isLeaf:
            res.append(node.val)
        return res
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        self.freq = {}
        for i,s in enumerate(sentences):
            self.trie.add_word(s)
            self.freq[s] = times[i]
        self.cur_search = ""

    def sort_options(self, options, lim = 3):
        temp = [(-self.freq[opt], opt) for opt in options]
        temp.sort()
        return [x[1] for x in temp[:lim]]

    def input(self, c: str) -> List[str]:
        self.cur_search += c
        options = self.trie.find(self.cur_search)
        return self.sort_options(options)

        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
