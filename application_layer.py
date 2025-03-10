import json

class ApplicationLayer:
    def send(self, message):
        """ Simulate sending an HTTP-like request """
        request = {"method": "GET", "data": message} 
        print(f"Application Layer (send): Sending request with data: {message}\n")
        return json.dumps(request)

    def receive(self, request):
        """ Simulate receiving an HTTP-like response """
        request = json.loads(request)
        response = f"Response: Received {request['data']}"
        print(f"Application Layer (receive): {response}\n")
        return response
