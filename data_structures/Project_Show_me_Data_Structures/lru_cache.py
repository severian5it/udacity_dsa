class Node(object):
    def __init__(self, node_key, val):
        self.node_key = node_key
        self.val = val
        self.next = None
        self.prev = None


class LRU_Cache(object):
    def __init__(self, max_size=5):
        self.head = Node('head', 'head')
        self.tail = Node('tail', 'tail')
        self.head.next = self.tail
        self.tail.prev = self.head
        self.max_size = max_size
        self.curr_size = 0
        self.node_lookup = {}

    def remove_node(self, node):
        """ Remove Node """
        node_after = node.next
        node_before = node.prev
        node_before.next = node_after
        node_after.prev = node_before

    def move_to_end(self, node):
        """ Move a Node before the tail """
        prev_node_tail = self.tail.prev
        prev_node_tail.next = node
        node.prev = prev_node_tail
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        """ Cache get """
        if key not in self.node_lookup:
            # cache miss
            return -1
        # cache hit
        node = self.node_lookup[key]
        node_val = node.val
        self.remove_node(node)
        self.move_to_end(node)
        return node_val

    def set(self, key, val):
        """ Cache set """
        if key in self.node_lookup:
            # is in Cache, move it to the end.
            node = self.node_lookup[key]
            node.val = val
            self.remove_node(node)
            self.move_to_end(node)
        else:
            if self.curr_size >= self.max_size:
                lru_node = self.head.next
                del self.node_lookup[lru_node.node_key]
                self.remove_node(lru_node)
                self.curr_size -= 1

            new_node = Node(key, val)
            self.node_lookup[key] = new_node
            self.move_to_end(new_node)
            self.curr_size += 1


if __name__ == "__main__":
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);

    # Test1  cache hit
    print(f"cache returns {our_cache.get(1)}")  # returns 1
    # Test2  cache hit
    print(f"cache returns {our_cache.get(2)}")  # returns 2
    # Test3  cache miss
    print(f"cache returns {our_cache.get(9)}")  # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    # Test4  cache miss because 3 has been evicted.
    print(f"cache returns {our_cache.get(3)}") # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

    # Test5 set and get None
    our_cache.set(None, 6)
    print(f"cache returns {our_cache.get(None)}") # expecting None to be handled as key

    # Test5 set and get 0
    our_cache.set(0, 100)
    print(f"cache returns {our_cache.get(0)}")  # expecting 0 to be handled as key


