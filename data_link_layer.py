import pickle
import subprocess
import re

class DataLinkLayer:
    def __init__(self):
        """ Automatically determine the MAC address of the active network adapter """
        self.mac_address = self.get_mac_address()

    def get_mac_address(self):
        """ Get the full local MAC address using Windows' getmac command """
        try:
            # Run 'getmac' command to get MAC addresses
            output = subprocess.check_output("getmac", shell=True, text=True)

            # Extract the full MAC address (format: XX-XX-XX-XX-XX-XX)
            mac_addresses = re.findall(r"([0-9A-Fa-f]{2}(?:[:-][0-9A-Fa-f]{2}){5})", output)

            if mac_addresses:
                return mac_addresses[0]  # 
        except Exception as e:
            print(f"Error getting MAC address: {e}")
        
        return "00:00:00:00:00:00"  # Fallback if no MAC found

    def send(self, data):
        """ Encapsulate data with the MAC address of the active network adapter """
        frame = {"mac": self.mac_address, "payload": data}
        print(f"Data Link Layer (send): Sending data with MAC {self.mac_address}\n")  
        return pickle.dumps(frame)  # Serialize frame

    def receive(self, frame):
        """ Extract payload from the frame """
        frame = pickle.loads(frame)  # Deserialize frame
        print(f"Data Link Layer (receive): Received data from MAC {frame['mac']}\n")  
        return frame["payload"]
