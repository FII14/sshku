import socket

def scan_ports(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                result = sock.connect_ex((host, port))
                if result == 0:
                    open_ports.append(port)
        except socket.error:
            pass
    
    return open_ports

if __name__ == "__main__":
    host = input("Masukkan alamat host yang ingin dipindai: ")

    # Batas awal dan akhir port yang ingin dipindai (contoh: 1 hingga 65535)
    start_port = 1
    end_port = 65535

    open_ports = scan_ports(host, start_port, end_port)

    if open_ports:
        print(f"Port terbuka pada {host}:")
        for port in open_ports:
            print(f"- {port}")
    else:
        print(f"Tidak ada port terbuka pada {host}")
        
