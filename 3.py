#lap trinh quet cong:
import socket
target = input('Moi nhap ip hoac ten mien:')
def quet(target):
    try:
        ip=socket.gethostbyname(target)
        for port in range(1,65635):
            sock =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(0.025)
            result=sock.connect_ex((ip,port))
            if result == 0:
                print('Port {}: Open'.format(port))
            sock.close()
    except socket.gaierror:
        print('IP, hostname khong xu ly')
    except socket.error:
        print('Khong the ket noi voi may chu')
quet(target)