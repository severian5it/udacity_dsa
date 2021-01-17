class RouteTrieNode(object):
    def __init__(self, handler=None):
        self.is_leaf = False
        self.children = {}
        self.handler= handler

    def insert(self, node, path):
        # Insert the node with path
        self.children[path] = node


class RouteTrie(object):
    def __init__(self, handler=None):
        self.root = RouteTrieNode(handler)

    def insert(self, path_element, handler):
        # insert node with path as list and handler
        current_node = self.root
        for p in path_element:
            if p not in current_node.children:
                node = RouteTrieNode()
                current_node.insert(node, p)
                current_node = node
            else:
                current_node = current_node.children[p]
        current_node.is_leaf = True
        current_node.handler = handler

    def find(self, path_element):
        # find a path element
            current_node = self.root
            for p in path_element:
                if p not in current_node.children:
                    return False

                current_node = current_node.children[p]
            return current_node


class Router(object):
    def __init__(self, root, hand_404):
        self.routeTrie = RouteTrie()
        self.routeTrie.insert('/', root)
        self.notfound = hand_404

    def add_handler(self,path, handler):
        # add handler to the trie
        if not path:
            return "please specify path"

        path_element = self.split_path(path)
        self.routeTrie.insert(path_element, handler)

    def lookup(self, path):
        # lookup for path
        if not path:
            return "please specify path"
        path_element = self.split_path(path)
        node = self.routeTrie.find(path_element)

        if node and node.is_leaf:
            return node.handler
        else:
            return self.notfound

    def split_path(self, path):
        # split a path into a list.
        if path == '/':
            return [path]

        if path[-1] == '/':
            path = path[:-1]

        path_element = path.split('/')

        return path_element


router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes

# Edge and corner case
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup(None))  # should print 'not found handler' or None if you did not implement one