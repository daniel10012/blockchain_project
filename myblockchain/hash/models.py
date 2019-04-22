from django.db import models
import hashlib

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




# my_str = "hello world"
# my_str_as_bytes = str.encode(my_str)
# type(my_str_as_bytes) # ensure it is byte representation
# my_decoded_str = my_str_as_bytes.decode()
# type(my_decoded_str) # ensure it is string representation