```mermaid
graph TD;
    A[Client] -->|Connects| B[Server]
    B -->|Sends NICK| C[Client Receives NICK]
    C -->|Sends Nickname| B
    B -->|Checks Bans| D[Read bans.txt]
    D -->|Nickname Found?| E{Yes}
    E -->|Sends BAN| F[Client Receives BAN]
    F -->|Closes Connection| B
    E -->|No| G{Is Admin?}
    G -->|Yes| H[Sends PASS]
    H -->|Receives Password| B
    B -->|Checks Password| I{Correct?}
    I -->|No| J[Sends REFUSE]
    J -->|Closes Connection| B
    I -->|Yes| K[Add Client to List]
    K -->|Broadcast Join Message| L[All Clients Receive Join Message]
    K -->|Sends Connected Message| C
    A -->|Sends Message| B
    B -->|Broadcasts Message| L
    A -->|Sends Command| B
    B -->|Handles Command| M{Command Type}
    M -->|KICK| N[Checks Admin]
    N -->|Yes| O[Kicks User]
    M -->|BAN| P[Checks Admin]
    P -->|Yes| Q[Bans User]
    Q -->|Writes to bans.txt| R[Update bans.txt]
    M -->|Default| S[Broadcasts Message]
    B -->|Handles Disconnection| T[Removes Client]
    T -->|Broadcasts Leave Message| L