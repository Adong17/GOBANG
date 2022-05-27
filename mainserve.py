from graphics import *
import time
import socket
import os
from tcp_client import *
from PIL import ImageGrab
from udp_broadcast_client import *
from udp_broadcast_serve import *
import threading
import Gobang2

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcp_socket.bind(('0.0.0.0', 7789))  # 绑定端口
tcp_socket.listen(128)  # 使套接字变为被动套接字


def recvmess():
    connfd, address = tcp_socket.accept()
    print("Connect from", address)  # 打印连接的客户端
    data = connfd.recv(1024)
    print(data.decode())
    return data.decode(), connfd

def simrecvmes(connfd):

    data = connfd.recv(1024)
    print(data.decode())
    return data.decode(), connfd

def simsendmes(sendbuf,connfd):

    connfd.send(sendbuf.encode()) # 发送字节串
    print(sendbuf)

def tcpsendmess(sendbuf,connfd):
    # 创建tcp套接字

    # server_addr = ipaddress
    # tcp_socket.connect(('0.0.0.0', 7789))

    # 发送接收消息
    connfd.send(sendbuf.encode()) # 发送字节串
    print(sendbuf)
    flag = True
    while(flag):
        data = connfd.recv(1024)
    if data:
        flag = False
    return data.decode()



def main():
    udpsendmes('欢迎来到孤独棋社，这里提供与人机对弈的五子棋，若想与服务器对弈，请与我连线,若想下棋，请通过TCP与我连线,端口号为7789')
    recvmes, connfd = recvmess()


    if recvmes == "我想与你连线":
        sendmes = input("输入消息为：")
        simsendmes(sendmes, connfd)
        # recvmes, connfd = simrecvmes(connfd)
        Gobang2.main(connfd)
    else:
        print('未连接成功，继续发送广播消息')

if __name__ == '__main__':
    main()