import zlib

class PresentationLayer:
    def send(self, data):
        """ Simulate data compression """
        compressed_data = zlib.compress(data.encode())  
        print(f"Presentation Layer (send): Compressed data\n")
        return compressed_data 

    def receive(self, compressed_data):
        """ Simulate data decompression """
        decompressed_data = zlib.decompress(compressed_data).decode()
        print(f"Presentation Layer (receive): Decompressed data\n")
        return decompressed_data
