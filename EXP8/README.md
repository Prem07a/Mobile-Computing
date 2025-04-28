# TCP File Transfer - Python Socket Programming

This project demonstrates how to transfer files between a client and server using **TCP sockets** in Python. It provides a basic but reliable system for sending and receiving files over a network.

---

## Overview

- **Protocol**: TCP (Transmission Control Protocol)
- **Communication Model**: OSI 7-Layer Model (focus on Transport and below)
- **Features**:
  - Client connects to server and sends a file.
  - Server listens for incoming connections and saves the received file.

## Files

- `client.py` — Python script to send a file.
- `server.py` — Python script to receive and save the file.
- `main.txt` — Example file to send.
- `received_file.txt` — The file created after successful transfer.

---

## How It Works

### Server Side

1. Creates a TCP socket and binds to an IP address and port.
2. Listens for incoming connections (`listen()`).
3. Accepts a connection (`accept()`).
4. Receives data chunks and writes them into a file.
5. Closes the connection.

### Client Side

1. Creates a TCP socket.
2. Connects to the server’s IP address and port.
3. Reads the file (`main.txt`) in chunks.
4. Sends the file data over the established TCP connection.
5. Closes the connection after transmission.

---

## Running the Project

### Start the Server

```bash
python server.py
```

### Start the Client

```bash
python client.py
```

> Ensure the server is running **before** the client attempts to connect.

---

## Understanding TCP and OSI Model

### What is TCP?

- **TCP (Transmission Control Protocol)** is a **connection-oriented**, **reliable** protocol.
- Key features of TCP:
  - **Reliable transmission** (ensures data arrives correctly).
  - **Ordered delivery** (data arrives in the same order it was sent).
  - **Error detection and recovery**.
  - **Flow control and congestion control**.
- TCP guarantees that packets will be delivered — or if something goes wrong, it will retransmit lost packets.

In our project, TCP ensures that all file chunks arrive at the server in the correct order without corruption.

---

### OSI Model and This Project

The **OSI (Open Systems Interconnection) model** has 7 layers. TCP and sockets mainly involve:

| OSI Layer | In this Project |
|:----------|:----------------|
| **Application Layer** (Layer 7) | Your Python scripts (`client.py` and `server.py`) |
| **Transport Layer** (Layer 4) | TCP protocol manages connection, reliability, and delivery |
| **Network Layer** (Layer 3) | IP protocol routes the data between machines |
| **Data Link Layer** (Layer 2) | Ethernet/Wi-Fi delivers data between directly connected nodes |
| **Physical Layer** (Layer 1) | Actual hardware — cables, Wi-Fi signals, etc. |

Thus:
- **Your Python code** operates at the **Application Layer**.
- **TCP** operates at the **Transport Layer**, managing reliable connections.
- **IP** routes packets over the network at the **Network Layer**.

---

## Example Directory Structure

```
/file_transfer_project/
    client.py
    server.py
    main.txt         # (File to send)
    received_file.txt # (File received, auto-created)
```

---

## Potential Improvements

- Dynamic filename transfer (client sends filename first).
- Progress bar for large files.
- File integrity checking (using checksum/hash).
- Exception handling for network interruptions.

## Layer-by-Layer Explanation (OSI Model applied to Code)

| OSI Layer | How It Appears in This Project |
|:----------|:-------------------------------|
| **Layer 7: Application Layer** | Your Python `server.py` and `client.py` scripts define the logic for opening files, sending/receiving data, and saving files. This is the topmost layer where human interaction happens. |
| **Layer 6: Presentation Layer** | Although simple, when your code reads (`open(file, 'rb')`) and writes (`write(data)`) files, it handles data formats (binary mode), ensuring data is properly interpreted. No encryption or compression is used here, but it could be. |
| **Layer 5: Session Layer** | The TCP connection (`socket.connect()`, `accept()`) establishes, maintains, and terminates a communication session between client and server. |
| **Layer 4: Transport Layer** | TCP itself (underneath `socket.SOCK_STREAM`) ensures reliable delivery, error detection, retransmissions, flow control. It guarantees all file chunks arrive correctly. |
| **Layer 3: Network Layer** | IP (Internet Protocol) is used automatically by your socket library to route packets from client to server (e.g., 127.0.0.1 for localhost). |
| **Layer 2: Data Link Layer** | Ethernet frames or Wi-Fi frames carry the IP packets across the physical network (managed by your operating system and network card, not by Python directly). |
| **Layer 1: Physical Layer** | The actual transmission happens through physical media — like copper cables, fiber optics, or wireless radio waves (Wi-Fi). |

---

### Quick Code Snippets Mapped to OSI Layers:

**Layer 7 (Application):**
```python
# Client opens a file and sends it
with open(file_path, 'rb') as file:
    while (chunk := file.read(buffer_size)):
        client_socket.sendall(chunk)
```
This is your **business logic** for sending a file.

---

**Layer 6 (Presentation):**
```python
# Reading in binary mode
with open(file_path, 'rb') as file:
```
Ensures correct interpretation of binary data.

---

**Layer 5 (Session):**
```python
# Establishing a connection
client_socket.connect((server_host, server_port))
```
Starts a communication session with the server.

---

**Layer 4 (Transport):**
```python
# TCP Sockets: Reliable delivery
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
Requests reliable delivery via TCP.

---

**Layer 3 (Network):**
> Handled internally by your system.  
When you specify `"127.0.0.1"`, your machine uses IP routing internally.

---

**Layer 2 (Data Link):**
> Managed by your network adapter (Ethernet/Wi-Fi card).  
Frames are built to move the packets over local networks.

---

**Layer 1 (Physical):**
> Electricity over cables, wireless signals over antennas, etc.  
You don't code for this — it happens at the hardware level.

