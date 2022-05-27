from socket import *

sendbuf = 'quit'
def tcpsendmess(sendbuf, ipaddress):
    # 创建tcp套接字
    sockfd = socket()  # 默认参数-->tcp套接字

    server_addr = ipaddress
    sockfd.connect((server_addr[0], 7789))

    # 发送接收消息
    sockfd.send(sendbuf.encode()) # 发送字节串
    print(sendbuf)
    data = sockfd.recv(1024)
    sockfd.close()
    return data.decode()

def tcprecvmess(sendbuf, ipaddress, port):
    sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockfd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sockfd.bind(('0.0.0.0', 8889))
    sockfd.listen(5)
    while True:
        print("Waiting for connect...")
        try:
            connfd, addr = sockfd.accept()
            print("Connect from", addr)  # 打印连接的客户端
        except KeyboardInterrupt:
            print("服务端退出")
            break
        except Exception as e:
            print(e)
            continue
        data = connfd.recv(1024)
    return data.decode()
def sendmess(sendbuf):
    # 创建tcp套接字
    sockfd = socket()  # 默认参数-->tcp套接字
    files = open("send.jpg", 'rb')

    # 连接服务端程序
    server_addr = ('192.168.3.35',8889)
    sockfd.connect(server_addr)

    # 发送接收消息
    sockfd.send(sendbuf.encode()) # 发送字节串
    data1 = sockfd.recv(1024)
    while (True):
        send = files.read(150000)
        if not send:
            break
        sockfd.send(send)
    data2 = sockfd.recv(1024)
    data = sockfd.recv(1024)
    files.close()
    sockfd.close()
    return data.decode()
    # 关闭套接字


if __name__=='__main__':
    sendmess(sendbuf)