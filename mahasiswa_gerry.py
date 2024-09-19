class Mahasiswa:
    def update(self, nama, kelas, nim, dpa,
                 jurusan="D4 Manajemen Informatika",
                 fakultas="Vokasi",
                 kampus="Universitas Negeri Surabaya"):
        self.nama = nama
        self.kelas = kelas
        self.nim = nim
        self.dpa = dpa
        self.jurusan = jurusan
        self.fakultas = fakultas
        self.kampus = kampus

    def __init__(self, *args):
        self.update(*args)
    
    def printData(self):
        for key, value in vars(self).items():
            if key == "fakultas":
                print(f"{key.title()}\t:\t{value}")
            else:
                print(f"{key.title()}\t\t:\t{value}")
        print()
    
    def editData(self, **kwargs):
        data = vars(self)
        for key, value in kwargs.items():
            data[key] = value

        self.update(**data)


mahasiswa_1 = Mahasiswa("Gerry", "2023E", "164", "Pak Agung")
mahasiswa_1.printData()
mahasiswa_1.editData(nama="Gerry Moeis", kelas="2023F")
mahasiswa_1.printData()