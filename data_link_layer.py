import pickle

def send(data, mac_address="AA:BB:CC:DD:EE:FF"):
    """ Encapsulate data with a MAC address """
    frame = {"mac": mac_address, "payload": data}
    return pickle.dumps(frame)  # Use Pickle

def receive(frame):
    """ Extract payload from the frame """
    frame = pickle.loads(frame)  # Deserialize frame
    return frame["payload"]
