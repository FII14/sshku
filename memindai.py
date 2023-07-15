import csv
import os

def load_attendance_data(filename):
    data = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            data = [row for row in reader]
    return data

def save_attendance_data(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nama", "Kehadiran"])
        writer.writerows(data)

def main():
    filename = "absensi_kelas.csv"
    attendance_data = load_attendance_data(filename)

    while True:
        nama = input("Masukkan nama siswa (atau 'selesai' untuk keluar): ")
        if nama.lower() == 'selesai':
            break

        kehadiran = input("Masukkan status kehadiran ('hadir' atau 'tidak hadir'): ")
        if kehadiran.lower() not in ['hadir', 'tidak hadir']:
            print("Status kehadiran tidak valid. Masukkan 'hadir' atau 'tidak hadir'.")
            continue

        attendance_data.append([nama, kehadiran])

    save_attendance_data(attendance_data, filename)
    print("Data absensi telah disimpan.")

if __name__ == "__main__":
    main()
