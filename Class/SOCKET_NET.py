"""
增加的功能：
    支持中文

功能：


"""
import socket
import time
from _thread import *

class Sn:   # 服务端
    """
    """
    def __init__(self):
        import socket
        # 创建Socket对象
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.ip = 'localhost'
        self.port = 12345
        self.header_length = 4      # 包头长度
        self.client_socket_list = list()    # 客服端连接列表(每个客服端连接都会加入到这个列表
        self.data_all = list()  #
    def Bind_listeners(self):     # 绑定监听
        try:
            self.server_socket.bind((self.ip, self.port))
        except socket.error as e:
            str(e)
        self.server_socket.listen(5)
    def threaded_client(self, num_conn, num_addr):      # 接收客服端包
        ip_dk = '%s:%d' % (num_addr[0], num_addr[1])
        while True:
            try:
                data_length = num_conn.recv(self.header_length)
                data_length.decode()
                js_cd = int(data_length)
                recv_msg = num_conn.recv(js_cd)
            except ConnectionResetError as con_rest:  # 报错应该是客服端关闭了连接
                print("客服端强制关闭", con_rest)
                self.client_socket_list.remove(("client", num_conn, num_addr))
                break
            else:
                if recv_msg:
                    try:
                        # 尝试对接收到的数据解码，如果解码成功，即使解码后的数据是ascii可显示字符也直接发送，
                        msg: str = recv_msg.decode()
                        self.data_all.append(msg)
                        # print(f'收到数据{num_addr}去掉头信息： {msg}')
                    except Exception as ret:
                        # 如果出现解码错误，提示用户选中16进制显示
                        ...
                    else:
                        ...

        print(ip_dk, "断开连接")
        num_conn.close()
        ...
    def run_server(self):
        while True:
            try:
                conn, addr = self.server_socket.accept()
            except Exception as ret:
                time.sleep(0.001)
            else:
                print(f"客服端{addr}已连接:")
                self.client_socket_list.append(("client", conn, addr))
                start_new_thread(self.threaded_client, (conn, addr))
    def get_data(self):
        if len(self.data_all) >= 1:
            g = self.data_all.pop(0)
            return g
        else:
            return None
    def send_All(self, num_data: str):    # 给所有人发送数据
        DH = "%04.d" % len(num_data.encode('utf-8'))
        for c in self.client_socket_list:
            try:
                c[1].sendall((DH+num_data).encode('utf-8'))
            except ConnectionResetError as con_rest:    # 报错应该是客服端关闭了连接
                print('ConnectionResetError 客服端关闭了连接')
    def send(self, num_conn, num_data):     # 给指定客服端发送数据
        numTemp = self.header_length
        DH = "%04.d" % len(num_data.encode('utf-8'))
        try:
            num_conn.sendall((DH + num_data).encode('utf-8'))
        except ConnectionResetError as con_rest:  # 报错应该是客服端关闭了连接
            print('ConnectionResetError 客服端关闭了连接')

class Cn:
    """
    """
    def __init__(self):
        import socket
        # 实例化一个socket对象，指明协议
        self.kfd_socket: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.ip = 'localhost'
        self.port = 12345
        self.header_length = 4  # 包头长度
        self.data_all = list()  #
    def lj_server(self):
        # 连接服务端socket
        self.kfd_socket.connect((self.ip, self.port))
    def threaded_(self):
        while True:
            try:
                data_length = self.kfd_socket.recv(self.header_length)
                data_length.decode()
                js_cd = int(data_length)
                recv_msg = self.kfd_socket.recv(js_cd)
            except ConnectionResetError as con_rest:  # 报错应该是服务端关闭了连接ConnectionResetError
                print("服务端强制关闭", con_rest)
                break
            else:
                if recv_msg:
                    try:
                        # 尝试对接收到的数据解码，如果解码成功，即使解码后的数据是ascii可显示字符也直接发送，
                        msg: str = recv_msg.decode()
                        self.data_all.append(msg)
                        # print(f'收到服务端数据去掉头信息： {msg}')
                    except Exception as ret:
                        # 如果出现解码错误，提示用户选中16进制显示
                        ...
                    else:
                        ...
        self.kfd_socket.close()
    def Run_Receive_data(self):
        start_new_thread(self.threaded_, ())
        """"""
    def get_server_data(self):
        if len(self.data_all) >= 1:
            g = self.data_all.pop(0)
            return g
        else:
            return None
    def send(self, num_data: str):
        DH = "%04.d" % len(num_data.encode('utf-8'))
        self.kfd_socket.sendall((DH+num_data).encode('utf-8'))



# ========================v测试代码v======================#
def cs():
    global s
    s.run_server()

if __name__ == '__main__':
    s = Sn()
    # s.ip = '192.192.192.192'
    s.Bind_listeners()
    start_new_thread(cs, ())


    time.sleep(0.5)
    while True:
        ml = input('调试:>')
        if ml == 'lb':
            for i in s.client_socket_list:
                print(i[0])
                print(i[1])
                print(i[2])
                print()
        elif ml == 'fs':
            for i in s.client_socket_list:
                print(i[0])
                print(i[1])
                print(i[2])
                cz = input('操作:>')
                if cz == 'y':
                    sj = '24680'
                    s.send(i[1], sj)
                print()

        elif ml == 'sendall':
            s.send_All("248")


