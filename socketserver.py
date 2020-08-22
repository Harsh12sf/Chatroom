import socket
import threading


try:
	#Socket contains a port and an IP address
	PORT = 5050
	HEADER=64
	#Getting IP address of computer
	#Google my public IP address and put that as ip and everyone around the world can access your server.
	ip="157.245.97.181"
	#Creating a socket
	server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	addr=(ip, PORT)
	#Binding socket and its values
	server.bind(addr)
	format='utf-8'
	disconmsg="DISCONNECT!"
	viewmsg='VIEW'
	listuser=[]
	ipuser=[]
	chatlist=[]

	def handle_client(conn,add):
		ind=ipuser.index(add)
		print(f"[NEW CONNECTION]{listuser[ind]} has connected with ip = {add}")
		connected=True
		while connected :
			msglen=conn.recv(HEADER).decode(format)
			if msglen:
				msglen=int(msglen)
				msg=conn.recv(msglen).decode(format)
				if(msg==disconmsg):
					connected= False
					print(f"[DISCONNECTED]{listuser[ind]} has disconnected....")
					del ipuser[ind]
					del listuser[ind]
				elif(msg!=disconmsg and msg!=viewmsg):
					print(f"[{listuser[ind]}] : {msg}")
					message = "[" + str(listuser[ind]) + "]" + ":" + msg
					print(message)
					chatlist.append(message)
					conn.send("Message Sent Successfully!".encode(format))
				elif(msg==viewmsg):
					if(len(chatlist) == 0):
						print(" There has been no chat ")
					elif(len(chatlist)!= 0):
						mas =" "
						for i in chatlist:
							mas = mas + str(i) + "\n"
						conn.send(mas.encode(format))
		print(ipuser)
		print(listuser)

		conn.close()

	namemsg="Enter your Name : "

	def start():
	#Listening for incoming connections
		server.listen()
		print(f"[LISTENING] Server is listening on {ip}")
		while True:
			conn,add = server.accept()
			ipuser.append(add)
			conn.send(namemsg.encode(format))
			name=conn.recv(2048).decode(format)
			listuser.append(name)
			thread=threading.Thread(target=handle_client, args = (conn,add))
			thread.start()
			print(f"[ACTIVE CONNECTIONS]{threading.activeCount()-1}")
			


	print("[STARTING] Server is starting ....")
	start()


except:

	print("error occured")
	server.shutdown(socket.SHUT_RDWR)
	server.close()
	print ("closed")