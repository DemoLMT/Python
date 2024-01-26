import socket
import subprocess 
from datetime import datetime 
subprocess.call('clear', shell=True)
target = input("Moi nhap dia chi IP va ten mien: ")
def port_scan(target):
    try:
        #in thong bao
        ip = socket.gethostbyname(target)
        print("-" * 50)
        print("Scanning target:", ip)
        print("Time started:", datetime.now())
        print("-" * 50)
        #vong lap chinh
        for port in range(1, 65635):
           sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           sock.settimeout(0.025)# Đặt thời gian timeout cho việc kết nối socket tới 1 giây.
           result = sock.connect_ex((ip, port))
           if result == 0:
                print("Port {}: Open".format(port))
           sock.close()
    except socket.gaierror:
        print("Hostname could not be resolved.")
    except socket.error:
        print("Could not connect to the server.")
port_scan(target)