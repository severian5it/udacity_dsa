# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode(object):
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.is_leaf = False
        self.children = {}
        self.handler= handler

    def insert(self, node, path):
        # Insert the node as before
        self.children[path] = node

# A RouteTrie will store our routes and their associated handlers
class RouteTrie(object):
    def __init__(self, handler=None):
        self.root = RouteTrieNode(handler)

    def insert(self, path_element, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
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
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
            current_node = self.root
            for p in path_element:
                if p not in current_node.children:
                    return False

                current_node = current_node.children[p]
            return current_node

# The Router class will wrap the Trie and handle
class Router(object):
    def __init__(self, root, hand_404):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routeTrie = RouteTrie()
        self.routeTrie.insert('/', root)
        self.notfound = hand_404


    def add_handler(self,path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        if not path:
            return "please specify path"

        path_element = self.split_path(path)
        self.routeTrie.insert(path_element, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if not path:
            return "please specify path"
        path_element = self.split_path(path)
        node = self.routeTrie.find(path_element)

        if node and node.is_leaf:
            return node.handler
        else:
            return self.notfound

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if path == '/':
            return [path]

        if path[-1] == '/':
            path = path[:-1]

        path_element = path.split('/')

        return path_element

        # Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler","not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup(None))  # should print 'not found handler' or None if you did not implement one