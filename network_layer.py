import pickle
import socket

class NetworkLayer:
    def __init__(self):
        """ Automatically determine the local machine's IP address """
        self.ip_address = self.get_local_ip()

    def get_local_ip(self):
        """ Get the local IP address of the machine """
        return socket.gethostbyname(socket.gethostname())

    def send(self, data):
        """ Simulate IP packet transmission """
        packet = {"ip": self.ip_address, "payload": data}
        print(f"Network Layer (send): Sending data from IP {self.ip_address}\n")  
        return pickle.dumps(packet)  # Serialize data

    def receive(self, packet):
        """ Simulate IP packet reception """
        packet = pickle.loads(packet)  # Deserialize packet
        print(f"Network Layer (receive): Received data at IP {packet['ip']}\n")  
        return packet["payload"]
