class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}

    def insert(self, node, char):
        self.children[char] = node

    def suffixes(self):
        # face function
        suffix_list = self._suffixes_rec('', [])
        return suffix_list

    def _suffixes_rec(self, suffix='', suffix_list=[]):
        # recursive function to find suffices
        if self.is_word and suffix:
            suffix_list.append(suffix)

        if not self.children:
            return suffix_list

        for k,v in self.children.items():
            v._suffixes_rec(suffix + k, suffix_list)
        return suffix_list

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        # insert word in trie
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                node = TrieNode()
                current_node.insert(node, char)
                current_node = node
            else:
                current_node = current_node.children[char]
        current_node.is_word = True

    def find(self, prefix):
        # find prefix in trie
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return False

            current_node = current_node.children[char]
        return current_node

    def find_suffices(self, prefix=''):
        # find suffices
        if not prefix:
            print('please specify a prefix')
            return

        current_node = self.find(prefix)
        if current_node:
            print(f"list of suffixes is {current_node.suffixes()}")
        else:
            print(prefix + " not found")


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

MyTrie.find_suffices('ant')
MyTrie.find_suffices('fun')
MyTrie.find_suffices('tri')
MyTrie.find_suffices('an')
MyTrie.find_suffices('t')

# Edge case
MyTrie.find_suffices('')
MyTrie.find_suffices(None)
MyTrie.find_suffices('stogatto')



