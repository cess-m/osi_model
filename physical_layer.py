import pickle

def send(data):
    """ Convert data into a binary format for transmission """
    return pickle.dumps(data)  # Encodes data into binary

def receive(binary_data):
    """ Convert binary format back to original data """
    return pickle.loads(binary_data)  # Decodes binary data
