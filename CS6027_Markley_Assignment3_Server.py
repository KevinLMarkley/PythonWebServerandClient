#Course: Adv Computer Networking - Spring 2019
#Instructor: Dr. Aledhari
#Kevin Markley
#Assignment 3

from socket import *

serverPort = 10000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("localhost", serverPort))	#Gave it the localhost name to use on my computer.

serverSocket.listen(1)
print("The server is ready to receive")

while True:
	connectionSocket, addr = serverSocket.accept()

	sentence = connectionSocket.recv(1024).decode()
	capitalizedSentence = sentence.upper()

	connectionSocket.send(capitalizedSentence.encode())

	connectionSocket.close()
