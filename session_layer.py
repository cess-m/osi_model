import pickle

def send(data, session_id=1234):
    session = {"session": session_id, "payload": data}
    return pickle.dumps(session)  # Use pickle to serialize bytes

def receive(session):
    session = pickle.loads(session)  # Deserialize correctly
    return session["payload"]
