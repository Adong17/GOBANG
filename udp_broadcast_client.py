from socket import *

def udpsendmes(mes):
    broadcastPort = 7788


    sendSocket = socket(AF_INET, SOCK_DGRAM)
    sendSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

    network = '127.0.0.1'

    sendSocket.sendto(mes.encode('utf-8'), (network, broadcastPort))


if __name__ == '__main__':
    udpsendmes("我想跟你下围棋")