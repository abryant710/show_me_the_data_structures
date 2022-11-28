"""
Blockchain
A Blockchain (https://en.wikipedia.org/wiki/Blockchain) is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 (https://en.wikipedia.org/wiki/SHA-2) hash, the Greenwich Mean Time (https://en.wikipedia.org/wiki/Greenwich_Mean_Time) when the block was created, and text strings as the data.

Use your knowledge of linked lists and hashing to create a blockchain implementation.

Block chain with 3 blocks, 'Block 0', 'Block 1' which refers to 'Block 0', and 'Block 2' which refers to 'Block 1'

[https://video.udacity-data.com/topher/2019/April/5ca8bd1d_untitled-diagram/untitled-diagram.png]

We can break the blockchain down into three main parts.

First is the information hash:

import hashlib

def calc_hash(self):
    sha = hashlib.sha256()

    hash_str = "We are going to encode this string of data!".encode("utf-8")

    sha.update(hash_str)

    return sha.hexdigest()

We do this for the information we want to store in the blockchain such as transaction time, data, and information like the previous chain.

The next main component is the block on the blockchain:

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

Above is an example of attributes you could find in a Block class.

Finally you need to link all of this together in a block chain, which you will be doing by implementing it in a linked list. All of this will help you build up to a simple but full blockchain implementation!
"""

import hashlib


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = "We are going to encode this string of data!".encode("utf-8")
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self):
        return f"Block: {self.timestamp}, {self.data}, {self.hash}"


class BlockChain:
    def __init__(self):
        self.head = None
        self.tail = None
        self.entries = {}
        self.length = 0

    def append(self, timestamp, data):
        if self.head is None:
            self.head = Block(timestamp, data, None)
            self.tail = self.head
        else:
            previous_hash = self.tail.hash
            self.tail = Block(timestamp, data, previous_hash)
        self.entries[self.length] = self.tail
        self.length += 1

    def __repr__(self):
        return f"BlockChain: {self.entries}"


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
# Test adding 3 blocks to the blockchain
def test_01():
    blockchain = BlockChain()
    blockchain.append("2019-01-01", "Block 0")
    blockchain.append("2019-01-02", "Block 1")
    blockchain.append("2019-01-03", "Block 2")

    assert blockchain.length == 3, "Test 01 Failed: Blockchain length should be 3"
    assert blockchain.head.data == "Block 0", "Test 01 Failed: Blockchain head should be 'Block 0'"
    assert blockchain.tail.data == "Block 2", "Test 01 Failed: Blockchain tail should be 'Block 2'"
    assert blockchain.entries[0].data == "Block 0", "Test 01 Failed: Blockchain entry 0 should be 'Block 0'"
    assert blockchain.entries[1].data == "Block 1", "Test 01 Failed: Blockchain entry 1 should be 'Block 1'"
    assert blockchain.entries[2].data == "Block 2", "Test 01 Failed: Blockchain entry 2 should be 'Block 2'"

    print("Test 1 passed")


# Test Case 2
# Test data on an empty blockchain
def test_02():
    blockchain = BlockChain()

    assert blockchain.length == 0, "Test 02 Failed: Blockchain length should be 0"
    assert blockchain.head is None, "Test 02 Failed: Blockchain head should be None"
    assert blockchain.tail is None, "Test 02 Failed: Blockchain tail should be None"
    assert blockchain.entries == {}, "Test 02 Failed: Blockchain entries should be an empty dictionary"

    print("Test 2 passed")


# Test Case 3
# Test looking up a block in the blockchain based on hash
def test_03():
    blockchain = BlockChain()
    blockchain.append("2019-01-01", "Block 0")
    blockchain.append("2019-01-02", "Block 1")
    blockchain.append("2019-01-03", "Block 2")

    assert blockchain.length == 3, "Test 03 Failed: Blockchain length should be 2"
    tail_hash = blockchain.tail.hash
    tail_previous_hash = blockchain.tail.previous_hash
    assert (
        blockchain.entries[2].hash == tail_hash
    ), "Test 03 Failed: Blockchain entry 2 hash should be the same as the tail hash"
    assert (
        blockchain.entries[2].previous_hash == tail_previous_hash
    ), "Test 03 Failed: Blockchain entry 2 previous hash should be the same as the tail previous hash"
    assert (
        blockchain.entries[1].hash == tail_previous_hash
    ), "Test 03 Failed: Blockchain entry 1 hash should be the same as the tail previous hash"

    print("Test 3 passed")


if __name__ == "__main__":
    test_01()
    test_02()
    test_03()
