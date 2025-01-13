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
This project is open-source and available for modification and distribution.
