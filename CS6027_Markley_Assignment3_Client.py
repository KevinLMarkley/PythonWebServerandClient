#Course: Adv Computer Networking - Spring 2019
#Instructor: Dr. Aledhari
#Kevin Markley
#Assignment 3

from socket import *

serverName = "localhost"    #Ran this through my own computer, may want to use a different name.
serverPort = 10000          #Used this port to avoid taking one that has predefined usage.

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentence = input("Input lowercase sentence:")

clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(1024)

print("From Server:", modifiedSentence.decode())

clientSocket.close()
