import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9000))
server.listen()


client, address = server.accept()

done = False

while not done:
    msg = client.recv(1024).decode("utf-8")
    if(msg == "quit"):
        done = True
    else:
        print(msg)
    client.send(input("Message: ").encode('utf-8'))

client.close()
server.close()
# comment
