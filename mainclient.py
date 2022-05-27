
from tcp_client import *
from PIL import ImageGrab
from udp_broadcast_client import *
from udp_broadcast_serve import *
import threading
from socket import *
import Gobang1

def recvmess(tcp_socket):
    connfd, address = tcp_socket.accept()
    print("Connect from", address)  # 打印连接的客户端
    data = connfd.recv(1024)
    print(data.decode())
    return data.decode(), connfd
def simsendmes(sendbuf,tcp_socket):
    tcp_socket.send(sendbuf.encode())  # 发送字节串

def tcpsendmess(sendbuf, ipaddress,tcp_socket):
    # 创建tcp套接字

    server_addr = ipaddress
    tcp_socket.connect((server_addr[0], 7789))

    # 发送接收消息
    tcp_socket.send(sendbuf.encode()) # 发送字节串
    print(sendbuf)
    flag = True
    while(flag):
        data = tcp_socket.recv(1024)
        if data:
            flag =False
    print(data.decode())
    return data.decode()

def main():
    address, data = udprecvmes()
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    # tcp_socket.connect(('192.168.3.22', 7789))
    print('Server received from {}:{}'.format(address, data))
    print("想与其通信，请输入 ‘TCP连线’")
    MSE = input("order:")
    if MSE =="TCP连线" :
        sendbuf = "我想与你连线"
        recvmes = tcpsendmess(sendbuf, address, tcp_socket)
        # simsendmes("明白了", tcp_socket)
        Gobang1.main(tcp_socket)
        tcp_socket.close()





if __name__ == '__main__':
    main()