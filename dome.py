"""

======================

@author:niuqun

@time:2019/9/4:8:25 PM

@email:17689551930@163.com

======================

"""
# group=0
# import  threading
# def num1(the):
#     global group
#     for i in range(the):
#         max.acquire()
#         group+=1
#         max.release()
#     print("num1__________%d"%group)
# def num2(the):
#     global group
#
#     for i in range(the):
#         max.acquire()
#         group += 1
#         max.release()
#     print("num2_________%d"%group)
# max=threading.Lock()
# t1=threading.Thread(target=num1,args=(1000000,))
#
# t2=threading.Thread(target=num2,args=(1000000,))
# t1.start()
# t2.start()
import socket
import threading
def send_sms(socket_udb):
    while True:
        data = input()
        ip = input()
        port = int(input())
        socket_udb.sendto(data.encode("utf-8"),(ip,port))

def recv_sms(socket_udb):
    while True :
         data=socket_udb.recv_form(1024)
         print(data[1].encode("utf-8"))

def main():
    socket_udb=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    socket_udb.bind(("",9090))
    t1=threading.Thread(target=send_sms(socket_udb))
    t2=threading.Thread(target=recv_sms(socket_udb))
    t1.start()
    t2.start()
if __name__=="__main__":
    main()