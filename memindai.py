import os
import pandas as pd

def load_attendance_data(filename):
    if os.path.exists(filename):
        df = pd.read_csv(filename)
        return df
    else:
        return pd.DataFrame(columns=["Nama", "Kehadiran"])

def save_attendance_data(df, filename):
    df.to_csv(filename, index=False)

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

        attendance_data = attendance_data.append({"Nama": nama, "Kehadiran": kehadiran}, ignore_index=True)

    save_attendance_data(attendance_data, filename)
    print("Data absensi telah disimpan.")

if __name__ == "__main__":
    main()
    
