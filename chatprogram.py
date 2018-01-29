#server program
import socket
 
host='192.168.22.141'
port = 5000
print("The host is at: ",host)

s = socket.socket()
print('Socket created')
 
# Bind socket to local host and port
s.bind((host, port))
     
print('Socket binding complete')
 
# Start listening on socket
s.listen(3000)
print ('Socket now listening')
 
# Now keep talking to the client
while True:
    #wait to accept a connection
    conn, addr = s.accept()
    print ('Connected with ' + addr[0] + ':' + str(addr[1]))

    while True:
        data = conn.recv(1024)
        print(data.decode('ascii'))
        data=input('Server>')
        conn.send(data.encode('ascii')) 
    conn.close()
s.close()

#client program
import socket
 
host='192.168.106'
port = 5000
print("The host is at: ",host)

client = socket.socket()
print('Socket created')

client.connect((host,port))

while True:
  #data = client.recv(1024)
  data = input('Client> ')
  if not data:
      break
  client.send(data.encode('ascii'))
  data = client.recv(1024)
  if not data:
      break
  print (data.decode('ascii'))

client.close()




