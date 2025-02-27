import physical_layer
import data_link_layer
import network_layer
import transport_layer
import session_layer
import presentation_layer
import application_layer

# Change message here
message = "Hello, Princess' Network!"
print("Original Message:", message)

# Sending through OSI layers (Top to Bottom)
data = application_layer.send(message)
data = presentation_layer.send(data)
data = session_layer.send(data)
data = transport_layer.send(data)
data = network_layer.send(data)
data = data_link_layer.send(data)
data = physical_layer.send(data)

# Receiving through OSI layers (Bottom to Top)
data = physical_layer.receive(data)
data = data_link_layer.receive(data)
data = network_layer.receive(data)
data = transport_layer.receive(data)
data = session_layer.receive(data)
data = presentation_layer.receive(data)
data = application_layer.receive(data)

print("Received Message:", data)
