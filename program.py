class BioData:
  def __init__(self, nama, kelas, umur, agama):
    self.nama = nama
    self.kelas = kelas
    self.umur = umur
    self.agama = agama
   
   def printNama(self):
    print(f"Nama anda: {self.nama}")
    
   def printKelas(self):
    print(f"Kelas anda: {self.kelas}")
   
Ahmad = BioData("Ahmad Borat", "12 IPA 1", "18 Tahun", "Islam")
Ahmad.printNama()
Ahmad.printKelas() 
