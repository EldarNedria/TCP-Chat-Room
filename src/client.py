import socket
import threading

class Client:
    def __init__(self):
        self.nickname = input("Enter your nickname: ")
        self.password = None
        if self.nickname == "admin":
            self.password = input("Enter password for admin account: ")
        
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('127.0.0.1', 55555))
        self.stop_thread = False

    def receive(self):
        while True:
            if self.stop_thread:
                break
            try:
                message = self.client.recv(1024).decode('ascii')
                if message == 'NICK':
                    self.client.send(self.nickname.encode('ascii'))
                    next_message = self.client.recv(1024).decode('ascii')
                    if next_message == 'PASS':
                        self.client.send(self.password.encode('ascii'))
                        if self.client.recv(1024).decode('ascii') == 'REFUSE':
                            print("Connection was refused! Wrong password!")
                            self.stop_thread = True
                    elif next_message == 'BAN':
                        print('Connection refused because of ban!')
                        self.client.close()
                        self.stop_thread = True
                else:
                    print(message)
            except:
                print("An error occured!")
                self.client.close()
                break

    def write(self):
        while True:
            if self.stop_thread:
                break
            message = f'{self.nickname}: {input("")}'
            if message[len(self.nickname)+2:].startswith('/'):
                if self.nickname == 'admin':
                    if message[len(self.nickname)+2:].startswith('/kick'):
                        self.client.send(f'KICK {message[len(self.nickname)+2+6:]}'.encode('ascii'))
                    elif message[len(self.nickname)+2:].startswith('/ban'):
                        self.client.send(f'BAN {message[len(self.nickname)+2+5:]}'.encode('ascii'))
                else:
                    print("Command can only be executed by admin!")
            else:
                self.client.send(message.encode('ascii'))

    def start(self):
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        write_thread = threading.Thread(target=self.write)
        write_thread.start()

if __name__ == "__main__":
    client = Client()
    client.start()