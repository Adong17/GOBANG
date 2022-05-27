import socket
from time import sleep
import cv2
# 创建TCP套接字(AF_INET表示ipv4 SOCK_STREAM(流式))
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 重用服务端的IP和端口 (如果服务端的IP及端口在短时间内释放掉
# 那么就把之前的IP及端口重用上，就可以解决端口被占用问题)
sockfd.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

# 绑定地址
sockfd.bind(('0.0.0.0',8889))

# 设置监听
sockfd.listen(5)
flag = 0
# 阻塞等待客户端连接
while True:
    print("Waiting for connect...")
    try:
        connfd,addr = sockfd.accept()
        files = open("ROBOT.jpg", 'wb')
        flag=1
        # print("Connect from",addr)  # 打印连接的客户端
    except KeyboardInterrupt:
        print("服务端退出")
        break
    except Exception as e:
        print(e)
        continue

    sendas='Go'
    # 收发消息
    while True:
        data = connfd.recv(120)
        # 连接的客户端退出，recv会立即返回空字符串
        if not data:
            break
        print(data.decode())
        ss = connfd.send(sendas.encode())
        while True:
            data1 = connfd.recv(150000)
            files.write(data1)
            if not data1:
                break
            img = cv2.imread("ROBOT.jpg", cv2.IMREAD_COLOR)
            cv2.imshow('12', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            break
        files.close()
        ns = connfd.send(sendas.encode())
        sleep(0.1)
        sendbuf = input("Msg:")
        n = connfd.send(sendbuf.encode())
        break
    connfd.close()


# 关闭套接字
sockfd.close()