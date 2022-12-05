import re
from enum import Enum
from socket import socket, AF_INET, SOCK_STREAM


class ClientResponse(Enum):
    ok = 1
    error = 2


server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 4444))
server.listen(0)

client, _ = server.accept()
response = client.recv(1024)

status = re.search(r'status:.', response).group(0)[-1]
if status == ClientResponse.ok.value:
    print('Status:', ClientResponse.ok.name)
    message = response.split('\\n')[0].split(':')[-1]
    print('Message:', message)
else:
    print('Status:', ClientResponse.error.name)
print(status)
