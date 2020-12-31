import hashlib
import datetime


def calc_hash(hash_str):
    """Return hashed strin
    Args:
        hash_str: string
    Returns:
        hashed string
    """
    sha = hashlib.sha256()
    hash_str = hash_str.encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()


class Block(object):
    def __init__(self, data):
        self.timestamp = datetime.datetime.now(datetime.timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%S.%f%Z")
        self.data = data
        self.prev = None
        self.previous_hash = None
        self.hash = calc_hash(data)


class BlockChain(object):
    def __init__(self):
        self.tail = None

    def size(self):
        size = 0
        block = self.tail
        while block:
            size += 1
            block = block.prev
        return size

    def __str__(self):
        cur_tail = self.tail
        out_string = ""
        while cur_tail:
            out_string += str(cur_tail.data) + " -> "
            cur_tail = cur_tail.prev
        return out_string

    def append(self, data):
        if self.tail is None:
            self.tail = Block(data)
            return

        block = Block(data)
        block.prev = self.tail
        block.previous_hash = self.tail.hash
        self.tail = block

    def search(self, data):
        """ Search the linked list for a node with the requested value and return the node. """
        current_block = self.tail
        while current_block:
            if current_block.data == data:
                return current_block
            else:
                current_block = current_block.prev
        return None

    def remove(self, data):
        """ Remove first occurrence of value. """
        current_block = self.tail
        if current_block.data == data:
            self.tail = current_block.prev
        else:
            while current_block:
                if current_block is None:
                    return
                elif current_block.prev.data == data:
                    current_block.prev = current_block.prev.prev
                    return
                else:
                    current_block = current_block.prev


if __name__ == "__main__":
    # Test1 node creation
    test_data = 'BTC 0.5'
    b = Block(test_data)
    print(b.data, b.prev, b.hash, b.previous_hash)

    # Test2 BlockChain creation
    BlockChain = BlockChain()
    BlockChain.append('BTC 0.1')
    BlockChain.append('BTC 0.3')
    print(BlockChain.size())
    print(str(BlockChain))

    # Test3 BlockChain Search
    print(BlockChain.search('BTC 0.2'))# should return None
    found = BlockChain.search('BTC 0.3')# should return node
    print(found.data)

    # Test4 BlockChain remove
    BlockChain.remove('BTC 0.3')
    print(BlockChain.size())
