import hashlib
import datetime


def calc_hash(self, hash_str):
    sha = hashlib.sha256()
    hash_str = hash_str.encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()

class Block:
    def __init__(self, data):
        self.timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")
        self.data = data
        self.previous_hash = None
        self.hash = calc_hash(self, data)




class BlockChain:
    def __init__(self):
        self.tail = None

    def size(self):
        size = 0
        block = self.tail
        while block:
            size += 1
            block = block.previous_hash
        return size

    def __str__(self):
        cur_tail = self.tail
        out_string = ""
        while cur_tail:
            out_string += str(cur_tail.data) + " -> "
            cur_tail = cur_tail.previous_hash
        return out_string

    def append(self, data):
        if self.tail is None:
            self.tail = Block(data)
            return

        block = Block(data)
        block.previous_hash = self.tail
        self.tail = block

    def search(self, data):
        """ Search the linked list for a node with the requested value and return the node. """
        current_block = self.tail
        while current_block:
            if current_block.data == data:
                return current_block
            else:
                current_block = current_block.previous_hash
        return None

    def remove(self, data):
        """ Remove first occurrence of value. """
        current_block = self.tail
        if current_block.data == data:
            self.tail = current_block.previous_hash
        else:
            while current_block:
                if current_block is None:
                    return
                elif current_block.previous_hash.data == data:
                    current_block.previous_hash = current_block.previous_hash.previous_hash
                    return
                else:
                    current_block = current_block.previous_hash



data = 'Some Info'
b = Block(data)
print(b.data, b.previous_hash, b.hash)


BlockChain = BlockChain()
BlockChain.append('BTC 0.1')
BlockChain.append('BTC 0.3')
print(BlockChain.size())
print(str(BlockChain))
print(BlockChain.search('BTC 0.2'))
found = BlockChain.search('BTC 0.3')
print(found.data)
BlockChain.remove('BTC 0.3')
print(BlockChain.size())

