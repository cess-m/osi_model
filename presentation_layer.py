import zlib

def send(data):
    compressed_data = zlib.compress(data.encode())
    return compressed_data

def receive(compressed_data):
    decompressed_data = zlib.decompress(compressed_data).decode()
    return decompressed_data
