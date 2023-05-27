#G1A020036 - FADHILLA ILHAM ROBBANI
#Kelas B

# Membuat kelas Mahasiswa
class Mahasiswa:

    # Membuat init function atau constructor dari kelas Mahasiswa sehingga ketika
    # objek dibuat, kita bisa langsung mendefinisikan atributnya
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
    
    # Membuat fungsi untuk menampilkan daftar atribut dari kelas Mahasiswa
    def tampilkan_info(self):
        print("Nama: ", self.nama)
        print("NIM: ", self.nim)
        print("Jurusan: ", self.jurusan.NamaJurusan)

# Membuat kelas Jurusan
class Jurusan:

    # Membuat init function atau constructor dari kelas Jurusan sehingga ketika
    # objek dibuat, kita bisa langsung mendefinisikan atributnya
    # Untuk atribut DaftarMahasiswa nantinya bisa kita isi nilainya dari fungsi tambah_mahasiswa
    def __init__(self, nama_jurusan):
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = []
    
    # Membuat fungsi untuk menambah objek Mahasiswa baru ke dalam atribut DaftarMahasiswa
    def tambah_mahasiswa(self, mahasiswa):
        self.DaftarMahasiswa.append(mahasiswa)
    
    # Membuat fungsi untuk menampilkan daftar mahasiswa pada jurusan di kelas Jurusan saat ini
    def tampilkan_daftar_mahasiswa(self):
        #Agar mudah, di sini saya menggunakan string interpolation dengan f-string untuk menampilkan data dalam string
        print(f'Daftar Mahasiswa di Jurusan {self.NamaJurusan}: ')
        for mahasiswa in self.DaftarMahasiswa:
            print(mahasiswa.nama)

#Membuat kelas Universitas
class Universitas:

    # Membuat init function atau constructor dari kelas Universitas sehingga ketika
    # objek dibuat, kita bisa langsung mendefinisikan atributnya
    # Untuk atribut DaftarJurusan nantinya bisa kita isi nilainya dari fungsi tambah_jurusan
    def __init__(self, nama_universitas):
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = []
    
    # Membuat fungsi untuk menambah objek Jurusan baru ke dalam atribut DaftarJurusan
    def tambah_jurusan(self, jurusan):
        self.DaftarJurusan.append(jurusan)
    
    # Membuat fungsi untuk menampilkan daftar jurusan pada jurusan di kelas Universitas saat ini
    def tampilkan_daftar_jurusan(self):
        #Agar mudah, di sini saya menggunakan string interpolation dengan f-string untuk menampilkan data dalam string
        print(f'Daftar Jurusan di Universitas {self.NamaUniversitas}: ')
        for jurusan in self.DaftarJurusan:
            print(jurusan.NamaJurusan)


# Implementasi kelas Mahasiswa, Jurusan, dan Universitas

# Membuat objek Universitas dengan nama "XYZ University"
universitas_xyz = Universitas("XYZ University")

# Membuat objek Jurusan dengan nama "Teknik Informatika" dan menambahkannya ke XYZ University
jurusan_teknik_informatika = Jurusan("Teknik Informatika")
universitas_xyz.tambah_jurusan(jurusan_teknik_informatika)

# Membuat objek Mahasiswa dengan nama dan nim masing-masing, dan memasukkannya ke dalam Jurusan Teknik Informatika di Universitas XYZ
mahasiswa_1 = Mahasiswa("Fadhilla Ilham Robbani", "G1A020036", jurusan_teknik_informatika)
jurusan_teknik_informatika.tambah_mahasiswa(mahasiswa_1)

# Menampilkan daftar jurusan yang ada di Universitas XYZ
universitas_xyz.tampilkan_daftar_jurusan()

# Menampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ
jurusan_teknik_informatika.tampilkan_daftar_mahasiswa()


