import pickle

class TransportLayer:
    def send(self, data, seq_num=1):
        """ Simulate transport layer packet sequencing """
        segment = {"seq": seq_num, "payload": data}
        print(f"Transport Layer (send): Sending segment #{seq_num}\n")
        return pickle.dumps(segment)  
    
    def receive(self, segment):
        """ Simulate transport layer packet reception """
        segment = pickle.loads(segment)  
        print(f"Transport Layer (receive): Received segment #{segment['seq']}\n")
        return segment["payload"]
