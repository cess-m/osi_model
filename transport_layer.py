import pickle

def send(data, seq_num=1):
    segment = {"seq": seq_num, "payload": data}
    return pickle.dumps(segment)  # Use Pickle

def receive(segment):
    segment = pickle.loads(segment)  # Deserialize correctly
    return segment["payload"]
