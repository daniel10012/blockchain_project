from django.db import models
import hashlib
from datetime import datetime

class Data(models.Model):
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content

    def hash(self):
        my_str = self.content
        my_str_as_bytes = str.encode(my_str)
        hash_object = hashlib.sha256(my_str_as_bytes)
        hex_dig = hash_object.hexdigest()
        return (hex_dig)

class Blockchain(models.Model):
    chain_num = models.CharField(max_length=100, default="0", primary_key=True)
    #current_transactions = []
    # chain = []
    # # Create the genesis block
    # genesis_block = Block(
    #                       block_num='0',
    #                       nonce="0",
    #                       data='Genesis Block',
    #                       timestamp="2019-05-24 00:00:00",
    #                       hash='0'*64,
    #                       previous_hash='0'*64
    # )
    #
    #
    # def new_block(self):
    #     """
    #     Create a new Block in the Blockchain
    #     :param proof: <int> The proof given by the Proof of Work algorithm
    #     :param previous_hash: (Optional) <str> Hash of previous Block
    #     :return: <dict> New Block
    #     """
    #
    #     block = {
    #         'block_num': len(self.chain) + 1,
    #         'nonce':"0",
    #         'data':' ',
    #         'timestamp': str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    #     }
    #
    #     # Reset the current list of transactions
    #     #self.current_transactions = []
    #
    #     self.chain.append(block)
    #     return block

class Block(models.Model):
    block_num = models.CharField(max_length=100, primary_key=True)
    nonce = models.CharField(max_length=100,default='0')
    data = models.CharField(max_length=100)
    timestamp = models.CharField(max_length=100,default='0')
    hash = models.CharField(max_length=100,default='0'*64)
    previous_hash = models.CharField(max_length=100, default='0' * 64)
    blockchain = models.ForeignKey('Blockchain', on_delete=models.CASCADE, )



    def __str__(self):
        return self.block_num

    def hashing(self):
        my_str = self.block_num + self.nonce + self.data + self.timestamp
        my_str_as_bytes = str.encode(my_str)
        hash_object = hashlib.sha256(my_str_as_bytes)
        hex_dig = hash_object.hexdigest()
        return (hex_dig)

    def mine(self, difficulty=4):
        nonce = "0"
        h = self.hashing()
        while h[:difficulty] != difficulty * "0":
            n = int(nonce)
            n += 1
            nonce = str(n)
            self.nonce = nonce
            h = self.hashing()
        return {"nonce": nonce, "hash": h}



