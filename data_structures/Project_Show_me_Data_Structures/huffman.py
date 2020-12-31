import sys

class PriorityQueue(object):
    def __init__(self):
        self.q = []

    def __repr__(self):
        sorted_list = sorted(self.q, key=lambda x: x.get_value(), reverse=True)
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in sorted_list])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"

        # for checking if the queue is empty

    def isEmpty(self):
        return len(self.q) == 0

    def size(self):
        return len(self.q)

    # for inserting an element in the queue
    def push(self, data):
        self.q.append(data)

        # for popping an element based on Priority

    def pop(self):
        if len(self.q)> 0:
            max = 0
            for i in range(len(self.q)):
                # overriding priority implementation for nodes
                if self.q[i].get_value() < self.q[max].get_value():
                    max = i
            item = self.q[max]
            del self.q[max]
            return item
        else:
            return -1

class Node(object):
    def __init__(self, value=None, letter= None):
        self.value = value
        self.letter = letter
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_letter(self, letter):
        self.letter = letter

    def get_letter(self):
        return self.letter

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    def is_leaf(self):
        if not self.has_left_child() and not self.has_right_child():
            return True
        return False

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node Value: {self.get_value()} Letter: {self.get_letter()}"

    def __str__(self):
        return f"Node Value: {self.get_value()} Letter: {self.get_letter()}"


def frequency_sentence(str):
    frequency = {}
    for s in str:
        frequency[s] = frequency.get(s, 0) + 1
    return frequency

def path_from_root_to_node(root, letter):
    """
    Assuming data as input to find the node
    The solution can be easily changed to find a node instead of data
    :param data:
    :return:
    """
    output = path_from_node_to_root(root, letter)
    return list(reversed(output))

# recursive solution
def path_from_node_to_root(root, letter):
    if root is None:
        return None

    elif root.get_letter() == letter:
        return []

    left_answer = path_from_node_to_root(root.left, letter)
    if left_answer is not None:
        left_answer.append(0)
        return left_answer

    right_answer = path_from_node_to_root(root.right, letter)
    if right_answer is not None:
        right_answer.append(1)
        return right_answer
    return None

def huffman_encoding(sentence):
    lett_freq = frequency_sentence(sentence)
    q_of_nodes = PriorityQueue()
    for letter, freq in lett_freq.items():
        node = Node(freq, letter)
        q_of_nodes.push(node)

    while q_of_nodes.size() > 1:
        a = q_of_nodes.pop()
        b = q_of_nodes.pop()
        c = a.get_value() + b.get_value()
        node = Node(c, None)
        node.set_left_child(a)
        node.set_right_child(b)
        q_of_nodes.push(node)

    root = q_of_nodes.pop()

    encoded_str = []
    for s in a_great_sentence:
        encoded_str.extend(path_from_root_to_node(root, s))

    encoded_str = ''.join([str(e) for e in encoded_str])
    return encoded_str, root


def huffman_decoding(encoded_str, root):
    decoded = []
    node = root

    for e in encoded_str:
        if e == '1':
            node = node.get_right_child()
        elif e == '0':
            node = node.get_left_child()
        if node.is_leaf():
            decoded.append(node.get_letter())
            node = root

    decoded = ''.join([e for e in decoded])
    return decoded


if __name__ == "__main__":
    # 1 Test Case string.
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))

    # 2 Test Case upper case repeating letters.
    a_great_sentence = "AAAAAAABBBCCCCCCCDDEEEEEE"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))

    # 3 Test Case number.
    a_great_sentence = "133 is  greater than 132"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(encoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))

    # 4 Test Case empty string.
    a_great_sentence = ""

    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The content of the decoded data is: {}\n".format(decoded_data))

