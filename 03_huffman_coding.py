"""
Overview - Data Compression
In general, a data compression algorithm reduces the amount of memory (bits) required to represent a message (data). The compressed data, in turn, helps to reduce the transmission time from a sender to receiver. The sender encodes the data, and the receiver decodes the encoded data. As part of this problem, you have to implement the logic for both encoding and decoding.

A data compression algorithm could be either lossy or lossless, meaning that when compressing the data, there is a loss (lossy) or no loss (lossless) of information. The Huffman Coding is a lossless data compression algorithm. Let us understand the two phases - encoding and decoding with the help of an example.

A. Huffman Encoding

Assume that we have a string message AAAAAAABBBCCCCCCCDDEEEEEE comprising of 25 characters to be encoded. The string message can be an unsorted one as well. We will have two phases in encoding - building the Huffman tree (a binary tree), and generating the encoded data. The following steps illustrate the Huffman encoding:

Phase I - Build the Huffman Tree
A Huffman tree is built in a bottom-up approach.

1. First, determine the frequency of each character in the message. In our example, the following table presents the frequency of each character.

(Unique) Character	Frequency
A	                      7
B	                      3
C	                      7
D	                      2
E	                      6

2. Each row in the table above can be represented as a node having a character, frequency, left child, and right child. In the next step, we will repeatedly require to pop-out the node having the lowest frequency. Therefore, build and sort a list of nodes in the order lowest to highest frequencies. Remember that a list preserves the order of elements in which they are appended.

We would need our list to work as a priority queue, where a node that has lower frequency should have a higher priority to be popped-out. The following snapshot will help you visualize the example considered above:

Visualization of what we would like our priority queue (https://en.wikipedia.org/wiki/Priority_queue) to look like, with the lowest frequency node on the left, 'D'-2, followed by 'B'-3, 'E'-6, 'A'-7, and finally the highest frequency node on the right, 'C'-7.

[https://video.udacity-data.com/topher/2020/May/5eac5f84_screenshot-2020-04-27-at-5.15.56-pm/screenshot-2020-04-27-at-5.15.56-pm.png]

Can you come up with other data structures to create a priority queue? How about using a min-heap instead of a list? You are free to choose from anyone.

3. Pop-out two nodes with the minimum frequency from the priority queue created in the above step.

4. Create a new node with a frequency equal to the sum of the two nodes picked in the above step. This new node would become an internal node in the Huffman tree, and the two nodes would become the children. The lower frequency node becomes a left child, and the higher frequency node becomes the right child. Reinsert the newly created node back into the priority queue.

Do you think that this reinsertion requires the sorting of priority queue again? If yes, then a min-heap could be a better choice due to the lower complexity of sorting the elements, every time there is an insertion.

5. Repeat steps #3 and #4 until there is a single element left in the priority queue. The snapshots below present the building of a Huffman tree.

Visualization of the steps described above to build a Huffman tree from a priority queue:

[https://video.udacity-data.com/topher/2020/May/5eac5fd2_huffman-tree-1/huffman-tree-1.png]

Visualization of repeating steps 3 and 4 above to create a Huffman tree:

[https://video.udacity-data.com/topher/2020/May/5eac5feb_huffman-tree-2/huffman-tree-2.png]

6. For each node, in the Huffman tree, assign a bit 0 for left child and a 1 for right child. See the final Huffman tree for our example:

The resulting Huffman tree from the given priority queue:

[https://video.udacity-data.com/topher/2020/May/5eac6028_huffman-tree-3/huffman-tree-3.png]

Phase II - Generate the Encoded Data

7. Based on the Huffman tree, generate unique binary code for each character of our string message. For this purpose, you'd have to traverse the path from root to the leaf node.

(Unique) Character	Frequency	Huffman Code
D	                      2	        000
B	                      3	        001
E	                      6	        01
A	                      7	        10
C	                      7	        11

Points to Notice

- Notice that the whole code for any character is not a prefix of any other code. Hence, the Huffman code is called a Prefix code (https://en.wikipedia.org/wiki/Prefix_code).
- Notice that the binary code is shorter for the more frequent character, and vice-versa.
- The Huffman code is generated in such a way that the entire string message would now require a much lesser amount of memory in binary form.
- Notice that each node present in the original priority queue has become a leaf node in the final Huffman tree.

This way, our encoded data would be 1010101010101000100100111111111111111000000010101010101

B. Huffman Decoding

Once we have the encoded data, and the (pointer to the root of) Huffman tree, we can easily decode the encoded data using the following steps:

1. Declare a blank decoded string
2. Pick a bit from the encoded data, traversing from left to right.
3. Start traversing the Huffman tree from the root.
    - If the current bit of encoded data is 0, move to the left child, else move to the right child of the tree if the current bit is 1.
    - If a leaf node is encountered, append the (alphabetical) character of the leaf node to the decoded string.
4. Repeat steps #2 and #3 until the encoded data is completely traversed.

You will have to implement the logic for both encoding and decoding in the following template. Also, you will need to create the sizing schemas to present a summary.


Visualization Resource

Check this website to visualize the Huffman encoding for any string message - Huffman Visualization! (https://people.ok.ubc.ca/ylucet/DS/Huffman.html)
"""

import sys


class TreeNode:
    def __init__(self, value, frequency):
        self.value = value
        self.frequency = frequency
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode({self.value}, {self.frequency})"

    def __lt__(self, other):
        return self.frequency < other.frequency


class HuffmanTree:
    def __init__(self, root):
        self.root = root

    def __repr__(self):
        return f"HuffmanTree({self.root})"

    def __lt__(self, other):
        return self.root.frequency < other.root.frequency

    def calc_encoded_data(data, pq):
        # Build Huffman code table containing the unique binary code for each character
        code_table = {}

        # Use recursion to build the code table
        def build_code_table(node, code):
            if node is None:
                return
            if node.value is not None:
                code_table[node.value] = code
                return
            build_code_table(node.left, f"{code}0")
            build_code_table(node.right, f"{code}1")

        build_code_table(pq[0], "")

        # Encode data using the lookup table
        encoded_data = ""
        for char in data:
            encoded_data += code_table[char]

        return encoded_data

    def huffman_encoding(data):
        """
        Encodes a string using Huffman encoding.

        Args:
            data: string to be encoded

        Returns:
            encoded_data: encoded string
            tree: Huffman tree used for encoding
        """
        if data == "" or data is None:
            return "", HuffmanTree(None)

        # Determine the frequency of each character in the string
        freq_table = {}
        for char in data:
            if char in freq_table:
                freq_table[char] += 1
            else:
                freq_table[char] = 1

        # Build a priority queue of TreeNode objects
        pq = []
        for char, freq in freq_table.items():
            pq.append(TreeNode(char, freq))
        pq.sort()

        # Build Huffman tree by popping out two nodes with the minimum frequency
        # continuously until there is only one node left in the priority queue
        while len(pq) > 1:
            left = pq.pop(0)
            right = pq.pop(0)
            # Create a new node with a frequency equal to the sum of the two nodes just popped
            parent = TreeNode(None, left.frequency + right.frequency)
            parent.left = left
            parent.right = right
            pq.append(parent)
            pq.sort()

        # Calculate the encoded data
        encoded_data = HuffmanTree.calc_encoded_data(data, pq)

        # Return the encoded data with the Huffman tree
        return encoded_data, HuffmanTree(pq[0])

    def huffman_decoding(data, tree):
        """
        Decodes a string using Huffman encoding.

        Args:
            data: encoded string to be decoded
            tree: Huffman tree used for encoding

        Returns:
            decoded_data: decoded string
        """
        if data == "":
            return ""

        decoded_data = ""
        # Start with root
        node = tree.root
        # Traverse the tree based on the encoded data
        # Moving left if the current bit is 0, and right if the current bit is 1
        for binary in data:
            if binary == "0":
                node = node.left
            else:
                node = node.right

            # If the node has a value, append it to the decoded data
            if node.value is not None:
                decoded_data += node.value
                # Reset the node to the root
                node = tree.root

        return decoded_data


def included_test():
    print("\Default Test:\n")
    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = HuffmanTree.huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = HuffmanTree.huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
# Test the case where input is None
def test_01():
    print("\nTest 01 - input is None:\n")
    test_sentence = None

    print("The content of the data is: {}\n".format(test_sentence))

    encoded_data, tree = HuffmanTree.huffman_encoding(test_sentence)

    assert encoded_data == "", print("Test 01 Failed: encoded data is not empty")
    assert tree.root is None, print("Test 01 Failed: tree root is not None")

    decoded_data = HuffmanTree.huffman_decoding(encoded_data, tree)

    assert decoded_data == "", print("Test 01 Failed: decoded data is not empty")

    print("Test 01 Passed")


# Test Case 2
# Test the case where input is empty string
def test_02():
    print("\nTest 02 - empty string:\n")
    test_sentence = ""

    print("The content of the data is: {}\n".format(test_sentence))

    encoded_data, tree = HuffmanTree.huffman_encoding(test_sentence)

    assert encoded_data == "", print("Test 02 Failed: encoded data is not empty")
    assert tree.root is None, print("Test 02 Failed: tree root is not None")

    decoded_data = HuffmanTree.huffman_decoding(encoded_data, tree)

    assert decoded_data == "", print("Test 02 Failed: decoded data is not empty")

    print("Test 02 Passed")


# Test Case 3
# Test the case where input is a very large string
def test_03():
    print("\nTest 03 - long input string:\n")
    test_sentence = "In general, a data compression algorithm reduces the amount of memory (bits) required to represent a message (data). The compressed data, in turn, helps to reduce the transmission time from a sender to receiver. The sender encodes the data, and the receiver decodes the encoded data. As part of this problem, you have to implement the logic for both encoding and decoding."

    print("The content of the data is: {}\n".format(test_sentence))

    encoded_data, tree = HuffmanTree.huffman_encoding(test_sentence)

    assert (
        encoded_data
        == "0001101000101111010101000010100011001011010110001111110101111010001011100010111110100011110111110110011010000110011000001110010111010110101110101001110110000011001101010111111011010001001011001010010000111111100110101001110101101110111101100001011001110111110111111110111100101110111011011011101111000101010110100000110000110001011111011010000011011101100000001101000100111110001111110110100110110011010000111000010110011101011111011110000110011010110101010011100010100100010111000101000101100010011100011001101010011110100011110111110110011010000110011100010011101000101110001010001111110000001011111001011000110001000011111111010100101011110110001111111000111111011010001001011001010010011111001101010011111000110010100100011101110000001100110000011100101111100000010111100111110111101100111101111110101111001110000100100100011011111000111111011010010100100000010110111000110000100111000110011010100111001110000100100100011011110000101010001110100100001111111001101010011101000101110001010001111110101001001001111100110101001110110100101001000000101101110001101110100100101000111010010000111111100110101001111000010101000111010010001001110100010111000101000100111110111000011111110110010101101100111011111011111111100110100000001111111011001100111101101010101110010111000111111110111010111101100111110100101101101110011111000111111000010111110110101011100101111000010110011111001101010011110101101111010100000101001111101111011101101111011010011111001101011110000101010001110100000000101010101110101001001001110100100101000111010000000010101010000100"
    ), print("Test 03 Failed: encoded data is not as expected")

    decoded_data = HuffmanTree.huffman_decoding(encoded_data, tree)

    assert decoded_data == test_sentence, print("Test 03 Failed: decoded data is not empty")

    print("Test 03 Passed")


if __name__ == "__main__":
    included_test()
    test_01()
    test_02()
    test_03()
