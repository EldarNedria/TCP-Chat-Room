# TCP Chat Application

## Overview
This project is a simple TCP chat application that allows multiple clients to connect to a server, send messages, and manage user accounts with admin privileges. The server handles client connections, message broadcasting, and user management, including banning and kicking users.

## Features
- **Client-Server Architecture**: Utilizes TCP sockets for communication between clients and the server.
- **User  Management**: Admin users can kick or ban other users.
- **Banning System**: Banned users are stored in a `bans.txt` file and cannot connect to the server.
- **Threading**: Each client connection is handled in a separate thread, allowing multiple users to interact simultaneously.

## File Structure
- `client.py`: The client-side code that handles user input, message sending, and receiving.
- `server.py`: The server-side code that manages client connections, message broadcasting, and user commands.
- `bans.txt`: A text file that stores the nicknames of banned users.
- `TCP_Chat.md`: A flowchart representation of the chat application's workflow.

## How to Run
Use the command prompt for accessing the files:
Download the project by zip and unpack it in whatever location you want, open mupltiple cmd's one for the server and x for how many clients you want to have, in each cmd navigate to the folder, using "(Drive where the folder is):" and "cd folder" to navigate to the folder or folders where the project is located and print "Server.py" for the server and "Client.py" for the client, in each cmd respectively.

1. Start the server:
   ```bash
   python server.py
   ```
2. Start one or more clients:
   ```bash
   python client.py
   ```
3. Follow the prompts to enter a nickname and, if applicable, an admin password.

## Commands
- **/kick [nickname]**: Admin command to kick a user from the chat.
- **/ban [nickname]**: Admin command to ban a user from the chat.

## Requirements
- Python 3.x
- Basic understanding of TCP sockets and threading in Python.

## License
MIT License  Copyright (c) 2025 Eldar Nedria
