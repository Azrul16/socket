# 🖧 Socket Programming in Python

This repository contains implementations of various network programming problems using Python's socket library. The solutions cover different aspects of client-server communication, including file transfer, concurrency, and remote computation.

## 📋 Table of Contents
- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Problem Descriptions](#problem-descriptions)
- [Setup Instructions](#setup-instructions)
- [Installation Requirements](#installation-requirements)
- [How to Run](#how-to-run)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## 📝 Introduction

This project demonstrates the use of Python for creating network applications using sockets. The problems involve:
- Implementing file transfer using TCP and UDP sockets.
- Creating a concurrent file server capable of handling multiple clients using multithreading.
- Developing a remote calculator service that performs arithmetic operations based on client requests.

## 🛠 Technologies Used
- Python 3.6+
- Socket Programming
- Multithreading



## 🧩 Problem Descriptions

### Problem 1: Simple File Transfer Protocol (FTP)

**Description:**  
This solution implements a basic file transfer protocol using both TCP (connection-oriented) and UDP (connectionless) sockets. The client divides the file into chunks and sends them to the server. The server acknowledges receipt of each chunk (for TCP).

### Problem 2: Concurrent File Server with Multithreading

**Description:**  
This solution implements a concurrent file server that spawns a new thread for each client, allowing multiple clients to request files simultaneously.

### Problem 3: Remote Calculator Application

**Description:**  
The remote calculator allows the client to send two integers and an arithmetic operation (+, -, *, /, %) to the server. The server performs the operation and sends back the result.

### Problem 4: Streaming Client and Server Application
**Description:** This solution develops a streaming client and server application using connectionless sockets. The streaming client requests a multimedia file (audio or video) from the server. The server reads the file in chunks of randomly distributed sizes between 1000 and 2000 bytes and sends these chunks as datagram packets to the client. The client processes the received packets and can launch a media player to play the file while downloading is still in progress.

### Problem 5: Simple Chatting Application
**Description:** This solution implements a simple chatting application using both connection-oriented (TCP) and connectionless (UDP) sockets. Users can type messages and press "Enter" to send them. Each message must be acknowledged by a reply before another message can be sent. The chat stops when Ctrl+C is pressed on both sides. For UDP, messages are limited to 1000 characters.

### Problem 6: Multi-Client Chatting Application
**Description:** This solution extends the single client-single server chatting application to support multiple clients using connection-oriented sockets. The server uses threads to handle each client connection independently, allowing multiple clients to chat with the server simultaneously.

## 🤝 Contributing

Contributions are welcome! Please fork this repository and submit a pull request.

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Push to your forked repository
6. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 👤 Author

# Azrul Amaline

[LinkedIn](https://www.linkedin.com/in/azrul-amaline) | [GitHub](https://github.com/Azrul16)  
Email: azrul.amaline16@gmail.com
