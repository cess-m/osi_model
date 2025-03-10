import pickle

class PhysicalLayer:
    def send(self, data):
        """ Convert data into a binary format for transmission """
        return pickle.dumps(data)  
    
    def receive(self, binary_data):
        """ Convert binary format back to original data """
        return pickle.loads(binary_data)  
