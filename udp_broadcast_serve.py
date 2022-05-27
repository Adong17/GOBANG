from socket import *



def udprecvmes():
    broadcastPort = 7788
    recvSocket = socket(AF_INET, SOCK_DGRAM)
    recvSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    recvSocket.bind(('', broadcastPort))
    print('Listening for broadcast at ', recvSocket.getsockname())
    while True:
        data, address = recvSocket.recvfrom(65535)
        break
    return address, data.decode('utf-8')

if __name__=='__main__':
    udprecvmes()

