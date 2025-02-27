import pickle

def send(data, ip_address="192.168.1.1"):
    packet = {"ip": ip_address, "payload": data}
    return pickle.dumps(packet)  # Use Pickle

def receive(packet):
    packet = pickle.loads(packet)  # Deserialize packet
    return packet["payload"]
