import json

def send(message):
    request = {"method": "GET", "data": message} 
    return json.dumps(request)

def receive(request):
    request = json.loads(request)
    return f"Response: Received {request['data']}"
