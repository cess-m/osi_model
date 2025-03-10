import pickle

class SessionLayer:
    def __init__(self, session_id=1234):
        """ Initialize with a session ID """
        self.session_id = session_id

    def send(self, data):
        """ Simulate session management by adding session metadata """
        session = {"session": self.session_id, "payload": data}
        print(f"Session Layer (send): Sending data with session ID {self.session_id}\n")
        return pickle.dumps(session)

    def receive(self, session):
        """ Extract payload from the session """
        session = pickle.loads(session)
        print(f"Session Layer (receive): Received data with session ID {session['session']}\n")
        return session["payload"]
