"""
Blockchain
A Blockchain (https://en.wikipedia.org/wiki/Blockchain) is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 (https://en.wikipedia.org/wiki/SHA-2) hash, the Greenwich Mean Time (https://en.wikipedia.org/wiki/Greenwich_Mean_Time) when the block was created, and text strings as the data.

Use your knowledge of linked lists and hashing to create a blockchain implementation.

Block chain with 3 blocks, 'Block 0', 'Block 1' which refers to 'Block 0', and 'Block 2' which refers to 'Block 1'
We can break the blockchain down into three main parts.

First is the information hash:

"""

import hashlib


def calc_hash(self):
    sha = hashlib.sha256()

    hash_str = "We are going to encode this string of data!".encode("utf-8")

    sha.update(hash_str)

    return sha.hexdigest()


"""
We do this for the information we want to store in the blockchain such as transaction time, data, and information like the previous chain.

The next main component is the block on the blockchain:
"""


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1

# Test Case 2

# Test Case 3


"""
Above is an example of attributes you could find in a Block class.

Finally you need to link all of this together in a block chain, which you will be doing by implementing it in a linked list. All of this will help you build up to a simple but full blockchain implementation!
"""
