import socket

host = input("Masukkan alamat host: ")
port = 22

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    if result == 0:
        print(f"Port {port} (SSH) terbuka pada {host}")
    else:
        print(f"Port {port} (SSH) tertutup pada {host}")
    sock.close()

except socket.error:
    print(f"Terjadi kesalahan saat mencoba terhubung ke {host} pada port {port}")

except socket.gaierror:
    print("Alamat host tidak valid atau tidak dapat dijangkau")
