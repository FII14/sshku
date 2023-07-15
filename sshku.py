import socket

def scan_port(host, port):
    try:
        # Membuat objek socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Mengatur waktu timeout menjadi 1 detik
        sock.settimeout(1)
        # Mencoba melakukan koneksi ke host dan port tertentu
        result = sock.connect_ex((host, port))
        # Jika koneksi berhasil, port terbuka
        if result == 0:
            print(f"Port {port} terbuka")
        else:
            print(f"Port {port} tertutup")
        # Menutup socket
        sock.close()

    except socket.error:
        print(f"Terjadi kesalahan saat mencoba terhubung ke {host} pada port {port}")

def main():
    host = input("Masukkan alamat host yang ingin dipindai: ")
    try:
        # Resolving alamat host ke alamat IP
        target_ip = socket.gethostbyname(host)
        print(f"Memindai port pada {host} ({target_ip})...")
        # Menjalankan fungsi scan_port() untuk memindai beberapa port
        for port in range(1, 1025):
            scan_port(target_ip, port)

    except socket.gaierror:
        print("Alamat host tidak valid atau tidak dapat dijangkau")

if __name__ == "__main__":
    main()
    
