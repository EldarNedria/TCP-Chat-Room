import threading
import socket

class Server:
    def __init__(self, host='127.0.0.1', port=55555):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()
        self.clients = []
        self.nicknames = []

    def broadcast(self, message):
        for client in self.clients:
            client.send(message)

    def handle(self, client):
        while True:
            try:
                msg = client.recv(1024)
                if msg.decode('ascii').startswith('KICK'):
                    if self.nicknames[self.clients.index(client)] == 'admin':
                        name_to_kick = msg.decode('ascii')[5:]
                        self.kick_user(name_to_kick)
                    else:
                        client.send('Command was refused!'.encode('ascii'))
                elif msg.decode('ascii').startswith('BAN'):
                    if self.nicknames[self.clients.index(client)] == 'admin':
                        name_to_ban = msg.decode('ascii')[4:]
                        self.kick_user(name_to_ban)
                        with open('bans.txt', 'a') as f:
                            f.write(f'{name_to_ban}\n')
                        print(f'{name_to_ban} was banned!')
                    else:
                        client.send('Command was refused!'.encode('ascii'))
                else:
                    self.broadcast(msg)
            except:
                if client in self.clients:
                    index = self.clients.index(client)
                    self.clients.remove(client)
                    client.close()
                    nickname = self.nicknames[index]
                    self.broadcast(f'{nickname} left the chat!'.encode('ascii'))
                    self.nicknames.remove(nickname)
                    break

    def receive(self):
        while True:
            client, address = self.server.accept()
            print(f'Connected with {str(address)}')

            client.send('NICK'.encode('ascii'))
            nickname = client.recv(1024).decode('ascii')

            with open('bans.txt', 'r') as f:
                bans = f.readlines()

            if nickname + '\n' in bans:
                client.send('BAN'.encode('ascii'))
                client.close()
                continue

            if nickname == 'admin':
                client.send('PASS'.encode('ascii'))
                password = client.recv(1024).decode('ascii')

                if password != 'admin':
                    client.send('REFUSE'.encode('ascii'))
                    client.close()
                    continue

            self.nicknames.append(nickname)
            self.clients.append(client)

            print(f'Nickname of the client is {nickname}')
            self.broadcast(f'{nickname} has joined the chat!'.encode('ascii'))
            client.send('Connected to the server'.encode('ascii'))

            thread = threading.Thread(target=self.handle, args=(client,))
            thread.start()

    def kick_user(self, name):
        if name in self.nicknames:
            name_index = self.nicknames.index(name)
            client_to_kick = self.clients[name_index]
            self.clients.remove(client_to_kick)
            client_to_kick.send('You were kicked by an admin!'.encode('ascii'))
            client_to_kick.close()
            self.nicknames.remove(name)
            self.broadcast(f'{name} was kicked by an admin!'.encode('ascii'))

if __name__ == "__main__":
    server = Server()
    print('Server is listening!!!')
    server.receive()