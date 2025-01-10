```mermaid
graph TD
    A[User 1] -->|Input Message| B[Encrypt Message]
    B --> C{Select Communication Mode}
    C -->|Online| D[Send to Online Server]
    C -->|Bluetooth| E[Send via Bluetooth]
    D -->|Encrypted Message| F[Online Server]
    F -->|Store & Retrieve Encrypted Messages| G[User 2]
    E -->|Encrypted Message| H[Bluetooth Server]
    H -->|Forward Message| I[User 2]
    G -->|Receive & Decrypt Message| J[User 2 Decrypts]
    I -->|Receive & Decrypt Message| J
    J -->|View Plain Text Message| K[User 2]
