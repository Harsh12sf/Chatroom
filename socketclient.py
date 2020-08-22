import socket
import threading

PORT = 5050
HEADER=64
format='utf-8'
disconmsg='DISCONNECT!'
viewmsg='VIEW'
server="157.245.97.181"
addr=(server, PORT)
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(addr)
try:
	print(sock.recv(2048).decode(format))
	nam=input()
	name=nam.encode(format)
	sock.send(name)

	def send(msg):

		message=msg.encode(format)
		msglen=len(message)
		send_length = str(msglen).encode(format)
		send_length +=b' ' * (HEADER - len(send_length))
		sock.send(send_length)
		sock.send(message)
		print(sock.recv(4096).decode(format))

	while(True):
		print("******** MENU ********\n1. Send a message \n2. Disconnect \n3. View Chat")
		option=int(input())
		if(option==1):
			print("Enter your message : ")
			msg=str(input())
			send(msg)
		elif(option==2):
			send(disconmsg)
			break
		elif(option==3):
			send(viewmsg)
		else:
			print("Enter a Valid Option")

except:

	print("An error occured, you will be disconnected")
	send(disconmsg)
#send("Oh Balle!")
#	input()
#	send("I love bball")
#	input()
#	send("PG is better than lebron")

#	send(disconmsg)
