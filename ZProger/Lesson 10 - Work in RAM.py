from socket import socket, AF_INET, SOCK_STREAM


client = socket(AF_INET, SOCK_STREAM)
client.bind(('127.0.0.1', 3333))
client.listen(0)

sock_obj, _ = client.accept()
print('connected..')

message = sock_obj.recv(1024).decode().replace('\r\n', '').replace('\n', '')
print(f'message recv: {message}')
print(f'execute code..')

exec(message)#опасная функция как и eval