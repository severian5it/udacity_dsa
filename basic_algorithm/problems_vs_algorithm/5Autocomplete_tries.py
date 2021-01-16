## Represents a single node in the Trie
class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}

    def insert(self, node, char):
        ## Add a child node in this Trie
        self.children[char] = node

    def suffixes(self):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        suffix_list = self._suffixes_rec( '', [])
        return suffix_list

    def _suffixes_rec(self, suffix='', suffix_list=[]):
        if self.is_word and suffix:
            return suffix_list.append(suffix)

        for k,v in self.children.items():
            v._suffixes_rec(suffix + k, suffix_list)
        return suffix_list

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    ## Initialize this Trie (add a root node)

    def insert(self, word):
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
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return False

            current_node = current_node.children[char]
        return current_node

    def find_suffixes(self, prefix=''):
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

MyTrie.find_suffixes('ant')
MyTrie.find_suffixes('fun')
MyTrie.find_suffixes('tri')
MyTrie.find_suffixes('')
MyTrie.find_suffixes(None)
MyTrie.find_suffixes('stogatto')



