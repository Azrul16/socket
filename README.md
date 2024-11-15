# 🖧 Socket Programming in Python

This repository contains implementations of various network programming problems using Python's socket library. The solutions cover different aspects of client-server communication, including file transfer, concurrency, remote computation, streaming, and chatting applications.

## 📋 Table of Contents

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Problem Descriptions](#problem-descriptions)
- [Setup Instructions](#setup-instructions)
- [Installation Requirements](#installation-requirements)
- [How to Run](#how-to-run)
- [Examples](#examples)
- [Project Description](#project-description)
- [Challenges Faced](#challenges-faced)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## 📝 Introduction

This project demonstrates the use of Python for creating various network applications using sockets. The problems involve:

- Implementing file transfer using TCP and UDP sockets.
- Creating a concurrent file server capable of handling multiple clients using multithreading.
- Developing a remote calculator service for arithmetic operations.
- Implementing a streaming client-server application using connectionless sockets.
- Developing a single client-server chatting application using both TCP and UDP.
- Extending the single client-server chatting application to support multiple clients.

## 🛠 Technologies Used

- Python 3.6+
- Socket Programming
- Multithreading

## 🗂 Project Structure

```plaintext
socket-programming-python/
├── problem1/                   # File Transfer Protocol (FTP)
│   ├── tcp_server.py
│   ├── tcp_client.py
│   ├── udp_server.py
│   └── udp_client.py
├── problem2/                   # Concurrent File Server
│   ├── server.py
│   └── client.py
├── problem3/                   # Remote Calculator
│   ├── server.py
│   └── client.py
├── problem4/                   # Streaming Client-Server Application
│   ├── server.py
│   └── client.py
├── problem5/                   # Single Client-Server Chatting
│   ├── tcp_chat_server.py
│   ├── tcp_chat_client.py
│   ├── udp_chat_server.py
│   └── udp_chat_client.py
├── problem6/                   # Multi-Client Chatting Application
│   ├── server.py
│   └── client.py
├── LICENSE.md
└── README.md
```

## 🧩 Problem Descriptions

### Problem 1: Simple File Transfer Protocol (FTP)

**Description:**  
This solution implements a basic file transfer protocol using both TCP (connection-oriented) and UDP (connectionless) sockets. The client divides the file into chunks of 100 bytes and sends them to the server. The server acknowledges receipt of each chunk (for TCP). If the acknowledgment is not received within a timeout period, the client retransmits the chunk. For UDP, the file is sent as datagram packets without acknowledgment.

### Problem 2: Concurrent File Server

**Description:**  
This solution implements a concurrent file server using multithreading. Each client request spawns a new thread, allowing multiple clients to request files simultaneously. The server reads the specified file and sends its contents to the client.

### Problem 3: Remote Calculator Application

**Description:**  
The remote calculator accepts two integers and an arithmetic operation (+, -, *, /, %) from the client. The server performs the operation and returns the result to the client.

### Problem 4: Streaming Client-Server Application

**Description:**  
The streaming client requests a multimedia file (audio or video) from the server. The server reads the file in chunks of random sizes (between 1000 and 2000 bytes) and sends them as datagram packets. The client receives the packets and plays the stream in real-time.

### Problem 5: Single Client-Server Chatting Application

**Description:**  
This solution implements a simple chatting application using both TCP (connection-oriented) and UDP (connectionless) sockets. The user at the client side can send messages by pressing "Enter". Each message must receive a reply before another message is sent.

### Problem 6: Multi-Client Chatting Application

**Description:**  
This solution extends the single client-server chatting application to support multiple clients. The server handles each client in a separate thread, allowing multiple clients to chat with the server concurrently.
